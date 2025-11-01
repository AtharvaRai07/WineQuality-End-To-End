from src.redwine import logger
from src.redwine.config.configuration import ConfigurationManager
from src.redwine.components.model_trainer import ModelTrainer

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self, config = ConfigurationManager()):
        self.config = config

    def initiate_model_trainer(self):
        model_trainer_config = self.config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config)
        model_trainer.train_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage {STAGE_NAME} failed due to error: {e} <<<<<<")
        raise e
