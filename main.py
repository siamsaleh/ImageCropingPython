import cv2
import glob
# from PIL import Image

# path = "Resource/IMG-20230913-WA0007.jpg"
# path = "imageJpg/IMG-20231101-WA0003.jpg"
path = "Resource/page-009.png"

img = cv2.imread(path)
print(img.shape)

rows, cols, _ = img.shape
print("Rows", rows)
print("Cols", cols)

# imdir = 'Resource'
# ext = ['png', 'jpg', 'gif']
#
# files = []
# [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
# images = [cv2.imread(file) for file in files]

# read all image in array
images = [cv2.imread(file) for file in glob.glob('Resource/*.png')]

# print(images)
# x = 0
# for image in images:
#     string = "File - {}".format(x)
#     forCut = image[132: 1131, 120: 735]
#     cv2.imshow(string, forCut)
#     x = x+1

# forCut = images[0][132: 1131, 120: 735]
# cv2.imwrite("page1.jpg", forCut)

# cut image
# cut_image = img[0: 1262, 0: 837]

# ROI (Region of Interest) 3|1|4|2
# cv2.rectangle(img, (120, 132), (735, 1131), (0, 255, 0), 3)
# border 3|1|4|2
cv2.rectangle(img, (106, 117), (748, 1145), (0, 255, 0), 3)
#   TOP Corner(X(LEFT):Y(TOP)), Bottom Corner(X(RIGHT):Y(BOTTOM))

# roi = img[130: 1131, 120: 736]
roi = img[117: 1145, 106: 748]
# No Text Page
# cut_image = img[132: 1131, 120: 735]

# cv2.imshow("Cut_Image", cut_image)
# cv2.imshow("Image", img)
cv2.imshow("Image", roi)

# width, height = 837, 1262
# imgResize = cv2.resize(img, (width, height))
# print(imgResize.shape)


# imgCropped = img[0:1262, 765:837]
# imgCropped = img[70:1226, 68:765]  # With sideBar   Top: Bottom, Left, Right
# imgCroppedWithoutText = img[0:1131, 127:837]  # With sideBar   Top: Bottom(BT Y), Left(TOP Y), Right

# cv2.imshow("Page Cropped", imgCropped)
# cv2.imshow("Page Cropped Without Text", imgCroppedWithoutText)

# cv2.imshow("Page", img)
# cv2.imshow("Page Resized", imgResize)

# cv2.imwrite("page1.jpg", cut_image)

# for image in images:
#     cv2.imshow(x, image)
#     x = x+1

cv2.waitKey(0)
cv2.destroyAllWindows()
