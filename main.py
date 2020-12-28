from cv2 import cv2
import dlib
from imutils import face_utils


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


def test_dlib(image):
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    p = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)

    # Load the input image and convert it to grayscale
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    rects = detector(gray, 0)

    # Loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv2.circle(image, (x, y), 8, (0, 255, 0), -1)

    return image


def main():
    print('Init project')
    path_image = "./image/test_dlib/thang.jpg"

    # test Dlib
    image = test_dlib(path_image)

    # Show image
    cv2.imshow("Output", image)
    cv2.waitKey(0)

    # Init Dlib

    # Detect ROI of face

    # Detect faces in the grayscale image

    # Loop over the face detections


if __name__ == "__main__":
    main()
