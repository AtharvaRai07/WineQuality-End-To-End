from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    """Configuration for data ingestion process."""
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    