# SynthSeal

[![CI](https://github.com/MadanMohan0537/synthseal/actions/workflows/ci.yml/badge.svg)](https://github.com/MadanMohan0537/synthseal/actions/workflows/ci.yml)

SynthSeal packages a synthetic table with the evidence needed to judge it: distribution fidelity, train-on-synthetic/test-on-real utility, nearest-neighbor privacy risk, a rare-record disclosure challenge, and a plain-language data card.

> **Project Lab traceability:** Idea 14 — Privacy-Safe Synthetic Data Studio. SynthSeal is the product name; the original title is retained only as metadata.

## The concrete problem

Synthetic data is not safe merely because it is artificial. A generator can reproduce a rare source row while aggregate metrics still look healthy. Conversely, aggressive privacy remediation can destroy downstream utility. SynthSeal reports both dimensions and blocks the tempting shortcut of presenting one score as proof.

## Shipped MVP

- Deterministic Adult-shaped public-data fixture containing no real people
- Conditional Gaussian sampler for numeric columns and grouped categorical sampling
- Per-column aggregate distribution gap
- Nearest-centroid train-on-synthetic/test-on-real benchmark
- Normalized nearest-neighbor and membership-threshold privacy metrics
- Release packager producing CSV, JSON evidence, and a data card
- **P1 rare-record disclosure challenge:** audits low-frequency combinations separately
- Seeded copied-outlier experiment and deterministic removal remediation
- 20 focused tests and Python 3.11–3.13 CI

No credentials, external services, models, or network access are required.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
python -m synthseal.cli --output release
```

The release directory contains:

- `synthetic.csv` — remediated synthetic table
- `report.json` — utility and privacy evidence before and after remediation
- `DATA_CARD.md` — intended use, metrics, and prohibitions

## Rare-record experiment

The frozen fixture contains exactly one rare Graduate/Remote/high-income combination. The experiment intentionally appends an exact synthetic copy, audits rare keys separately, and removes exposed rows. Acceptance criteria are set before execution:

- detect the copied rare row;
- retain zero known rare exposures after remediation;
- keep the absolute TSTR utility gap below 0.25;
- report denominators rather than claiming formal privacy.

## Architecture

```text
source rows -> conditional sampler -> synthetic candidate
                                    -> utility suite
                                    -> privacy suite -> rare challenge -> remediation
                                                        -> release package
```

## Evidence boundaries

This is a portfolio-scale evaluation workflow, not a privacy guarantee. The fixture is synthetic; the membership check is a simple threshold attack; categorical distance is hand-designed; the generator does not provide differential privacy; and the utility model is intentionally lightweight. Real releases require legal review, access controls, protected evaluation data, stronger attacks, purpose-specific models, and explicit privacy budgets. See [method and limitations](docs/METHOD.md) and [feature backlog](docs/BACKLOG.md).

## License

MIT
