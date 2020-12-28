import cv2
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

    cv2.imshow("Output", image)
    cv2.waitKey(0)

def main():
    print('Init project')
    path_image = "./image/test_dlib/thang.jpg"

    # test Dlib
    test_dlib(path_image)

    # Init Dlib

    # Detect ROI of face

    # Detect faces in the grayscale image

    # Loop over the face detections


if __name__ == "__main__":
    main()
