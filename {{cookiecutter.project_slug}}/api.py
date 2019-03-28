import os
import werkzeug
import re
from flask import Flask, jsonify, abort
from flask_restplus import Api, Resource, fields, reqparse

app = Flask(__name__)

api = Api(app, version='1.0', title='{{cookiecutter.project_name}}',
          description="{{cookiecutter.project_short_description}}",
          contact="hello@bmw.de")


TFL_MODEL = api.model("TFLite Model", {
    "model_name": fields.String(required=True, description="The model's name"),
    "inference_type": fields.String(required=True, description="The type of the model inference (e.g. image classification, object detection)")
})
TFL_MODELS = api.model("TFLite Model List", {
    'models': fields.List(fields.Nested(TFL_MODEL, description="The list of the uploaded models")),
    'loaded_model': fields.String(required=True, description="The name of the model loaded in memory", default=None)
})

@api.route('/models')
class Models(Resource):
    @api.doc("list_models")
    @api.marshal_with(TFL_MODELS)
    def get(self):
        """ Returns the list of uploaded models """
        models = []
        
        for model_name in os.listdir('models/'):
            try:
                conf = open("models/" + model_name + "/config", 'r')
                conf = conf.read().split("\n")
                models.append({
                    "model_name": model_name,
                    "inference_type": conf[0]
                })
            except Exception as ex:
                abort(500, str(ex))

        response = {
            "models": models,
            "loaded_model": "loaded_model"
        }
        return response




predict_parser = reqparse.RequestParser()
predict_parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help="The image to perform inference on")

@api.route('/predict')
@api.expect(predict_parser)
class Predict(Resource):
    @api.doc("predict")
    def post(self):
        """ Runs the model loaded in memory to infer on a given image """
        args = predict_parser.parse_args(strict=True)
        image = args['image']

        return []


@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': error.description}, 404)
    return response

@app.errorhandler(400)
def bad_request(error):
    response = jsonify({'error': error.description}, 400)
    return response

@app.errorhandler(500)
def internal_server_error(error):
    response = jsonify({'error': error.description}, 500)
    return response

if __name__ == '__main__':
    if not os.path.exists('models/'):
        os.makedirs('models/')
    app.run(host='0.0.0.0', port=5000, debug=True)
