from src.redwine.config.configuration import ConfigurationManager
from src.redwine.components.data_transformation import DataTransformation
from src.redwine import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self, config = ConfigurationManager()):
        self.config = config

    def initiate_data_transformation(self):
        with open(Path("artifacts/data_validation/status.txt")) as f:
            status = f.read().strip().split(":")[-1].strip()
        if status == 'True':
            logger.info("Data validation status is True. Proceeding with data transformation.")
            data_transformation_config = self.config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config=data_transformation_config)
            data_transformation.train_test_split_data_and_scaling()
        else:
            logger.error("Data validation status is False. Data transformation cannot proceed.")
            raise Exception("Data validation failed. Cannot proceed to data transformation.")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage {STAGE_NAME} failed due to error: {e} <<<<<<")
        raise e
