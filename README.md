# IBM SpaceX Capstone — Falcon 9 Landing Prediction

**IBM Data Science Professional Certificate | Final Capstone**

Predict first-stage Falcon 9 landing success with SpaceX API data, Wikipedia scraping, pandas preprocessing, exploratory charts, SQLite, Folium, Plotly Dash, and supervised classifiers.

## Project code
The repository contains my API collection, web-scraping, EDA, SQL, Folium and machine-learning lab notebooks, plus `spacex_dash_app.py` (the Dash dashboard).

## Additional reproducible analysis
- [Measured results, limitations and provenance](analysis/RESULTS.md)
- [Four-model reanalysis script](analysis/reproduce_results.py)
- [All ten SQLite lab queries](analysis/spacex_sql_queries.sql)

## Summary of the measured results
- Historical EDA/modeling sample: **90 launches**, **60 successful** first-stage recoveries (66.7%).
- Recovery-rate examples: Kennedy LC-39A **17/22 (77.3%)**; Cape Canaveral SLC-40 **33/55 (60.0%)**.
- Re-executed classification: logistic regression and SVM each **15/18 = 83.3% held-out test accuracy**.
- Dash sample (56 launches): **24** successful recoveries; KSC LC-39A **10/13 (76.9%)**.
- Haversine coastline example: **0.595 km** from the lab's Cape Canaveral launch-pad and sample coastline coordinate.

**Data notes:** IBM's course samples vary by task (90 modeling / 56 dashboard / 101 SQL). The analysis above was reproduced from the shared IBM course datasets; it is not a claim of live SpaceX statistics. The 18-row test set is small and model accuracy is not guaranteed out of sample.

**Submission:** Upload the final PDF presentation to the Coursera peer-grading assignment. This repository is the GitHub URL to include in the submission.

