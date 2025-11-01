from src.redwine.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.redwine.pipeline.data_validation_pipeline import DataValidationPipeline
from src.redwine.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.redwine import logger

logger.info("Welcome to Red Wine Quality Prediction Project")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage Data Ingestion started <<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> Stage Data Ingestion completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage Data Ingestion failed due to error: {e} <<<<<<")
        raise e

try:
    logger.info(f">>>>>> Stage Data Validation started <<<<<<")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> Stage Data Validation completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f">>>>>> Stage Data Validation failed due to error: {e} <<<<<<")
    raise e


try:
    logger.info(f">>>>>> Stage Data Transformation started <<<<<<")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> Stage Data Transformation completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f">>>>>> Stage Data Transformation failed due to error: {e} <<<<<<")
    raise e

