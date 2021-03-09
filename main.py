import imutils
from cv2 import cv2
import dlib
from imutils import face_utils
from collections import OrderedDict

DYNAMIC_ROI_INDEXES = OrderedDict([
    ("Left_Cheek", ((1, 1), (39, 28), (48, 49), (5, 5))),
    ("Right_Cheek", ((15, 15), (42, 28), (54, 53), (11, 11))),
    ("Forehead", ((18, 19), (19, -1), (24, -1), (25, 24))),
    ("Chin", ((48, 57), (6, 6), (10, 10), (54, 57))),
    ("Nose", ((21, 21), (22, 22), (31, 30), (35, 30)))
])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class BoxObject:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right


class AcneObject:
    def __init__(self, box_object, matrix, top_left, bottom_right, real_point=None):
        self.box_object = box_object
        self.matrix = matrix
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.real_point = real_point

    def isBoxObject(self, box_object):
        if not isinstance(box_object, BoxObject):
            raise Exception("Please check BoxObject of acneObject")


def dimensionsFace(shape):
    top = shape[0]
    bottom = shape[0]
    left = shape[0]
    right = shape[0]
    for points in range(len(shape)):
        if shape[points][1] < top[1]:
            top = shape[points]
        if shape[points][1] > bottom[1]:
            bottom = shape[points]
        if shape[points][0] < left[0]:
            left = shape[points]
        if shape[points][0] > right[0]:
            right = shape[points]
    distance = 3 / 4 * (bottom[1] - top[1])
    center = (bottom[0], top[1] + 1 / 3 * distance)
    topLeft = (left[0], 0 if center[1] - distance < 0 else int(center[1] - distance))
    bottomRight = (right[0], int(center[1] + distance))
    return topLeft, bottomRight


def get_position_border_of_face(shape_68_point):
    # Return 2 point in raw image
    #   Top left of face
    #   Bottom Right of face

    min_x = min(shape_68_point[:, 0])  # min y
    max_x = max(shape_68_point[:, 0])  # max y
    min_y = min(shape_68_point[:, 1])  # min x
    max_y = max(shape_68_point[:, 1])  # max x

    distance = (max_y - min_y) / 4
    top_left = (min_x, int(min_y - distance))
    bottom_right = (max_x, max_y)
    return [top_left, bottom_right]


def test_dlib(image):
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    p = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)

    # Load the input image and convert it to grayscale
    image = cv2.imread(image)
    image = imutils.resize(image, width=720)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    rects = detector(gray, 0)
    rect = rects[0]

    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    for (x, y) in shape:
        cv2.circle(image, (x, y), 4, (255, 0, 0), -1)

    # TODO: Lấy toạ độ khuôn mặt (top left, bottom right)

    return shape, image


def main():
    print('Init project')
    path_image = "./image/test_dlib/thang.jpg"

    # test Dlib
    shape_68_point, image = test_dlib(path_image)
    # print('Shape: ', shape_68_point)

    # Get position of face in raw image
    position_of_face = get_position_border_of_face(shape_68_point)
    test_nguyen = dimensionsFace(shape_68_point)
    # check = bool(position_of_face == test_nguyen)
    print('position_of_face: ', position_of_face)

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    color = (0, 255, 0)  # Green
    thickness = 2
    # image = cv2.rectangle(image, test_nguyen[0], test_nguyen[1], color=color, thickness=thickness)
    # image = cv2.rectangle(image, position_of_face[0], position_of_face[1], color=color, thickness=thickness)

    # Show image
    # cv2.imshow("Output", image)
    # cv2.waitKey(0)

    import numpy as np
    import cv2 as cv
    # Create a black image
    # Draw a diagonal blue line with thickness of 5 px

    '''
    name: Left_Cheek,	 array_contour [[131 496]
    [307 469]
    [278 660]
    [218 743]]
    '''
    cv2.line(image, (131, 496), (307, 469), color, 2)
    cv2.line(image, (307, 469), (278, 660), color, 2)
    cv2.line(image, (278, 660), (218, 743), color, 2)
    cv2.line(image, (218, 743), (131, 496), color, 2)

    '''
        name: Right_Cheek,	 array_contour [[575 521]
     [432 469]
     [460 658]
     [493 746]]
     '''
    cv2.line(image, (575, 521), (432, 469), color, 2)
    cv2.line(image, (432, 469), (460, 658), color, 2)
    cv2.line(image, (460, 658), (493, 746), color, 2)
    cv2.line(image, (493, 746), (575, 521), color, 2)

    '''
    name: Forehead,	 array_contour [[199 328]
     [244, 210]
     [504  210]
     [545 346]]
    '''
    cv2.line(image, (199, 328), (244, 210), color, 2)
    cv2.line(image, (244, 210), (504, 210), color, 2)
    cv2.line(image, (504, 210), (545, 346), color, 2)
    cv2.line(image, (545, 346), (199, 328), color, 2)

    '''
    name: Chin,	 array_contour [[278 732]
     [257 789]
     [457 793]
     [460 732]]
    '''
    cv2.line(image, (278, 732), (257, 789), color, 2)
    cv2.line(image, (257, 789), (457, 793), color, 2)
    cv2.line(image, (457, 793), (460, 732), color, 2)
    cv2.line(image, (460, 732), (278, 732), color, 2)

    '''
    name: Nose,	 array_contour [[334 362]
     [419 364]
     [318 552]
     [427 552]]
     '''
    cv2.line(image, (334, 362), (419, 364), color, 2)
    cv2.line(image, (419, 364), (427, 552), color, 2)
    cv2.line(image, (318, 552), (334, 362), color, 2)
    cv2.line(image, (427, 552), (318, 552), color, 2)

    cv2.imshow("Output", image)
    cv2.waitKey(0)

    # Init Dlib

    # Detect ROI of face

    # Detect faces in the grayscale image

    # Loop over the face detections


if __name__ == "__main__":
    main()
