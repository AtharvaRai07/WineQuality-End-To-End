# WineQuality — End-to-End

High-level, end-to-end example project for training and serving a red-wine quality prediction model.

This repository contains a lightweight ML pipeline that covers data ingestion, validation, transformation, model training, evaluation and a small Flask app to serve predictions. It's designed as a learning/example project and integrates basic experiment tracking (MLflow) and a simple UI for making single predictions.

## Features
- Download and ingest the Wine Quality dataset
- Validate and transform data (train/test split)
- Train an ElasticNet regression model and save the artifact
- Evaluate model and log metrics to MLflow (optionally configured to DagsHub)
- Simple Flask UI to submit wine measurements and get a predicted quality score

## Repo layout (important paths)
- `main.py` — runs the end-to-end pipeline (ingest → validate → transform → train → evaluate)
- `app.py` — small Flask app with `/` (form) and `/predict` endpoints
- `src/redwine/` — project source with pipeline and components
- `templates/` — HTML templates for the Flask UI (`index.html`, `results.html`)
- `artifacts/` — output artifacts (data, models, metrics)
- `config/` — `config.yaml` used by the configuration manager
- `requirements.txt` — Python dependencies

## Quickstart (Windows cmd)
1. Create and activate a virtual environment

```cmd
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies

```cmd
pip install -r requirements.txt
```

3. Run the full pipeline (creates artifacts/model.joblib and evaluation metrics)

```cmd
python main.py
```

4. Run the Flask app (web UI)

```cmd
python app.py
# open http://127.0.0.1:5000/ in your browser
```

## Prediction API
- Submit the form on the home page to POST to `/predict`.
- The server expects the following numeric inputs (example names are the form `name` attributes):
	- `fixed_acidity`, `volatile_acidity`, `citric_acid`, `residual_sugar`, `chlorides`,
		`free_sulfur_dioxide`, `total_sulfur_dioxide`, `density`, `pH`, `sulphates`, `alcohol`

The Flask app uses a small `PredictionPipeline` from `src/redwine/pipeline/prediction_pipeline.py` to create predictions. If you change input names in the template, update `app.py` accordingly.

## MLflow / DagsHub
- The project supports MLflow logging. By default MLflow writes to the local `mlruns/` folder.
- To push experiments to DagsHub (or a remote MLflow server) set the MLflow tracking URI and provide authentication (see DagsHub docs). Typical authentication options:
	- Create a `_netrc` file on Windows (`%USERPROFILE%\\_netrc`) containing your DagsHub username and personal access token
	- Set `MLFLOW_TRACKING_USERNAME` and `MLFLOW_TRACKING_PASSWORD` environment variables before running
- The tracking URI used in the example config is similar to: `https://dagshub.com/<owner>/<repo>.mlflow`

## Notes & troubleshooting
- If you get a 400/403 when posting predictions, confirm the form `name` attributes match what `app.py` expects and the MLflow authentication (for remote logging) is correct.
- If your Flask app returns `Bad Request` when submitting the form, ensure all fields include `name` attributes and the `<form>` uses `method="post"`.
- Model file path and config values are defined in `config/config.yaml` and read by the configuration manager.

## Extending this project
- Add preprocessing/scaling pipelines and persist them with the model (recommended)
- Add more robust input validation and error handling in the Flask UI
- Add Dockerfile / deployment scripts to containerize the app
- Add unit tests for pipeline components

## License & contact
This repository is provided as-is for learning purposes. See `LICENSE` for details.

Questions or improvements welcome — open an issue or a pull request.

## Maintainer
- Name: Atharva Rai
- Email: atharvarai07@gmail.com

Last updated: November 2025
