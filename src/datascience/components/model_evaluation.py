import os
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from src.datascience.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def eval_metrics(self):
        # Load test data and model
        data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Separate features and target
        x_test = data.drop(columns=[self.config.target_column], axis=1)
        y_test = data[self.config.target_column]

        # Predict and calculate metrics
        pred = model.predict(x_test)
        mae = mean_absolute_error(y_test, pred)
        mse = mean_squared_error(y_test, pred)
        r2 = r2_score(y_test, pred)

        # MLflow setup
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            # Save metrics to file
            scores = {'mae': mae, 'mse': mse, 'r2_score': r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log parameters and metrics
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('mse', mse)
            mlflow.log_metric('r2', r2)

            
         
