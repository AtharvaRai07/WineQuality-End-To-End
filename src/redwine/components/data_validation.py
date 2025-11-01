import os
import pandas as pd
from src.redwine import logger

from src.redwine.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig):
        self.data_validation_config = data_validation_config

    def validate_data(self) -> bool:
        """Validate the data based on the provided schema."""
        try:
            validation_status = None

            data = pd.read_csv(self.data_validation_config.unzip_data_dir)

            schema_dict = self.data_validation_config.all_schema
            schema_cols = self.data_validation_config.all_schema.keys()

            for col in data.columns:
                if col not in schema_cols:
                    logger.error(f"Column {col} not found in schema.")
                    validation_status = False
                else:
                    actual_dtype = str(data[col].dtype)
                    expected_dtype = str(schema_dict[col])

                    if actual_dtype != expected_dtype:
                        logger.error(f"Data type mismatch for column {col}: expected {expected_dtype}, got {actual_dtype}")
                        validation_status = False
                    else:
                        validation_status = True

            with open(self.data_validation_config.STATUS_FILE, 'w') as status_file:
                status_file.write(f"Validation Status: {validation_status}\n")
            logger.info(f"Data validation completed. Status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.error(f"Error during data validation: {e}")
            raise e
    