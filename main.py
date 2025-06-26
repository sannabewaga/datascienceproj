from src.datascience import logger
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.components.data_validation import DataValidation
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.config.configuration import ConfigurationManager


def run_pipeline():
    try:
        logger.info("🔄 Starting Full ML Pipeline...")

        config = ConfigurationManager()

        # 1. Data Ingestion
        logger.info("🚚 Running Data Ingestion...")
        di = DataIngestion(config=config.get_data_ingestion_config())
        di.run()

        # 2. Data Validation
        logger.info("🔍 Running Data Validation...")
        dv = DataValidation(config=config.get_data_validation_config())
        dv.run_validation()

        # 3. Data Transformation
        logger.info("⚙️ Running Data Transformation...")
        dt = DataTransformation(config=config.get_data_transformation_config())
        dt.run()

        # 4. Model Training
        logger.info("🏋️ Running Model Training...")
        mt = ModelTrainer(config=config.get_model_trainer_config())
        mt.run()

        # 5. Model Evaluation
        logger.info("🧪 Running Model Evaluation...")
        me = ModelEvaluation(config=config.get_model_validation_config())
        me.eval_metrics()

        logger.info("✅ Pipeline execution completed successfully.")

    except Exception as e:
        logger.exception(f"❌ Pipeline failed due to: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()
