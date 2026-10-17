# Feature backlog

| Priority | Feature | User problem | Behavior | Dependencies | Success test | Risks / tradeoffs | Status |
|---|---|---|---|---|---|---|---|
| P0 | Evidence-backed release | Teams cannot judge safe usefulness | Package table, utility, privacy and data card | Python stdlib | Reproducible release has all artifacts | Simple metrics can be overinterpreted | Shipped |
| P1 | Rare-record disclosure challenge | Average privacy hides copied outliers | Audit rare quasi-identifier combinations and nearest matches | Protected real evaluation set | Seeded rare copy detected and removed; utility stays in budget | Distance is not a privacy guarantee | Shipped |
| P1 | Attack ensemble | One membership threshold misses threats | Add shadow-model and attribute-inference attacks | ML library, attack splits | Seeded memorization is found by at least one attack | Attack results depend on attacker knowledge | Planned |
| P1 | Subgroup utility floor | Aggregate utility hides unusable minority slices | Report TSTR metrics with uncertainty per eligible subgroup | Larger holdout, bootstrap | Seeded subgroup collapse blocks release | Small groups yield noisy estimates | Planned |
| P2 | Constraint fidelity report | Plausible marginals can violate business rules | Declare and test cross-column constraints per synthesizer | Constraint DSL | All seeded impossible relationships are caught | Enforcement may distort utility | Planned |
| P2 | Differential-privacy frontier | Teams cannot choose privacy budget rationally | Sweep epsilon and plot attack/utility trade-off | DP synthesizer, accountant | Committee can identify feasible frontier or reject release | Epsilon is difficult to explain; utility may collapse | Explored |
| P2 | Purpose-bound approvals | A safe QA dataset may be unsafe for modeling | Bind release to purpose, fields, recipients, expiry | Identity and approval workflow | Out-of-purpose request cannot reuse approval | Adds governance friction | Explored |
| P3 | Linkage adversary | External datasets can re-identify rare rows | Simulate linkage with auxiliary attributes | Public auxiliary fixture | Seeded linkable records are flagged | Attacker assumptions may be unrealistic | Explored |
| P3 | Remediation portfolio | Row removal is not always best | Compare suppress, generalize, resample and DP noise | Multiple strategies | Pareto report shows privacy/utility changes | More choices can obscure accountability | Explored |
| P3 | Release drift monitor | Source changes make old evidence stale | Fingerprint source/schema and invalidate old reports | Registry, scheduled evaluation | Changed source cannot ship with prior card | Re-evaluation cost | Explored |
