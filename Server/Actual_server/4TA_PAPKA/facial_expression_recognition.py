"""Facial expression recognition"""
import os
from tensorflow import keras
from deepface.DeepFace import analyze


def face_features(username, targetEmoton):
    """Function which identify facial emotion.
    :emotion(str): Facial emotion
    :img(numpy.ndarray): NumPy tensor representation of the image
    :return: Facial emotion and Gender
    :rtype: str
    """
    # Get image's path
    path_image = os.path.dirname(os.path.abspath(__file__)) + r'/Face_expressions' + rf'/{username}.png'

    # Convert the image to NumPy array with data type unsigned int(8 bit)
    img = keras.preprocessing.image.load_img(path_image)
    img = keras.preprocessing.image.img_to_array(img, dtype='uint8')

    # Predict whether facial emotion is
    # anger, fear, neutral, sad, disgust, happy or surprise
    features = analyze(img, actions=['emotion'], enforce_detection=False)
    emotion = features[0]['dominant_emotion']

    print(str(emotion))

    # Delete the images
    if(targetEmoton == emotion):
        return True
    os.remove(path_image)
    return False
