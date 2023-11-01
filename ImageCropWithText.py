import cv2
import glob

# read all image in array
images = [cv2.imread(file) for file in glob.glob('Resource/*.png')]

# No Text Page
# [132: 1131, 120: 735]
# border
# img[117: 1145, 106: 748]
# with text
# img[76: 1220, 82: 771]


# cv2.rectangle(img, (82, 76), (771, 1220), (0, 255, 0), 3)
# border 3|1|4|2
#   TOP Corner(X(LEFT):Y(TOP)), Bottom Corner(X(RIGHT):Y(BOTTOM))

# print(images)
x = 0
for image in images:
    string = "page-{:03d}".format(x)
    forCut = image[76: 1220, 82: 771]
    # cv2.imshow(string, forCut)
    # save image
    imageName = string + '.jpg'
    cv2.imwrite(imageName, forCut)
    x = x+1

cv2.waitKey(0)
cv2.destroyAllWindows()