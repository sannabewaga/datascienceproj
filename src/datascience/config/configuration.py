from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import DataIngestionConfig,DataValidationConfig
from box import ConfigBox
from pathlib import Path


class ConfigurationManager:
    def __init__(self, 
                 params_file_path: str = PARAMS_FILE_PATH, 
                 config_file_path: str = CONFIG_FILE_PATH, 
                 schema_file_path: str = SCHEMA_FILE_PATH) -> None:
        self.config: ConfigBox = read_yaml(Path(config_file_path))
        # self.params: ConfigBox = read_yaml(Path(params_file_path))
        self.schema: ConfigBox = read_yaml(Path(schema_file_path))
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=self.schema.COLUMNS
        )