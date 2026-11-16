# Falcon 9 historical launch dashboard

An interactive **Plotly Dash** application from the IBM Applied Data Science Capstone, reorganized into its own folder alongside its required dataset.

## Run

From the repository root, install the Python dependencies and start the app:

```bash
python -m pip install -r requirements.txt
python dashboard/app.py
```

Open the local URL printed by Dash (typically http://127.0.0.1:8050).

## Features

- Filter by launch site, including an “All Sites” option.
- View counts of successful recoveries across sites, or success/failure counts for an individual site.
- Restrict the payload-mass range and explore outcomes by booster version.

The bundled `spacex_launch_dash.csv` is the **56-row historical IBM dashboard sample**, which differs from the 90-row modeling and 101-row SQL datasets. The app runs locally, is not a deployed public service, and is not connected to live SpaceX launches.

The Dash source is based on the course tasks; it is kept simple rather than described as a production service.
