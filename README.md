# Falcon 9 First-Stage Landing Prediction

**IBM Data Science Professional Certificate · Applied Data Science Capstone**  
**Project:** Explore and classify first-stage recovery outcomes in historical Falcon 9 launch data.

![Model accuracy comparison](assets/model_comparison.svg)

> **Scope:** Course-based educational project using historical, curated IBM lab datasets. It is **not a live SpaceX prediction system**, nor are the lab datasets interchangeable. My submitted IBM lab notebooks and a separately reproduced analysis are both documented here.

## At a glance

| Part | Methods and tools |
|---|---|
| Collect | SpaceX API, Wikipedia/BeautifulSoup |
| Prepare | Python, Pandas, data validation, missing values, one-hot encoding |
| Analyze | SQL/SQLite, exploratory visualization |
| Explore | Folium launch-site maps, interactive Plotly Dash |
| Predict | Logistic regression, SVM, decision tree, KNN, scikit-learn |

### Results from the reproduced historical analysis

The EDA/modeling sample contains **90 launches**, with **60 successful first-stage recoveries** (66.7%). The best reported held-out test accuracy was **83.3% (15/18 flights)** for both logistic regression and SVM. Logistic regression also incorrectly predicted success for **3 of 6 actual failed recoveries**; this is an important limitation. On such a small test set, model ranking and estimated accuracy are uncertain.

For full method and source details, see the [results and provenance notes](analysis/RESULTS.md) and the [reproduction script](analysis/reproduce_results.py). A separate [recruiter-facing case study](docs/CASE_STUDY.md) explains the technical decisions and practical limitations.

## Explore the repository

- [Case study](docs/CASE_STUDY.md) — problem, workflow, methods, quantitative results, limitations
- [Measured results and data provenance](analysis/RESULTS.md) — model and chart evidence
- [Reproduce the model comparison](analysis/reproduce_results.py) — Python script
- [SQL queries](analysis/spacex_sql_queries.sql) — ten course queries
- [Interactive dashboard source](spacex_dash_app.py) — site and payload selectors
- [LinkedIn profile and post copy](docs/LINKEDIN.md) — attribution-aware descriptions
- Original course lab notebooks are provided in the repository root.

## Run the project

Python 3.10+ is recommended. From a terminal, clone the repository and create a virtual environment:

```bash
git clone https://github.com/aelshamlool0720-stack/IBM-SpaceX-Capstone.git
cd IBM-SpaceX-Capstone
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1` instead of `source .venv/bin/activate`.

**Dashboard:** The checked-in `spacex_launch_dash.csv` is the dedicated 56-row dashboard dataset.

```bash
python spacex_dash_app.py
```

Open the local URL shown by Dash (typically http://127.0.0.1:8050). This runs locally, **not as a hosted live demo**.

**Model reanalysis:** The script downloads two IBM datasets, so it requires internet access.

```bash
python analysis/reproduce_results.py
```

The script writes `analysis/model_results.json`. Use the [results notes](analysis/RESULTS.md) to compare model accuracy and confusion matrices.

**Other notebooks:** Open the `.ipynb` files with JupyterLab and run their cells, noting that API/web-scraping labs may depend on external services and website structure. The files are course-lab artifacts, not a single production pipeline.

## Data sets and caution

| IBM task | Data count |
|---|---:|
| EDA/modeling | 90 rows |
| Dash | 56 rows |
| SQLite lab | 101 rows |

These are snapshots selected for different IBM assignments. Do not compare rates across them without stating their denominators, or generalize them to current launches. Launch-site associations are not causal, and a random train/test split does not establish prospective performance on future launches.

## Attribution

This project is adapted from the **IBM Applied Data Science Capstone** course. It uses IBM SkillsNetwork historical course datasets, SpaceX API material, and public historical launch information. The additional modeling comparison is explicitly documented as a *separate reproduction* from the course samples. The project does not represent an affiliation with SpaceX.

## Next improvements

- Compare random holdout against a **chronological** validation split.
- Add tests for core data-processing functions and clearer data-download failures.
- Package reusable code rather than relying only on course notebooks.
- Report uncertainty and failure-class precision/recall alongside accuracy.

**Full report:** a refined PDF and editable PowerPoint were prepared separately for portfolio presentation. If you download those materials, upload the PDF to `reports/` before adding a link here.
