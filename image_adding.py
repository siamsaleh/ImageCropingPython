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
#     img_over = Image.open(r"imagesAddBgRight/" + "trans-right-" + right_file_names[index])
#     img_over_original_r = Image.open(r"imagesAddBgRight/" + "trans-right-" + right_file_names[index])
#
#     # Resize
#     img_over_r = img_over_original_r.resize((int(img_over_original_r.width * .75), img_over_original_r.height),
#                                             Image.ANTIALIAS)
#
#     image_bg_width = img_bg.width
#     image_add_width_r = img_over_r.width
#
#     img_bg.paste(img_over_r, (image_bg_width - image_add_width_r + 7, 0), mask=img_over_r)
#     img_bg.save("finalImages/" + right_file_names[index])
#     # img_bg.paste(img_over, (image_bg_width - image_add_width + 7, 0), mask=img_over)
#     # img_bg.save("finalImages/" + right_file_names[index])
#
#     print(index)
#     index = index+1
########################################################################################################################
# TODO adding LEFT images
# index = 0
# for image in left_images:
#     img_bg = Image.open(r"imageCroppedLeft/" + left_none_file_names[index])
#     img_over = Image.open(r"imagesAddBgLeft/" + "trans-left-" + left_none_file_names[index])
#     img_over_original_l = Image.open(r"imagesAddBgLeft/" + "trans-left-" + left_none_file_names[index])
#
#     # Resize
#     img_over_l = img_over_original_l.resize((int(img_over_original_l.width * .75), img_over_original_l.height),
#                                             Image.ANTIALIAS)
#
#     image_bg_width = img_bg.width
#     image_add_width_l = img_over_l.width
#
#     img_bg.paste(img_over_l, (- 7, 0), mask=img_over_l)
#     img_bg.save("finalImages/" + left_none_file_names[index])
#     # img_bg.paste(img_over, (- 7, 0), mask=img_over)
#     # img_bg.save("finalImages/" + left_none_file_names[index])
#
#     print(index)
#     index = index+1
