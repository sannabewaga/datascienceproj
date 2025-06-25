import os  
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any, List
from src.datascience import logger  # Adjust as per your project structure

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    try:
        with open(file_path) as file:
            data = yaml.safe_load(file)
            logger.info(f"Successfully loaded {file_path} YAML file")
            return ConfigBox(data)
    except BoxValueError as e:
        logger.error(f"BoxValueError: {e}")
        raise ValueError("Invalid Box conversion") from e
    except Exception as e:
        logger.error(f"Error loading YAML file {file_path}: {e}")
        raise

@ensure_annotations
def create_directories(dir_paths: list, verbose: bool = True):
    for path in dir_paths:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
        except Exception as e:
            logger.error(f"Failed to create directory at: {path} — {e}")
            raise

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Saved JSON file at {path}")
    except Exception as e:
        logger.exception(f"Failed to save JSON at {path}: {e}")
        raise

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as f:
            content = json.load(f)
        logger.info(f"Loaded JSON file from {path}")
        return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"BoxValueError in JSON at {path}: {e}")
        raise ValueError("Invalid JSON to ConfigBox conversion") from e
    except Exception as e:
        logger.exception(f"Failed to load JSON at {path}: {e}")
        raise


@ensure_annotations
def save_model(path: Path, model: Any) -> None:
    try:
        joblib.dump(model, path)
        logger.info(f"Model saved at {path}")
    except Exception as e:
        logger.exception(f"Failed to save model at {path}: {e}")
        raise

@ensure_annotations
def load_model(path: Path) -> Any:
    try:
        model = joblib.load(path)
        logger.info(f"Model loaded from {path}")
        return model
    except Exception as e:
        logger.exception(f"Failed to load model from {path}: {e}")
        raise
