from src.redwine.pipeline.data_ingestion_pipeline import DataIngestionPipeline, STAGE_NAME
from src.redwine import logger

logger.info("Welcome to Red Wine Quality Prediction Project")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage {STAGE_NAME} failed due to error: {e} <<<<<<")
        raise str(e)
