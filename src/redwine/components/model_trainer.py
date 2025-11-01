import os
import pandas as pd
from src.redwine import logger
from src.redwine.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def train_model(self):
        train_data = pd.read_csv(self.model_trainer_config.train_data_path)
        test_data = pd.read_csv(self.model_trainer_config.test_data_path)

        train_x = train_data.drop(self.model_trainer_config.target_column, axis=1)
        test_x = test_data.drop(self.model_trainer_config.target_column, axis=1)
        train_y = train_data[self.model_trainer_config.target_column]
        test_y = test_data[self.model_trainer_config.target_column]

        lr = ElasticNet(
            alpha=self.model_trainer_config.alpha,
            l1_ratio=self.model_trainer_config.l1_ratio,
            random_state=self.model_trainer_config.random_state
        )
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.model_trainer_config.root_dir, self.model_trainer_config.model_name))
        logger.info("Model training completed and model saved.")
