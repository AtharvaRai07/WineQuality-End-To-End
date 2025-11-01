from src.redwine.config.configuration import ConfigurationManager
from src.redwine.components.data_ingestion import DataIngestion
from src.redwine import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self, config=ConfigurationManager()):
        self.config = config

    def initiate_data_ingestion(self):
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_config = self.config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage {STAGE_NAME} failed due to error: {e} <<<<<<")
        raise str(e)

