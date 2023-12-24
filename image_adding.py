from PIL import Image
import support_class

# ALL Images
all_images = support_class.read_all_images()
image_file_names = support_class.get_file_names("Resource/pages", "")

########################################################################################################################
# TODO adding LEFT RIGHT images
index = 0
for image in all_images:
    # for image in range(0, 10):
    img_bg = Image.open(r"imagesCenter/" + image_file_names[index])
    img_over_original_r = Image.open(r"imagesTransparentRight/" + "trans-" + image_file_names[index])
    img_over_original_l = Image.open(r"imagesTransparentLeft/" + "trans-" + image_file_names[index])

    # Resize
    img_over_r = img_over_original_r.resize((int(img_over_original_r.width * .75), img_over_original_r.height),
                                            Image.ANTIALIAS)
    img_over_l = img_over_original_l.resize((int(img_over_original_l.width * .75), img_over_original_l.height),
                                            Image.ANTIALIAS)

    image_bg_width = img_bg.width
    image_add_width_r = img_over_r.width
    image_add_width_l = img_over_l.width

    img_bg.paste(img_over_r, (image_bg_width - image_add_width_r + 7, 0), mask=img_over_r)
    img_bg.paste(img_over_l, (- 7, 0), mask=img_over_l)
    img_bg.save("finalImages/" + image_file_names[index])

    print(index)
    index = index + 1
