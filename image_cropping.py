import glob
import os

import cv2


def read_all_images():
    left_text_none_all_image_path = 'Resource/LeftNone/*.png'  # read all image in array
    right_text_all_image_path = 'Resource/Right/*.png'
    center_text_all_image_path = 'Resource/Center/*.png'

    # Return Center Right Left None all images here
    return ([cv2.imread(file) for file in glob.glob(left_text_none_all_image_path)]
            + [cv2.imread(file) for file in glob.glob(right_text_all_image_path)]
            + [cv2.imread(file) for file in glob.glob(center_text_all_image_path)])


def read_right_images():
    right_text_all_image_path = 'Resource/Right/*.png'
    return [cv2.imread(file) for file in glob.glob(right_text_all_image_path)]


# add_pre_text = "top-"
def get_file_names(folder_path, add_pre_text):
    file_names = []
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_names.append(add_pre_text + filename)  # file name

    return file_names


def read_left_none_images():
    left_text_none_all_image_path = 'Resource/LeftNone/*.png'
    return [cv2.imread(file) for file in glob.glob(left_text_none_all_image_path)]


def read_center_images():
    center_text_none_all_image_path = 'Resource/Center/*.png'
    return [cv2.imread(file) for file in glob.glob(center_text_none_all_image_path)]


def image_cropping(images, file_names, saved_image_folder_path):
    # Save Images In Folder
    x = 0
    for image in images:
        for_cut = image[117: 1145, 106: 748]  # image cropping axis values
        cv2.imwrite(os.path.join(saved_image_folder_path, file_names[x]), for_cut)  # image saving in folder
        x = x + 1


def show_image_cropping(images, top_right_y, bottom_left_y, bottom_left_x, top_right_x):
    for_cut = images[0][top_right_y: bottom_left_y, bottom_left_x: top_right_x]
    string = "top-page-{:03d}".format(1)
    cv2.imshow(string, for_cut)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_cropped_image_in_folder(images, file_names, folder_name,
                                  top_right_y, bottom_left_y, bottom_left_x, top_right_x):
    x = 0
    for image in images:
        for_cut = image[top_right_y: bottom_left_y, bottom_left_x: top_right_x]
        cv2.imwrite(os.path.join(folder_name, file_names[x]), for_cut)
        x = x + 1


########################################################################################################################
# LEFT NONE Images
left_none_images = read_left_none_images()
left_none_file_names = get_file_names("Resource/LeftNone", "")

top_left_none_file_names = get_file_names("Resource/LeftNone", "top-")
bottom_left_none_file_names = get_file_names("Resource/LeftNone", "bottom-")

# RIGHT Images
right_images = read_right_images()
right_file_names = get_file_names("Resource/Right", "")

top_right_file_names = get_file_names("Resource/Right", "top-")
bottom_right_file_names = get_file_names("Resource/Right", "bottom-")

# Center Images
center_images = read_center_images()
center_file_names = get_file_names("Resource/Center", "")

top_center_file_names = get_file_names("Resource/Center", "top-")
bottom_center_file_names = get_file_names("Resource/Center", "bottom-")

lr_right_file_names = get_file_names("Resource/Right", "right-")
lr_left_none_file_names = get_file_names("Resource/LeftNone", "left-")
lr_center_file_names = get_file_names("Resource/Center", "center-")
########################################################################################################################
# TODO LEFT NONE [142 : 1547, 179 : 1091]
# show_image_cropping(left_none_images, 142, 1547, 179, 1091)
# write_cropped_image_in_folder(left_none_images, left_none_file_names, "imageCroppedLeft/", 142, 1547, 179, 1091)
########################################################################################################################
# TODO RIGHT [142, 1547, 82, 996]
# show_image_cropping(right_images, 142, 1547, 82, 996)
# write_cropped_image_in_folder(right_images, right_file_names, "imageCroppedRight/", 142, 1547, 82, 996)
########################################################################################################################
# TODO CENTER [142, 1546 : 130, 1042]
# show_image_cropping(center_images, 142, 1546, 130, 1042)
# write_cropped_image_in_folder(center_images, center_file_names, "finalImages/", 142, 1546, 130, 1042)
########################################################################################################################

# TOP BOTTOM

########################################################################################################################
# TODO TOP --- LEFT NONE [3, 142, 179, 1091]
# show_image_cropping(left_none_images, 3, 142, 179, 1091)
# write_cropped_image_in_folder(left_none_images, top_left_none_file_names, "imagesTop", 3, 142, 179, 1091)
########################################################################################################################
# TODO BOTTOM --- LEFT NONE [1547, 1675, 179, 1091]
# show_image_cropping(left_none_images, 1547, 1675, 179, 1091)
# write_cropped_image_in_folder(left_none_images, bottom_left_none_file_names, "imagesBottom", 1547, 1675, 179, 1091)
########################################################################################################################
# TODO TOP --- RIGHT [3, 142, 82, 996]
# show_image_cropping(right_images, 3, 142, 82, 996)
# write_cropped_image_in_folder(right_images, top_right_file_names, "imagesTop", 3, 142, 82, 996)
#######################################################################################################################
# TODO BOTTOM --- RIGHT [1547, 1675, 82, 996]
# show_image_cropping(right_images, 1547, 1675, 82, 996)
# write_cropped_image_in_folder(right_images, bottom_right_file_names, "imagesBottom", 1547, 1675, 82, 996)
########################################################################################################################
# TODO TOP --- CENTER [3, 142 : 130, 1042]
# show_image_cropping(center_images, 3, 142, 130, 1042)
# write_cropped_image_in_folder(center_images, top_center_file_names, "imagesTop", 3, 142, 130, 1042)
#######################################################################################################################
# TODO BOTTOM --- CENTER [1546, 1678 : 130, 1042]
# show_image_cropping(center_images, 1546, 1678, 130, 1042)
# write_cropped_image_in_folder(center_images, bottom_center_file_names, "imagesBottom", 1546, 1678, 130, 1042)
########################################################################################################################

# LEFT RIGHT

#######################################################################################################################
# TODO RIGHT -- RIGHT_IMG [142, 1547, 1003, 1092]
show_image_cropping(right_images, 142, 1547, 1003, 1092)
# write_cropped_image_in_folder(right_images, lr_right_file_names, "imagesRight", 142, 1547, 1003, 1092)
#######################################################################################################################
# TODO LEFT -- LEFT_IMG [142, 1547, 80, 171]
# show_image_cropping(left_none_images, 142, 1547, 80, 171)
# write_cropped_image_in_folder(left_none_images, lr_left_none_file_names, "imagesLeft", 142, 1547, 80, 171)
#######################################################################################################################
