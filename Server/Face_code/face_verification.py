"""Face verification"""
import os
from deepface.DeepFace import verify
import tensorflow as tf

# Get images
DIRECTORY = r'Face_images'
IMG_1, IMG_2 = os.listdir(DIRECTORY)


def check_image():
    """
    :path_img_1(str): Path for the first image
    :path_img_2(str): Path for the second image
    :result(bool): True if the faces are the same person otherwise False
    :key(numpy.ndarray): NumPy tensor representation of the image
    :return: key if the faces are the same person otherwise return False
    :rtype: str or False
    """

    # Get images' paths
    path_img_1, path_img_2 = os.path.join(DIRECTORY, IMG_1), os.path.join(DIRECTORY, IMG_2)

    # Verify whether both images are the same person
    result = verify(path_img_1, path_img_2)['verified']

    # If the faces are the same person
    # return unique key that is string representation of the image NumPy array
    if result:
        key = tf.keras.preprocessing.image.load_img(path_img_1)
        key = tf.keras.preprocessing.image.img_to_array(key, dtype='float32')
        return str(key)

    # Delete the images
    os.remove(path_img_1)
    os.remove(path_img_2)

    # If the faces are not the same person return False
    return False
