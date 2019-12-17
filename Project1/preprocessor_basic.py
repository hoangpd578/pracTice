'''Sẽ bao gồm các hàm xử lý, resize ảnh, sử dụng histogram để tăng độ tương phản của ảnh '''

import cv2
import numpy as np
import matplotlib.pyplot as plt

def resize(img, width = None, height = None, inter = cv2.INTER_AREA):
    (w, h) = img.shape[:2]
    dim = None
    if width is None and height is None:
        pass
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))
    img_resize = cv2.resize(img, dim, interpolation = inter)
    cv2.imshow('img', img)

    cv2.imshow('resize', img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def histogramEqualization(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalization = cv2.equalizeHist(img)
    cv2.imshow('img', img)
    cv2.imshow('equalization', equalization)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
