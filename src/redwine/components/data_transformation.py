import os
from src.redwine import logger
from src.redwine.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        self.data_transformation_config = data_transformation_config

    def train_test_split_data_and_scaling(self):
        data = pd.read_csv(self.data_transformation_config.data_path)
        logger.info("Data loaded successfully for transformation.")

        X = data.drop(self.data_transformation_config.target_column, axis=1)
        y = data[self.data_transformation_config.target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=self.data_transformation_config.test_size,
            random_state=self.data_transformation_config.random_state,
            stratify=y if self.data_transformation_config.stratify else None
        )

        sc = StandardScaler()
        X_train_scaled = sc.fit_transform(X_train)
        X_test_scaled = sc.transform(X_test)

        X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
        X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)

        train_scaled = pd.concat([X_train_scaled, y_train.reset_index(drop=True)], axis=1)
        test_scaled = pd.concat([X_test_scaled, y_test.reset_index(drop=True)], axis=1)

        train_scaled.to_csv(os.path.join(self.data_transformation_config.root_dir, "train.csv"), index=False)
        test_scaled.to_csv(os.path.join(self.data_transformation_config.root_dir, "test.csv"), index=False)

        logger.info("Train-test split completed and files saved.")
        logger.info(f"Train shape: {train_scaled.shape}, Test shape: {test_scaled.shape}")
