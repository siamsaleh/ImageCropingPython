from PIL import Image
import detect_lr_position


def overlay_images(overlay_top_path, output_path, position1=(0, 0), position2=(0, 0)):
    # Open the background and overlay images
    trans_top_lr = Image.open(overlay_top_path)

    # make white background as icon
    white_bg = Image.new("RGBA", (91, 335), (231, 247, 255, 255))
    trans_background = Image.new("RGBA", trans_top_lr.size, (255, 0, 0, 0))

    # Resize overlay images to fit the background
    overlay2 = trans_top_lr.resize(trans_background.size, Image.ANTIALIAS)

    # Create a copy of the background image
    result = trans_background.copy()

    # Overlay the first image
    result.paste(white_bg, position1, white_bg)

    # Overlay the second image
    result.paste(overlay2, position2, overlay2)

    # Save the result
    result.save(output_path, "PNG")


# left right cropped image path, left right cropped transparent image, output path
def overlay_image_bg(lr_img_path, trans_img_path, output_img_path):
    uniq_detected_points = detect_lr_position.lr_position_detect(
        lr_img_path, "test.png")

    if len(uniq_detected_points) > 0:
        # if icon available
        detected_point = uniq_detected_points[0][1]

        overlay_images(trans_img_path, output_img_path,
                       position1=(0, detected_point - 95), position2=(0, 0))
    else:
        # save same image
        img = Image.open(trans_img_path)
        img.save(output_img_path)
