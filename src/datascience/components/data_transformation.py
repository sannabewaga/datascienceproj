import os
import urllib.request
import zipfile
from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience import logger
import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_train_test_split(self):
        try:
            data = pd.read_csv(self.config.data_path)

            train, test = train_test_split(data, test_size=0.2, random_state=42)

            # Define file paths inside root_dir
            train_path = os.path.join(self.config.root_dir, "train.csv")
            test_path = os.path.join(self.config.root_dir, "test.csv")

            train.to_csv(train_path, index=False)
            test.to_csv(test_path, index=False)

            logger.info(f"Train and test files saved to {train_path} and {test_path}")

        except Exception as e:
            logger.error(f"Error in train-test split: {e}")
            raise

    def run(self):
        self.initiate_train_test_split()

        