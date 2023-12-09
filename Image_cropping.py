import glob
import os

import cv2


def read_all_images():
    left_text_none_all_image_path = 'Resource/LeftNone/*.png'  # read all image in array
    right_text_all_image_path = 'Resource/Right/*.png'

    # Return Right Left None all images here
    return ([cv2.imread(file) for file in glob.glob(left_text_none_all_image_path)]
            + [cv2.imread(file) for file in glob.glob(right_text_all_image_path)])


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


def image_cropping(images, file_names, saved_image_folder_path):
    # Save Images In Folder
    x = 0
    for image in images:
        for_cut = image[117: 1145, 106: 748]  # image cropping axis values
        cv2.imwrite(os.path.join(saved_image_folder_path, file_names[x]), for_cut)  # image saving in folder
        x = x + 1


def show_image_cropping(images, top_right_y, bottom_left_y, bottom_left_x, top_right_x):
    for_cut = images[1][top_right_y: bottom_left_y, bottom_left_x: top_right_x]
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

lr_right_file_names = get_file_names("Resource/Right", "lr-")
lr_left_none_file_names = get_file_names("Resource/LeftNone", "lr-")
########################################################################################################################
# TODO LEFT NONE [117: 1145, 106: 748]
# show_image_cropping(left_none_images, 117, 1145, 106, 748)
# write_cropped_image_in_folder(left_none_images, left_none_file_names, "image/", 117, 1145, 106, 748)
########################################################################################################################
# TODO RIGHT [116: 1144, 88: 730]
# show_image_cropping(right_images, 116, 1144, 88, 730)
# write_cropped_image_in_folder(right_images, right_file_names, "image/", 116, 1144, 88, 730)
########################################################################################################################
# TODO TOP --- LEFT NONE [2: 117, 102: 750]
# show_image_cropping(left_none_images, 2, 117, 102, 750)
# write_cropped_image_in_folder(left_none_images, top_left_none_file_names, "imagesTop", 2, 117, 102, 750)
########################################################################################################################
# TODO BOTTOM --- LEFT NONE [1182: 1259, 98: 755]
# show_image_cropping(left_none_images, 1182, 1259, 98, 755)
# write_cropped_image_in_folder(left_none_images, bottom_left_none_file_names, "imagesBottom", 1182, 1259, 98, 755)
########################################################################################################################
# TODO TOP --- RIGHT [3: 116, 85: 729]
# show_image_cropping(right_images, 3, 116, 85, 729)
# write_cropped_image_in_folder(right_images, top_right_file_names, "imagesTop", 3, 116, 85, 729)
#######################################################################################################################
# TODO BOTTOM --- RIGHT [1182: 1259, 85: 729]
# show_image_cropping(right_images, 1182, 1259, 85, 729)
# write_cropped_image_in_folder(right_images, bottom_right_file_names, "imagesBottom", 1182, 1259, 85, 729)
########################################################################################################################

# LEFT RIGHT

#######################################################################################################################
# TODO RIGHT -- RIGHT_IMG [116, 1145 : 735, 766]
# show_image_cropping(right_images, 116, 1145, 735, 766)
# write_cropped_image_in_folder(right_images, lr_right_file_names, "imagesLeftRight", 116, 1145, 735, 766)
#######################################################################################################################
# TODO LEFT -- LEFT_IMG [117: 1145, 69: 99] not done
# show_image_cropping(left_none_images, 117, 1145, 69, 99)
# write_cropped_image_in_folder(left_none_images, lr_left_none_file_names, "imagesLeftRight", 117, 1145, 69, 99)
