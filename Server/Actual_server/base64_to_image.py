"""Decode base64 data and create image"""
import base64
import os


def get_image():
    """Function which decode base64 data and create image.
    :name(str): Name of the user
    :data(str): Two halves of the base64 data
    :text(str): Base64 data
    :img(str): Image type i.e. jpeg, jpg, png etc.
    """
    # Get name and image files path
    img_path = r'/home/bogi5/Github/individite_repo/Server/Face_image_base64'
    name = os.listdir(img_path)[0]
    name = name.split('.')[0]
    img = os.path.join(img_path, name + '.txt')

    # Extract base64 data
    with open(img, 'r') as file:
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
    new_img = rf'Face_images/{name}.{image}'
    with open(new_img, 'wb') as file:
        file.write(text)
