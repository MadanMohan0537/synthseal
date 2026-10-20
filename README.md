# Synthetic Data Release Audit

[![CI](https://github.com/MadanMohan0537/synthetic-data-release-audit/actions/workflows/ci.yml/badge.svg)](https://github.com/MadanMohan0537/synthetic-data-release-audit/actions/workflows/ci.yml)

**Package a synthetic table with the evidence needed to judge it: how closely it matches the source, whether it is still useful for modeling, and whether it leaks rare real records.**

A dependency-free Python MVP. The install name, the `synthseal` console script, and `python -m synthseal.cli` are still `synthseal`. The JSON report's `product` field and the data card title still say SynthSeal.

## Problem and who it's for

Synthetic data is not safe just because it is artificial. A generator can copy a rare source row while the aggregate statistics still look healthy. Heavy privacy fixes can also destroy usefulness. Data scientists, privacy reviewers, and the product or program owners who approve a data release need both sides together, instead of one quality score.

## Approach

1. Generate a synthetic table. Rows are drawn from education and target groups. Numeric columns (`age`, `income`, `hours`) come from a Gaussian using that group's mean and standard deviation, floored at 0. `region` is sampled from the same group.
2. Measure fidelity as one number, `distribution_gap`: the mean of scaled absolute differences of means on the numeric columns and total-variation distances on the categorical columns (`education`, `region`, `target`). Measure utility with train-on-synthetic, test-on-real (TSTR) using a nearest-centroid model on the numeric columns.
3. Measure privacy risk with normalized nearest-neighbor distance and a membership check. A synthetic row counts as a hit when that distance is at most 0.02.
4. Run a separate rare-record disclosure challenge. A category combination of `education`, `region`, and `target` is in scope when it occurs at most twice in the real rows passed to the audit. Exposed rows (distance at most 0.02) are removed.
5. Write a release folder: `synthetic.csv`, `report.json` (evidence before and after remediation), and `DATA_CARD.md`.

```text
source rows -> conditional sampler -> synthetic candidate
                                    -> utility suite
                                    -> privacy suite -> rare challenge -> remediation
                                                        -> release package
```

## What exists today

Checked against this tree by running the unit tests and `python -m synthseal.cli --output release` on Python 3.12:

- A deterministic Adult-shaped fixture of 240 rows in `synthseal/fixtures.py`. It is generated in process and contains no real people. It is not a copy of a public census file.
- The fixture's last row is its only Graduate/Remote/high-income record (`education` Graduate, `region` Remote, `target` 1, income 199000). The CLI trains on the first 179 rows plus that record, holds out the other 60 rows, generates 180 synthetic rows, and appends an exact copy of the rare record. That run reports 1 rare exposure before remediation and 0 after, and writes 180 released rows.
- On that same run, real-trained nearest-centroid accuracy is 52/60 (0.867 to three decimals) and synthetic-trained accuracy is 54/60 (0.900). The reported TSTR gap is real accuracy minus synthetic accuracy: -2/60, printed as -0.033.
- Release files from that command: `synthetic.csv`, `report.json`, and `DATA_CARD.md`.
- 20 unit tests in `tests/test_studio.py`, all passing in that run. `.github/workflows/ci.yml` is set up to run the same test command and the CLI on Python 3.11, 3.12, and 3.13.
- Shipped code is the sampler, those evidence metrics, exposed-row removal, and the release writer. `docs/BACKLOG.md` marks stronger attacks, subgroup utility, constraint checks, differential privacy, purpose-bound approval, linkage, remediation other than row removal, and drift monitoring as Planned or Explored. None of those are implemented.

## How success would be measured

| Measure | Status |
|---|---|
| Known rare-record exposures remaining after remediation | Not yet measured |
| Absolute TSTR utility gap kept below 0.25 | Not yet measured |
| Reviewer time to approve or reject a release | Not yet measured |
| Releases blocked for privacy reasons that a single score would have passed | Not yet measured |

`tests/test_studio.py` fails the utility test when the absolute gap on its own split is 0.25 or more. That check is not a committed measurement of the CLI figures above. `release/` is gitignored, and this repo has no stored evaluation results.

## Limitations

- This is an evaluation workflow. It does not provide a privacy guarantee, and the generator does not provide differential privacy.
- The fixture is synthetic. The membership check is a distance threshold (default 0.02). Categorical distance adds a fixed penalty when `education` or `region` differs. `target` is not part of that distance.
- The utility model is a nearest-centroid classifier on `age`, `income`, and `hours`.
- Remediation only deletes rows the rare-record challenge marks as exposed.
- A real release would also need legal review, access controls, protected evaluation data, stronger attacks, and an explicit privacy budget.

See [docs/METHOD.md](docs/METHOD.md) and [docs/BACKLOG.md](docs/BACKLOG.md).

## Quick start

Running the audit needs Python 3.11 or newer. The audit itself does not use credentials, models, or network access.

```bash
git clone https://github.com/MadanMohan0537/synthetic-data-release-audit.git
cd synthetic-data-release-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
python -m synthseal.cli --output release
```

## Deployment

Madan deploys with Cloudflare Workers:

```bash
npx wrangler deploy
```

Cloudflare Workers is the planned target and is not configured in this repository. This project is not deployed. That command still needs all of the following, and none of them are in the tree:

- `wrangler.toml`
- a Worker entry point
- Python Workers, or a JavaScript/TypeScript port of the Python `synthseal` package

## License

MIT. See [LICENSE](LICENSE).
