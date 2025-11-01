import os
import urllib.request as request
from src.redwine import logger
import zipfile

from src.redwine.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config=DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def download_data(self):
        if not os.path.exists(self.data_ingestion_config.local_data_file):
            logger.info("Downloading data from source URL...")
            filename, _ = request.urlretrieve(
                url = self.data_ingestion_config.source_url,
                filename=self.data_ingestion_config.local_data_file
            )
            logger.info(f"Data downloaded successfully and saved to {filename}")
        else:
            logger.info("Data file already exists. Skipping download.")

    def extract_zip_file(self):
        unzip_path = self.data_ingestion_config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.data_ingestion_config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Data extracted successfully to {unzip_path}")
