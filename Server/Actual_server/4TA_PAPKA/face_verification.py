"""Face verification"""
import os
from deepface.DeepFace import verify
from tensorflow import keras


def check_image():
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
    accounts = os.path.dirname(os.path.abspath(__file__))

    directory += r'/Verify_face'
    accounts += r'/Face_images'
    p1 = os.path.dirname(os.path.abspath(__file__))
    p1 += r"/Verify_face"
    path_img_2 = os.listdir(p1)[0]
    path_img_2 = path_img_2.split('.')[0]
    img_1 = os.listdir(directory)[0]
    # Get images' paths
    path_img_1 = os.path.join(directory, img_1)


    # Find image type
    for i in os.listdir(accounts):
        if i.split('.')[0] == path_img_2:
            path_img_2 += '.' + i.split('.')[1]
            break
    path_img_2 = os.path.join(accounts, path_img_2)

    # Verify whether both images are the same person
    result = verify(path_img_1, path_img_2)['verified']

    # If the faces are the same person
    # return unique key that is string representation of the image NumPy array
    key = keras.preprocessing.image.load_img(path_img_2)
    key = keras.preprocessing.image.img_to_array(key, dtype='float32')

    # Delete the files
    os.remove(path_img_1)

    # If the faces are not the same person return False otherwise key
    return str(key) if result else False
