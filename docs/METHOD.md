# Method and limitations

## Study design

The deterministic fixture has 240 Adult-shaped rows and one intentionally rare combination. Training uses 179 ordinary rows plus the rare source row; a disjoint 60-row real holdout supports utility evaluation. Utility compares a nearest-centroid classifier trained on real data with the same classifier trained on synthetic data and tested on that untouched holdout.

Privacy evidence reports normalized nearest-real-record distance and the share of synthetic rows below a 0.02 attack threshold. The P1 challenge separately selects combinations occurring at most twice, inserts an exact rare copy, and verifies detection and removal.

## What the results mean

A small utility gap supports only this task and fixture. A low observed attack rate means this particular attack did not succeed often; it does not prove anonymity, differential privacy, or resistance to stronger adversaries.

## Limitations

- Data is synthetic and Adult-shaped, not a redistributed public dataset.
- The conditional sampler does not preserve all correlations.
- The classifier is not representative of every downstream use.
- Euclidean/categorical distance embeds subjective weights.
- Rare-key definitions depend on selected quasi-identifiers.
- Removing exposures can alter subgroup representation.
- No differential privacy, CTGAN, relational synthesis, UI, or access-control layer is implemented.
- Evaluation data would require protection in a real workflow.
