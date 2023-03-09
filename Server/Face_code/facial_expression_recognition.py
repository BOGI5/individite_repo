"""Facial expression recognition"""
import os
import tensorflow as tf
from deepface.DeepFace import analyze

# Get image's path
DIRECTORY = r'Face_expressions'
IMAGE = os.listdir(DIRECTORY)[0]
PATH_IMG = os.path.join(DIRECTORY, IMAGE)


def expression():
    """Function which identify facial emotion.
    :result(str): Facial emotion
    :img(numpy.ndarray): NumPy tensor representation of the image
    :return: Facial emotion
    :rtype: str
    """
    # Convert the image to NumPy array with data type unsigned int(8 bit)
    img = tf.keras.preprocessing.image.load_img(PATH_IMG)
    img = tf.keras.preprocessing.image.img_to_array(img, dtype='uint8')

    # Predict whether facial emotion is
    # anger, fear, neutral, sad, disgust, happy or surprise
    result = analyze(img, actions=['emotion'], enforce_detection=False)
    result = result[0]['dominant_emotion']

    os.remove(PATH_IMG)

    return result
