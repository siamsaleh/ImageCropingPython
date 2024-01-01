import glob
import os

import cv2
import numpy as np


def get_file_names(folder_path, add_pre_text):
    file_names = []
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_names.append(add_pre_text + filename)  # file name

    return file_names


# cropped
def read_right_images():
    right_text_all_image_path = 'imageCroppedRight/*.png'
    return [cv2.imread(file) for file in glob.glob(right_text_all_image_path)]


# cropped
def read_right_trans_images():
    right_text_all_image_path = 'imagesTransparentRight/*.png'
    return [cv2.imread(file) for file in glob.glob(right_text_all_image_path)]


def read_left_images():
    left_text_all_image_path = 'imageCroppedLeft/*.png'
    return [cv2.imread(file) for file in glob.glob(left_text_all_image_path)]


def read_left_trans_images():
    left_text_all_image_path = 'imagesTransparentLeft/*.png'
    return [cv2.imread(file) for file in glob.glob(left_text_all_image_path)]


def points_in_circle_np(radius, x0, y0):
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:, np.newaxis] - x0) ** 2 + (y_ - y0) ** 2 <= radius ** 2)
    # x, y = np.where((np.hypot((x_-x0)[:,np.newaxis], y_-y0)<= radius)) # alternative implementation
    all_point_list = []
    for x, y in zip(x_[x], y_[y]):
        point = (x, y)
        all_point_list.append(point)
    return all_point_list
