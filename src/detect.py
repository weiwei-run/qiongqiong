import numpy as np
import cv2
import dlib
from PIL import Image

def crop(source, pos):
    x1 = pos[2][0]
    y1 = pos[2][1]
    x2 = pos[1][0]
    y2 = pos[1][1]
    d = abs(x2 - x1)
    region = source[(int)(y1 - d * 0.75):y2, x1:x2]
    # save the image
    cv2.imwrite("the_mouth.jpg", region)

def detect_mouth(img, pos):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    detector = dlib.get_frontal_face_detector()
    # use the predictor　
    predictor = dlib.shape_predictor('./dist/shape_predictor_68_face_landmarks.dat')
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for a in dets:
        cv2.rectangle(img, (a.left(), a.top()), (a.right(), a.bottom()), (255, 0, 0))
    # point_list=[]#save the mouth point to point_list[]#
    # Extract 68 feature points of the face and crop the lip image#
    for index, face in enumerate(dets):
        shape = predictor(gray, face)
        for i, pt in enumerate(shape.parts()):
            # print('Part {}: {}'.format(i, pt))
            # print(i)
            pt_pos = (pt.x, pt.y)
            if i >= 48 and i <= 67:
                cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
            if i >= 56 and i <= 58:
                # print(pt_pos)
                pos[i - 56][0] = pt.x
                pos[i - 56][1] = pt.y
            # cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
    return img

def detectPicture(Filepath):
    img = cv2.imread(Filepath)
    # copy the input image for the later crop
    img_clone = np.copy(img)
    # cv2.imwrite('source.jpg', img_clone)
    # save the lip position to pos array#
    pos = np.zeros((3, 2), dtype=int)
    result = detect_mouth(img, pos)
    cv2.imwrite("the_face.jpg", result)
    # crop the lip areas#
    source = cv2.imread(Filepath)
    crop(source, pos)
