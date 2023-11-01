import cv2
import glob, os

# read all image in array
images = [cv2.imread(file) for file in glob.glob('Resource/LeftNone/*.png')]

###########################################################################

folder_path = "Resource/LeftNone"  # Replace with the path to your folder
file_names = []

# List all files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_names.append(filename)

print(file_names)

###########################################################################

# No Text Page
# [132: 1131, 120: 735]
# border
# img[117: 1145, 106: 748]

# print(images)
x = 0
for image in images:
    string = "page-{:03d}".format(x)
    forCut = image[117: 1145, 106: 748]
    # cv2.imshow(string, forCut)
    # save image
    # imageName = string + '.jpg'
    imageName = file_names[x]
    cv2.imwrite(imageName, forCut)
    x = x+1

cv2.waitKey(0)
cv2.destroyAllWindows()