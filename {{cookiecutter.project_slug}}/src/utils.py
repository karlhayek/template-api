""" Stores functions that perform miscellaneous tasks """

import os
from pathlib import Path

MODELS_PATH = Path.cwd() / "models"


def get_models_info():
    """ Gets the names and inference type of all models present in /models """

    if not MODELS_PATH.is_dir():
        raise FileNotFoundError("The /models directory was not found!")

    models = []
    for model_name in os.listdir(MODELS_PATH):
        config_path = MODELS_PATH / model_name / "config.txt"
        with open(config_path, mode='r') as file:
            content = [line for line in file]

            models.append({
                "model_name": model_name,
                "inference_type": content[0]
            })
    return models
