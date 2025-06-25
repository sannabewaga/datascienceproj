import os
import urllib.request
import zipfile
from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet


class ModelTrainer:

    def __init__(self,config = ModelTrainerConfig):
        self.config = config


    def train_model(self):
        try:
            # Load training and testing data
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            # Separate features and target
            X_train = train_data.drop(self.config.target_column, axis=1)
            y_train = train_data[self.config.target_column]

            X_test = test_data.drop(self.config.target_column, axis=1)
            y_test = test_data[self.config.target_column]

            # Initialize model with config parameters
            model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
            model.fit(X_train, y_train)

            # Save the model
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            import joblib
            joblib.dump(model, model_path)

            logger.info(f"Model trained and saved at {model_path}")

        except Exception as e:
            logger.error(f"Error during model training: {e}")
            raise
    
    def run(self):
        self.train_model()


            