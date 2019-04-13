"""
    Contains the API code for the server to listen to and execute commands.
    Below is a simple, incomplete but running example of an API.
"""

import werkzeug
from flask import Flask, abort
from flask_restplus import Api, Resource, fields, reqparse
import model_utils
import utils

app = Flask(__name__)

api = Api(app, version='1.0', title='{{cookiecutter.project_name}}',
          description="{{cookiecutter.project_short_description}}",
          contact="")

# We define api models below to specify the response for some routes
TFL_MODEL = api.model("TFLite Model", {
    "model_name": fields.String(required=True, description="The model's name"),
    "inference_type": fields.String(required=True, description="The functionality of the model (e.g. image classification, object detection)")
})

PREDICTION_MODEL = api.model("Classification Result", {
    "class_name": fields.String(required=True, description="The predicted class"),
    "confidence": fields.Float(required=True, description="The classification score")
})

VERSION_MODEL = api.model("API Version", {
    "version": fields.String(required=True, description="The API version")
})


@api.route('/models')
class Models(Resource):
    # The .marshal_with and .marshal_list_with decorators
    # are for describing the content of the request's response
    @api.marshal_list_with(TFL_MODEL)
    def get(self):
        """ Returns the list of uploaded models """
        try:
            models = utils.get_models_info()
        except FileNotFoundError:
            abort(500, "The /models directory was not found!")

        return models


@api.route('/version')
class Version(Resource):
    @api.marshal_with(VERSION_MODEL)
    def get(self):
        """ Returns the API version"""
        return {"version": api.version}


# Below is a parser for parsing the arguments that the /predict route requires in HTTP requests
prediction_parser = reqparse.RequestParser()
prediction_parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files',
                               required=True, help="The image to perform inference on")
prediction_parser.add_argument('model_name', type=str, required=True,
                               help="The name of the model to be used for predictino")


@api.route('/predict')
@api.expect(prediction_parser)
class Predict(Resource):
    @api.marshal_with(PREDICTION_MODEL)
    def post(self):
        """ Runs the model loaded in memory to infer on a given image """

        args = prediction_parser.parse_args(strict=True)
        image = args['image']
        model_name = args['model_name']

        prediction = model_utils.predict(image, model_name)

        return prediction


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
