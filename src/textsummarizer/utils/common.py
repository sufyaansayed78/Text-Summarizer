import os 
from box.exceptions import BoxValueError
from pathlib import Path
import yaml
from src.textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any




def read_yaml(path_to_yaml) -> ConfigBox:
    with open(path_to_yaml, 'r') as yaml_file:
        try : 
            content = yaml.safe_load(yaml_file)
            logger.info(" File contents : ", content)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        except BoxValueError as e:
            logger.error(f"Error occurred while loading YAML file: {path_to_yaml} - {e}")
            raise e


def create_directories(path_to_directories) :
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")
        