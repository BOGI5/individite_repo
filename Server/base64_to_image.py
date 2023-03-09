"""Decode base64 data and create image"""
import base64


def get_image():
    """Function which decode base64 data and create image.
    :data(str): Two halves of the base64 data
    :text(str): Base64 data
    :img(str): Image type i.e. jpeg, jpg, png etc.
    """
    # Extract base64 data
    with open('message.txt', 'r') as file:
        text = file.read()

    # Remove the type from the base64 data
    data = text.split(',')[0] + ','
    text = bytes(text.replace(data, ''), 'utf8')

    # Get image type
    data = data.split('/')[1]
    image = data.split(';')[0]

    # Decode the base64 data
    text = base64.decodebytes(text)

    # Crete image
    with open(rf'image.{image}', 'wb') as file:
        file.write(text)
