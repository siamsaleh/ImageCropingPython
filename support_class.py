import glob
import os

import cv2


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


def read_all_images():
    all_image_path = 'Resource/pages/*.png'  # read all image in array

    # Return all images here
    return [cv2.imread(file) for file in glob.glob(all_image_path)]
