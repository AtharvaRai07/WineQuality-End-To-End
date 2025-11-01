from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    """Configuration for data ingestion process."""
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    """Configuration for data validation process."""
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass
class DataTransformationConfig:
    """Configuration for data transformation process."""
    root_dir: Path
    data_path: Path
    target_column: str
    random_state: int
    test_size: float
    stratify: str


@dataclass
class ModelTrainerConfig:
    """Configuration for model trainer process."""
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    random_state: int
    target_column: str

@dataclass
class ModelEvaluationConfig:
    """Configuration for model evaluation process."""
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str
