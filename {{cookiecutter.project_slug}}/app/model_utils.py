""" Stores classes and functions that deal with ML models """


def predict(image, model_name):
    """ Runs the model to infer on the given image

    Arguments:
        image {Pillow Image} -- image to do prediction on
        model_name {str} -- name of the model to be used for prediction

    Returns:
        dict -- dictionary containing the predicted class along with the confidence
    """

    # Perform prediction magic here

    return {
        "class_name": "doggo",
        "confidence": 0.8
    }
