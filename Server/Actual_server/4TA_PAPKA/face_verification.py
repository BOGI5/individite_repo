"""Face verification"""
import os
from deepface.DeepFace import verify
from tensorflow import keras


def check_image(username):
    """
    :path_img_1(str): Path for the first image
    :path_img_2(str): Path for the second image
    :result(bool): True if the faces are the same person otherwise False
    :key(numpy.ndarray): NumPy tensor representation of the image
    :return: key if the faces are the same person otherwise return False
    :rtype: str or False
    """
    # get path to current directory
    directory = os.path.dirname(os.path.abspath(__file__))

    path_img_1 = directory + r'/Verify_face' + rf'/{username}.png'
    path_img_2 = directory + r'/Face_images' + rf'/{username}.png'


    # Verify whether both images are the same person
    try:
        result = verify(path_img_1, path_img_2)['verified']
    except:
        return False

    # If the faces are the same person
    # return unique key that is string representation of the image NumPy array
    key = keras.preprocessing.image.load_img(path_img_2)
    key = keras.preprocessing.image.img_to_array(key, dtype='float32')

    # Delete the files
   # os.remove(path_img_1)

    # If the faces are not the same person return False otherwise key
    return str(key) if result else False
