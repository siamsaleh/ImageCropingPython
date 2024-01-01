import cv2
import matplotlib.pyplot as plt
import numpy as np
import support_class


def get_all_detected_point(loc):
    # all uniq point detected will be store here - tuple
    uniq_detected_points = []
    # all TEMPLATE MATCHING points
    detected_points = []  # this will be a list and the items will be tuple
    for pt in zip(*loc[::-1]):
        detected_points.append(pt)

    all_point_list = []  # type list
    for point in detected_points:
        if point in all_point_list:
            # exist pass
            pass
        else:
            # not exist
            uniq_detected_points.append(point)  # if not exist it is uniq point
            # add new circle all points
            all_point_list = all_point_list + support_class.points_in_circle_np(25, point[0], point[1])

    # TODO uncomment
    print(uniq_detected_points)
    print("Uniq ayah/points - {:d}".format(len(uniq_detected_points)))
    print(50 * "#")
    # [D] [1st priority A]
    uniq_detected_points = sorted(uniq_detected_points, key=lambda x: (x[1], -x[0]))
    return uniq_detected_points


def template_matching(image_path, save_file_name):
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('template/sample3.png', 0)
    h, w = template.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    plt.imshow(res, cmap='gray')

    threshold = 0.5  # Pick only values above 0.8. For TM_CCOEFF_NORMED, larger values = good fit.

    loc = np.where(res >= threshold)
    uniq_detected_points = get_all_detected_point(loc)

    # Outputs 2 arrays. Combine these arrays to get x,y coordinates - take x from one array and y from the other.
    # Reminder: ZIP function is an iterator of tuples where first item in each iterator is paired together,
    # then the second item and then third, etc.
    for pt in uniq_detected_points:
        # cv2.circle(img_rgb, pt, 25, (0, 0, 255), 2)  # circle
        # Draw rectangle around each object. We know the top left (pt),
        # draw rectangle to match the size of the template image.
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 5)  # Red rectangles with thickness 2.

    # TODO
    cv2.imwrite('' + save_file_name, img_rgb)

    # cv2.imshow("Matched image", img_rgb)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    print(image_path)
    print(50 * "#")
    return uniq_detected_points


def lr_position_detect(image_path, save_file_name):
    uniq_detected_points = template_matching(image_path, save_file_name)
    return uniq_detected_points


# lr_position_detect("imagesLeft/left-page-028.png", "test.png")
