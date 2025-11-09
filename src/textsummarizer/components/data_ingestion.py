from urllib import request
import os
from pathlib import Path
import zipfile
from src.textsummarizer.entity.config_entity import DataIngestionConfig
from src.textsummarizer.logging import logger




class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> Path:
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.source_URL}...")
            request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"Data downloaded successfully and saved to {self.config.local_data_file}")
        else:
            logger.info(f"Data file already exists at {self.config.local_data_file}")
        
    def extract_zip(self) -> None:
            logger.info(f"Extracting data from {self.config.local_data_file} to {self.config.unzip_dir}...")
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Data extracted successfully to {self.config.unzip_dir}")