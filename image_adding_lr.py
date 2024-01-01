from PIL import Image
import support_class
import add_bg_in_trans_img

left_none_file_names = support_class.get_file_names("imagesLeft/", "")
right_file_names = support_class.get_file_names("imagesRight/", "")

right_images = support_class.read_right_images()
right_trans_images = support_class.read_right_trans_images()

left_images = support_class.read_left_images()
left_trans_images = support_class.read_left_trans_images()

########################################################################################################################
# TODO adding RIGHT images
# index = 0
# for image in right_images:
#
#     add_bg_in_trans_img.overlay_image_bg(lr_img_path=r"imagesRight/" + right_file_names[index],
#                                          trans_img_path=
#                                          r"imagesTransparentRight/" + "trans-" + right_file_names[index],
#                                          output_img_path="imagesAddBgRight/" + "trans-" + right_file_names[index]
#                                          )
#
#     print(index)
#     index = index+1
########################################################################################################################
# TODO adding LEFT images
# index = 0
# for image in left_images:
#     add_bg_in_trans_img.overlay_image_bg(lr_img_path=r"imagesLeft/" + left_none_file_names[index],
#                                          trans_img_path=
#                                          r"imagesTransparentLeft/" + "trans-" + left_none_file_names[index],
#                                          output_img_path="imagesAddBgLeft/" + "trans-" + left_none_file_names[index]
#                                          )
#
#     print(index)
#     index = index + 1

# TEST
########################################################################################################################
# add_bg_in_trans_img.overlay_image_bg(lr_img_path="imagesLeft/left-page-028.png",
#                                      trans_img_path="trans-left-page-028.png",
#                                      output_img_path="imagesAddBgLeft/overlay.png"
#                                      )
