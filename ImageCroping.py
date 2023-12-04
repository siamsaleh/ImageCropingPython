import cv2
import glob, os


def image_cropping(images, file_names, saved_image_folder_path):
    # Save Images In Folder
    x = 0
    for image in images:
        for_cut = image[117: 1145, 106: 748]  # image cropping axis values
        cv2.imwrite(os.path.join(saved_image_folder_path, file_names[x]), for_cut)  # image saving in folder
        x = x + 1
