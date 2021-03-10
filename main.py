import pandas
import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
from math import sqrt

from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

import keras
from keras.models import Sequential, Input, Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU

import pymongo
import dns
from bson import ObjectId
import io
from PIL import Image
import pandas
from collections import Counter

# Get coordinates from data
def get_coordinates(center, size):
    # Check input
    if not center or not size:
        print("Error: Cannot get coordinates")
        return None
    
    # get position
    x_bottom_right  = int(center['x'] + size['x']/2)
    x_top_left      = int(center['x'] - size['x']/2)
    y_bottom_right  = int(center['y'] - size['y']/2)
    y_top_left      = int(center['y'] + size['y']/2)

    bottom_right  = (x_bottom_right, y_bottom_right)
    top_left      = (x_top_left, y_top_left)

    return top_left, bottom_right 


# Connect Database

# Process data

# 

def main():
    print('main')


if __name__ == "__main__":
    main()
