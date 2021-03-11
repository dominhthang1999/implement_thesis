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
from sklearn.cluster import AgglomerativeClustering


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


def get_default_size_for_roi(labels):
    DEFAULT_SIZE = {}
    acreages = []  # List acreage of all label in image
    sum_acreages = 0
    count_none_unknown = 0
    count_use = 0

    # Get list acreage in specify ROI
    for index, label in enumerate(labels):

        # pass not be label or None
        if not label['label_class'] or label['label_class'] == 'unknown':
            count_none_unknown += 1
            continue
        acreage_label = label['size']['x'] * label['size']['y']
        acreages.append(acreage_label)
        sum_acreages += acreage_label

        count_use += 1

    # NO has label
    if count_use == 0:
        return None

    # Has 1 or 2 labels
    if count_use <= 2:
        DEFAULT_SIZE = int(sqrt(max(acreages)))

    if count_use > 2:
        cluster_label = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
        # np_acreages = np.array(acreages)
        np_acreages = np.array(acreages).reshape(-1, 1)
        cluster_label.fit_predict(np_acreages)

        # Get list class label (Biggest)
        index_label_size_big = np.where(cluster_label.labels_ == 1)[0]

        # Calculator DEFAULT_SIZE for all label
        DEFAULT_SIZE = int(
            sqrt(sum([acreages[index_big] for index_big in index_label_size_big]) / len(index_label_size_big)))

    print(acreages)
    print(sum_acreages)
    print('Count NOT use ', count_none_unknown)
    print('Count use ', count_use)

    return DEFAULT_SIZE


# Process data
def get_all_acne_from_image(labels):
    acne = {
        'unknown': [],
        'Whitehead': [],
        'Blackhead': [],
        'Papules': [],
        'Pustules': [],
        'Other Acne': [],
        'Normal Skin': [],
        'Non-skin': [],
        'Non-acne': [],
        'Consider Acne': []
    }

    DEFAULT_SIZE = get_default_size_for_roi(labels)

    return acne


def get_all_acne_from_db(label_image_file):
    # Define acne
    acne = {
        'unknown': [],
        'Whitehead': [],
        'Blackhead': [],
        'Papules': [],
        'Pustules': [],
        'Other Acne': [],
        'Normal Skin': [],
        'Non-skin': [],
        'Non-acne': [],
        'Consider Acne': []
    }

    for index, label_image in enumerate(label_image_file):
        if label_image['uid'] == 106:
            result = get_all_acne_from_image(label_image['json_file']['labels'])
    return acne


def main():
    path = "mongodb+srv://user:ye1gkjKBIWGxjVEpUFxCoAjNnAdEeRYpiLeE4guhP4FxUHtGYCPMzdd11TtoJAyA" \
           "@multidisciplinary-lt0bz.azure.mongodb.net/<dbname>?authSource=admin&replicaSet=Multidisciplinary" \
           "-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true "

    print('Connecting Database')
    db = get_database(path)  # get db
    print('Done connect Database')

    # Get collection
    label_image = db['label_image']
    files = db['fs.files']
    chunks = db['fs.chunks']

    # Get all label
    label_image_file = label_image.find({})
    print('Get all acne from db')
    result = get_all_acne_from_db(label_image_file)

    print('DONE')


if __name__ == "__main__":
    main()
