import glob
import os

import cv2


def read_all_images():
    all_image_path = 'Resource/pages/*.png'  # read all image in array

    # Return all images here
    return [cv2.imread(file) for file in glob.glob(all_image_path)]


# add_pre_text = "top-"
def get_file_names(folder_path, add_pre_text):
    file_names = []
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_names.append(add_pre_text + filename)  # file name

    return file_names


def image_cropping(images, file_names, saved_image_folder_path):
    # Save Images In Folder
    x = 0
    for image in images:
        for_cut = image[117: 1145, 106: 748]  # image cropping axis values
        cv2.imwrite(os.path.join(saved_image_folder_path, file_names[x]), for_cut)  # image saving in folder
        x = x + 1


def show_image_cropping(images, top_right_y, bottom_left_y, bottom_left_x, top_right_x):
    # remove existing design left right
    images[1] = cv2.line(images[1], (110, 147), (110, 1653), (255, 255, 255), 50)
    images[1] = cv2.line(images[1], (1127, 147), (1127, 1653), (255, 255, 255), 50)

    for_cut = images[1][top_right_y: bottom_left_y, bottom_left_x: top_right_x]
    string = "top-page-{:03d}".format(4)
    cv2.imshow(string, for_cut)
    cv2.imwrite("test.png", for_cut)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_cropped_image_in_folder(images, file_names, folder_name,
                                  top_right_y, bottom_left_y, bottom_left_x, top_right_x):
    x = 0
    for image in images:
        # TODO Center only uncomment
        # # remove existing design left right (center)
        # image = cv2.line(image, (110, 147), (110, 1653), (255, 255, 255), 50)
        # image = cv2.line(image, (1127, 147), (1127, 1653), (255, 255, 255), 50)

        for_cut = image[top_right_y: bottom_left_y, bottom_left_x: top_right_x]
        cv2.imwrite(os.path.join(folder_name, file_names[x]), for_cut)
        x = x + 1


########################################################################################################################
# ALL Images
all_images = read_all_images()
image_file_names = get_file_names("Resource/pages", "")
########################################################################################################################

# CENTER

########################################################################################################################
# TODO Cropping --- ALL [147 : 1653, 110 : 1127]
# show_image_cropping(all_images, 147, 1653, 110, 1127)
# write_cropped_image_in_folder(all_images, image_file_names, "imagesCenter", 147, 1653, 110, 1127)
########################################################################################################################

# LEFT RIGHT

#######################################################################################################################
# TODO RIGHT -- ALL [147 : 1653, 1106 : 1191]
# show_image_cropping(all_images, 147, 1653, 1106, 1191)
# write_cropped_image_in_folder(all_images, image_file_names, "imagesRight", 147, 1653, 1106, 1191)
#######################################################################################################################
# TODO LEFT -- ALL [147 : 1653, 47 : 132]
# show_image_cropping(all_images, 147, 1653, 47,  132)
# write_cropped_image_in_folder(all_images, image_file_names, "imagesLeft", 147, 1653, 47,  132)
#######################################################################################################################

# TOP BOTTOM

#######################################################################################################################
# TODO TOP -- ALL [0 : 147, 110 : 1127]
# show_image_cropping(all_images, 0, 147, 110, 1127)
# write_cropped_image_in_folder(all_images, image_file_names, "imagesTop", 0, 147, 110, 1127)
#######################################################################################################################
# TODO BOTTOM -- ALL [1653 : 1754, 110 : 1191] not done
# show_image_cropping(all_images, 1653, 1754, 110,  1191)
# write_cropped_image_in_folder(all_images, image_file_names, "imagesBottom", 1653, 1754, 110,  1191)
#######################################################################################################################
