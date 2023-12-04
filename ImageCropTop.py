import cv2
import glob, os

# read all image in array
images = [cv2.imread(file) for file in glob.glob('Resource/LeftNone/*.png')]

folder_path = "Resource/LeftNone"  # Replace with the path to your folder
file_names = []

# List all files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_names.append("top-"+filename)  # file name

print(file_names)

# Save Images In Folder
x = 0
for image in images:
    forCut = image[117: 1145, 106: 748]  # image cropping axis values
    string = "top-page-{:03d}".format(x)
    cv2.imshow(string, forCut)
    savedImageFolderPath = 'imagesTopBottom/'  # folder path where we will save the images
    cv2.imwrite(os.path.join(savedImageFolderPath, file_names[x]), forCut)  # image saving in folder
    x = x + 1

cv2.waitKey(0)
cv2.destroyAllWindows()

# border 3|1|4|2
# TOP Corner(X(LEFT):Y(TOP)), Bottom Corner(X(RIGHT):Y(BOTTOM))