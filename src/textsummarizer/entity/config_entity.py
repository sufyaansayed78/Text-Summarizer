from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path 
    source_URL: Path 
    local_data_file: Path 
    unzip_dir: Path 

@dataclass
class DataTransformationConfig:
    """Data Transformation Configurations"""
    root_dir: Path 
    transformed_data_dir: Path
    tokenizer_name: str