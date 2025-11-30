import os
import yaml
import panas as pd
from src.custom_exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

def load_config(path):
    try:
        if path.exists():
            raise FileNotFoundError(f"File is not found at path: {path}")
        
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"File loaded successfully from {path}")
            return config
    except Exception as e:
        logger.error(f"Error loading file from {path}: {e}")
        raise CustomException("Failed to load YAML file", e)
        
    

def load_data(path):
    try:
        if not path.exists():
            raise FileNotFoundError(f"File is not found at path: {path}")
        
        data = pd.read_csv(path)
        logger.info(f"Data loaded successfully from {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {path}: {e}")
        raise CustomException("Failed to load data", e)

