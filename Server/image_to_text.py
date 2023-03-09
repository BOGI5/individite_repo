"""Text extraction from image"""
import os
from pytesseract import pytesseract
import tensorflow as tf

# Get image's path
DIRECTORY = r'Text_images'
IMAGE = os.listdir(DIRECTORY)[0]
PATH_IMG = os.path.join(DIRECTORY, IMAGE)


def extract_text():
    """Function which extracts text from image.
    :img(numpy.ndarray): NumPy tensor representation of the image
    :text(str): Extracted text
    :return: Text extracted from the image
    :rtype: str
    """
    img = tf.keras.preprocessing.image.load_img(PATH_IMG)
    text = pytesseract.image_to_string(img)
    return text
