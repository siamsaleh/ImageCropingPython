from PIL import Image
import support_class

left_none_file_names = support_class.get_file_names("imageCroppedLeft/", "")
right_file_names = support_class.get_file_names("imageCroppedRight/", "")

right_images = support_class.read_right_images()
right_trans_images = support_class.read_right_trans_images()

left_images = support_class.read_left_images()
left_trans_images = support_class.read_left_trans_images()

########################################################################################################################
# TODO adding RIGHT images
# index = 0
# for image in right_images:
#     img_bg = Image.open(r"imageCroppedRight/" + right_file_names[index])
#     img_over = Image.open(r"imagesTransparentRight/" + "trans-right-" + right_file_names[index])
#
#     image_bg_width = img_bg.width
#     image_add_width = img_over.width
#
#     img_bg.paste(img_over, (image_bg_width - image_add_width + 7, 0), mask=img_over)
#     img_bg.save("finalImages/" + right_file_names[index])
#
#     print(index)
#     index = index+1
########################################################################################################################
# TODO adding LEFT images
index = 0
for image in left_images:
    img_bg = Image.open(r"imageCroppedLeft/" + left_none_file_names[index])
    img_over = Image.open(r"imagesTransparentLeft/" + "trans-left-" + left_none_file_names[index])

    image_bg_width = img_bg.width
    image_add_width = img_over.width

    img_bg.paste(img_over, (- 7, 0), mask=img_over)
    img_bg.save("finalImages/" + left_none_file_names[index])

    print(index)
    index = index+1

