import os
from PIL import Image


def image_add_left(image_bg, image_add):
    image_bg.paste(image_add, (-7, 0), mask=image_add)
    image_bg.show()


def image_add_right(image_bg, image_add):
    image_bg_width = image_bg.width
    image_add_width = image_add.width
    # Pasting img2 image on top of img1
    # starting at coordinates (0, 0)
    image_bg.paste(image_add, (image_bg_width-image_add_width+7, 0), mask=image_add)
    image_bg.show()


# Here we can transparent image
# os.system('python3 utils/make_transparent.py "imagesRight/right-page-018.png" "output.png"')

# Opening the primary image (used in background)
img1 = Image.open(r"page-018.png")

# Opening the secondary image (overlay image)
img2 = Image.open(r"output.png")

# image_add_left(img1, img2)
image_add_right(img1, img2)


# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
# img1.paste(img2, (w1-w2 + 7, 0), mask=img2)
# img1.paste(img2, (-7, 0), mask=img2)

# Displaying the image
# img1.show()
