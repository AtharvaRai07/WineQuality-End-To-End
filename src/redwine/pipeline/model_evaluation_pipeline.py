from src.redwine import logger
from src.redwine.config.configuration import ConfigurationManager
from src.redwine.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self, config = ConfigurationManager()):
        self.model_evaluation_config = config

    def initiate_model_evaluation(self):
        model_evaluation_config = self.model_evaluation_config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>>> Stage {STAGE_NAME} failed due to error: {e} <<<<<<")
        raise e

