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
    random_state: int
    test_size: float
    stratify: str


