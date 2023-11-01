import cv2
import glob, os

# read all image in array
images = [cv2.imread(file) for file in glob.glob('Resource/Right/*.png')]

###########################################################################

folder_path = "Resource/Right"  # Replace with the path to your folder
file_names = []

# List all files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_names.append(filename)

# print(file_names)

###########################################################################
# right
# img[116: 1144, 88: 730]

# cv2.rectangle(img, (88, 116), (730, 1144), (0, 255, 0), 3)
# border 3|1|4|2
#   TOP Corner(X(LEFT):Y(TOP)), Bottom Corner(X(RIGHT):Y(BOTTOM))

# print(images)
x = 0
for image in images:
    string = "page-{:03d}".format(x)
    forCut = image[116: 1144, 88: 730]
    # cv2.imshow(string, forCut)
    # save image
    # imageName = string + '.jpg'
    imageName = file_names[x]
    cv2.imwrite(imageName, forCut)
    x = x+1

cv2.waitKey(0)
cv2.destroyAllWindows()