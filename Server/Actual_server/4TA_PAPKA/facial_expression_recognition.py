"""Facial expression recognition"""
import os
from tensorflow import keras
from deepface.DeepFace import analyze


def face_features():
    """Function which identify facial emotion.
    :emotion(str): Facial emotion
    :img(numpy.ndarray): NumPy tensor representation of the image
    :return: Facial emotion and Gender
    :rtype: str
    """
    # Get image's path
    directory = r'Face_expressions'
    image = os.listdir(directory)[0]
    path_image = os.path.join(directory, image)

    # Convert the image to NumPy array with data type unsigned int(8 bit)
    img = keras.preprocessing.image.load_img(path_image)
    img = keras.preprocessing.image.img_to_array(img, dtype='uint8')

    # Predict whether facial emotion is
    # anger, fear, neutral, sad, disgust, happy or surprise
    features = analyze(img, actions=['emotion'], enforce_detection=False)
    emotion = features[0]['dominant_emotion']

    # Delete the images
    os.remove(path_image)

    return emotion
