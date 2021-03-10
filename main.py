import io
from collections import Counter
from math import sqrt

import cv2 as cv2
import dns
import keras
import numpy as np
import pandas
import pymongo
from bson import ObjectId
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.normalization import BatchNormalization
from keras.models import Input, Model, Sequential
from keras.utils import to_categorical
from matplotlib import pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split


# Get coordinates from data
def get_coordinates(center, size):
    # Check input
    if not center or not size:
        print("Error: Cannot get coordinates")
        return None

    # get position
    x_bottom_right = int(center['x'] + size['x'] / 2)
    x_top_left = int(center['x'] - size['x'] / 2)
    y_bottom_right = int(center['y'] - size['y'] / 2)
    y_top_left = int(center['y'] + size['y'] / 2)

    bottom_right = (x_bottom_right, y_bottom_right)
    top_left = (x_top_left, y_top_left)

    return top_left, bottom_right


# Connect Database
def get_database(path: str):
    # Check input
    if not path or not isinstance(path, str):
        print("Error: Cannot connect database")
        return None

    # Connect Database
    db = pymongo.MongoClient(path)
    main_db = None
    if db:
        main_db = db['<dbname>']
    return main_db


def show_image(image):
    pass


def get_image_from_db_by_name_image(name_image):
    pass


# Process data
def get_all_acne_from_image():
    pass


def get_all_acne_from_db():
    # loop image
    get_all_acne_from_image()


def main():
    path = ''
    db = get_database(path)  # get db

    # Get collection
    label_image = db['label_image']
    files = db['fs.files']
    chunks = db['fs.chunks']

    print('main')


if __name__ == "__main__":
    main()
