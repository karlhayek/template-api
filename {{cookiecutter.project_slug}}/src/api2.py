"""
    Contains the API code for the server to listen to and execute commands.
    Below is a simple, incomplete but running example of an API.
"""

from typing import List
from fastapi import FastAPI, Query, HTTPException, File
from pydantic import BaseModel, Schema

import model_utils
import utils

app = FastAPI(version='1.0', title='{{cookiecutter.project_name}}',
              description="{{cookiecutter.project_short_description}}")


# We define api models below to document expected request and response bodies

class VersionResponse(BaseModel):
    # Schema is used to give more information on each attribute of the model
    # use ellipsis ('...') to indicate the field is required
    version: str = Schema(..., description="API version")


class ModelsResponse(BaseModel):
    model_name: str
    inference_type: str = Schema(..., description="Functionality of the model")


class PredictionResponse(BaseModel):
    class_name: str = Schema(..., description="Predicted class")
    confidence: float = Schema(..., description="Classification score")


# Below we define the routes for the API

@app.get('/version', response_model=VersionResponse)
async def get_version():
    """ Returns the API version"""
    return {"version": app.version}


@app.get("/models", response_model=List[ModelsResponse])
async def get_models():
    """ Returns the list of uploaded models """
    try:
        models = utils.get_models_info()
    except FileNotFoundError:
        raise HTTPException(500, detail="The /models directory was not found!")

    return models


@app.post('/predict', response_model=PredictionResponse)
async def predict(
    model_name: str = Query(..., description="Name of model for inference"),
    image: bytes = File(..., description="Image to perform inference on"),
):
    """ Runs the model loaded in memory to infer on a given image """
    try:
        image = utils.convert_bytes_to_image(image)
    except Exception as ex:
        raise HTTPException(422, detail="Error while reading request image.\
            Please make sure it is a valid image. " + str(ex))

    prediction = model_utils.predict(image, model_name)

    return prediction
