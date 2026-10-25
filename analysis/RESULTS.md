# Executed results and rubric evidence

## Data provenance
Reanalysis uses IBM SkillsNetwork's standard Falcon 9 course datasets, also available in other public learner repositories. These **are not new SpaceX launches or live data**. Datasets differ by lab and should not be pooled: 90 launch rows for EDA/modeling, 56 rows for Plotly Dash, and 101 historical rows for SQL. User-uploaded EDA notebook contains five executed charts.

## Executed EDA findings (IBM 90-row modeling sample)
- 60 successes / 90 launches = **66.7%** recovery class.
- Cape Canaveral SLC 40: **33/55 = 60.0%**; Kennedy LC 39A: **17/22 = 77.3%**; Vandenberg SLC 4E: **10/13 = 76.9%**.
- GTO: **14/27 = 51.9%**; VLEO: **12/14 = 85.7%**.
- 2017: **15/18 = 83.3%**; 2019: **9/10 = 90.0%**; 2020: **16/19 = 84.2%**.

## SQL findings (IBM 101-row sample)
- Four launch-site labels: CCAFS LC-40, CCAFS SLC-40, VAFB SLC-4E, KSC LC-39A.
- NASA (CRS) customer records: **48,213 kg** total payload mass across 21 rows.
- F9 v1.1: **2,928.4 kg** mean payload mass across 5 rows.
- First recorded successful ground-pad landing: **2015-12-22**.
- Maximum recorded payload mass: **15,600 kg**.
- Historical landing-outcome ranking, 2010-06-04 to 2017-03-20: No attempt 10; Failure (drone ship) 5; Success (drone ship) 5; Success (ground pad) 5; Controlled (ocean) 3; Uncontrolled (ocean) 2; Failure (parachute) 1; Precluded (drone ship) 1.

## Dash findings (IBM 56-row sample)
- **24** successful first-stage recoveries.
- KSC LC-39A: **10/13 = 76.9%**, highest observed site success rate.
- v1.1: **1/15 = 6.7%**; FT: **16/24 = 66.7%**; B4: **6/11 = 54.5%**; B5: **1/1** (insufficient sample).
- Pie-chart success share is a count of successes, not the within-site success rate.

## Folium distance example
- CCSFS SLC 40: **28.5618571, -80.577366**.
- IBM lab's example coastline point: **28.56367, -80.57163**.
- Haversine distance: approximately **0.595 km**. This sample point is not a verified geographically nearest coastline.

## Re-executed machine learning comparison
Identical 90-row IBM dataset, 80 features; train/test split 72/18 using random_state=2. Training-only StandardScaler Pipeline and 5-fold stratified CV (shuffle=True, random_state=42) with GridSearchCV.

| Model | CV accuracy | Held-out accuracy | Confusion matrix [[TN,FP],[FN,TP]] |
|---|---:|---:|---|
| Logistic regression | 80.76% | **83.33%** | [[3,3],[0,12]] |
| Support vector machine | 80.76% | **83.33%** | [[3,3],[0,12]] |
| Decision tree | 83.43% | 72.22% | [[2,4],[1,11]] |
| K-nearest neighbors | 76.57% | 77.78% | [[2,4],[0,12]] |

Logistic regression is a good interpretable baseline tied for top held-out accuracy. The 18-sample test split is small; false predictions of success are important. The reported results are a **new reanalysis**, not copied from unseen outputs in the original learner notebook.

## Deliverable
Use the separate **Data Science Capstone Project Report.pdf** as the Coursera submission. It includes the results, method descriptions, charts, map analysis, evaluated models, and the repository link.
