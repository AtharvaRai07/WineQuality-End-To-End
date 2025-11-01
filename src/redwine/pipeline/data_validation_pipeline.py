from src.redwine.config.configuration import ConfigurationManager
from src.redwine.components.data_validation import DataValidation
from src.redwine import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self, config=ConfigurationManager()):
        self.config = config

    def initiate_data_validation(self):
        data_validation_config = self.config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config=data_validation_config)
        data_validation.validate_data()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage {STAGE_NAME} failed due to error: {e} <<<<<<")
        raise str(e)
