import os
import pandas as pd
from pathlib import Path
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from src.redwine.entity.config_entity import ModelEvaluationConfig
from src.redwine.utils.common import save_json
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
import numpy as np
import joblib

class ModelEvaluation:
    def __init__(self, model_evaluation_config:ModelEvaluationConfig):
        self.model_evaluation_config = model_evaluation_config

    def evaluate_metrics(self, true_value, predicted_value):
        rmse = np.sqrt(mean_squared_error(true_value, predicted_value))
        mae = mean_absolute_error(true_value, predicted_value)
        r2 = r2_score(true_value, predicted_value)
        return (rmse, mae, r2)

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.model_evaluation_config.test_data_path)
        model = joblib.load(self.model_evaluation_config.model_path)

        test_x = test_data.drop(self.model_evaluation_config.target_column, axis=1)
        test_y = test_data[self.model_evaluation_config.target_column]

        # signature = infer_signature(test_x,test_y)

        mlflow.set_tracking_uri(self.model_evaluation_config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_values = model.predict(test_x)

            (rmse,mea,r2) = self.evaluate_metrics(true_value=test_y, predicted_value=predicted_values)

            scores = {"rmse": rmse, "mea": mea, "r2": r2}
            save_json(Path(self.model_evaluation_config.metric_file_name), scores)

            mlflow.log_params(params=self.model_evaluation_config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mea", mea)
            mlflow.log_metric("r2", r2)

            mlflow.log_artifact(self.model_evaluation_config.metric_file_name)

            # if tracking_uri_type_store != "file":
            #     mlflow.sklearn.log_model(model, artifact_path="model")

            # else:
            #     mlflow.sklearn.log_model(model, artifact_path="model")


