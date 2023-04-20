"""Decode base64 data and create image"""
import base64
import os


def get_image(text, name, directory):
    """Function which decode base64 data and create image.
    :name(str): Name of the user
    :data(str): Two halves of the base64 data
    :text(str): Base64 data
    :img(str): Image type i.e. jpeg, jpg, png etc.
    """

    # Remove the type from the base64 data
    data = text.split(',')[0] + ','
    text = bytes(text.replace(data, ''), 'utf8')

    # Get image type
    data = data.split('/')[1]
    image = data.split(';')[0]

    # Decode the base64 data
    text = base64.decodebytes(text)

    # Crete image
    new_img = os.path.dirname(os.path.abspath(__file__))
    new_img += directory + str(name) + "." + image
    with open(new_img, 'wb') as file:
        file.write(text)
