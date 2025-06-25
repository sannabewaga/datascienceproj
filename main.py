from src.datascience import logger
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.components.data_validation import DataValidation
from src.datascience.config.configuration import ConfigurationManager

config = ConfigurationManager()  # create the manager
# data_ingestion_config = config.get_data_ingestion_config()  # get the config instance

# di = DataIngestion(config=data_ingestion_config)  # pass instance, not class
# di.run()
 

data_validation_config = config.get_data_validation_config()


dv = DataValidation(config=data_validation_config)
dv.run_validation()
