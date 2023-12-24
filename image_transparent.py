import glob
import os

import cv2
import support_class


def read_right_images():
    right_text_all_image_path = 'imagesRight/*.png'
    return [cv2.imread(file) for file in glob.glob(right_text_all_image_path)]


def read_left_none_images():
    left_text_none_all_image_path = 'imagesLeft/*.png'
    return [cv2.imread(file) for file in glob.glob(left_text_none_all_image_path)]


########################################################################################################################
all_lr_left_images = read_left_none_images()
all_lr_right_images = read_right_images()

left_none_file_names = support_class.get_file_names("imagesLeft/", "")
right_file_names = support_class.get_file_names("imagesRight/", "")
########################################################################################################################
# TODO LEFT TRANSPARENT
# count = 1
# index = 0
# for image in all_lr_left_images:
#     string = 'python3 utils/make_transparent.py "imagesLeft/' + left_none_file_names[index] + '" '
#     string = string + '"imagesTransparentLeft/trans-' + left_none_file_names[index] + '"'
#     os.system(string)
#     count = count + 1
#     index = index + 1
#     print(string + ' index - {:03d}\n'.format(index))

# TODO RIGHT TRANSPARENT
count = 1
index = 0
for image in all_lr_right_images:
    string = 'python3 utils/make_transparent.py "imagesRight/' + right_file_names[index] + '" '
    string = string + '"imagesTransparentRight/trans-' + right_file_names[index] + '"'
    os.system(string)
    count = count + 1
    index = index + 1
    print(string + ' index - {:03d}\n'.format(index))
