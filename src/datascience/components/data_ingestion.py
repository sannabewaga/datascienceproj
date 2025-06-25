import os
import urllib.request
import zipfile
from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience import logger



class DataIngestion:
    def __init__(self,config = DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading the input file at {self.config.local_data_file}")
            urllib.request.urlretrieve(self.config.source_url, self.config.local_data_file)
            logger.info("Download complete.")

        else:
            logger.info("File already exists")


    def unzip_file(self):
        if os.path.exists(self.config.local_data_file):
            logger.info(f"Extracting {self.config.local_data_file} to {self.config.unzip_dir}")
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info("Extraction complete.")
        else:
            logger.warning(f"ZIP file not found at {self.config.local_data_file}, cannot extract.")
        
    def run(self):
        self.download_file()
        self.unzip_file()
        