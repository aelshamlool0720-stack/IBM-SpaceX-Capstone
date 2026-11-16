# Falcon 9 Landing Prediction — Portfolio Case Study

**Project type:** Course-based IBM Data Science Professional Certificate capstone, with an additional reproduced analysis.  
**Repository:** [IBM-SpaceX-Capstone](https://github.com/aelshamlool0720-stack/IBM-SpaceX-Capstone)

## Problem

A recovered Falcon 9 first stage can be reused. This educational project asks whether historical launch attributes—including site, orbit, payload and flight sequence—help distinguish successful from unsuccessful first-stage recoveries. It is **not** an operational launch-risk system or a real-time analysis.

## Data and methods

- API acquisition from SpaceX and historical web scraping, with separate IBM-provided static lab datasets.
- Data cleaning and exploration with Pandas, plots and SQLite queries.
- Launch-site geographic analysis using Folium and an interactive Plotly Dash dashboard.
- Four classifiers: logistic regression, support vector machine, decision tree and k-nearest neighbors.
- For the reproduced model comparison: 90 rows, 72 training / 18 test rows, 5-fold stratified cross-validation on the training data, and tuned scikit-learn pipelines.

### Separate datasets by task

| Task | Rows | Reason |
|---|---:|---|
| EDA + predictive modeling | 90 | Curated historical launch sample |
| Plotly Dash | 56 | Separate dashboard exercise sample |
| SQLite analysis | 101 | Separate historical SQL exercise sample |

**Never mix their denominators or interpret them as live SpaceX data.** See [RESULTS.md](../analysis/RESULTS.md).

## Verified in the reproduced report

Of 90 modeling records, 60 have successful recovery class (66.7%). On the specific 18-row holdout:

| Classifier | Held-out accuracy |
|---|---:|
| Logistic regression | 83.3% (15/18) |
| SVM | 83.3% (15/18) |
| Decision tree | 72.2% (13/18) |
| K-nearest neighbors | 77.8% (14/18) |

The logistic-regression confusion matrix was **[[3, 3], [0, 12]]**, using unsuccessful recovery as class 0 and successful recovery as class 1. **Three of six real failures were incorrectly called successes.** Error type matters more than a single high accuracy number.

## Main lessons

1. Preprocessing should happen inside training/CV workflows, not on held-out test data.
2. Small historical samples produce uncertain performance estimates.
3. Recovery rates vary by era, site and orbit, but these descriptive differences do not prove causation.
4. The project shows an analytical workflow, not production MLOps, monitoring, or prospective reliability.

## Where to find everything

- [Reproduction script](../analysis/reproduce_results.py)
- [Recorded results and provenance](../analysis/RESULTS.md)
- [SQL exercise queries](../analysis/spacex_sql_queries.sql)
- [Dashboard application](../spacex_dash_app.py)
- [Project root README](../README.md)

## Authorship and attribution

The source notebooks follow the IBM Applied Data Science Capstone learning exercises, and the case-study report includes a separately reconstructed analysis using the IBM course datasets. This is an educational portfolio adaptation, not an independently collected commercial dataset, an endorsement by SpaceX, or an operational prediction product.
