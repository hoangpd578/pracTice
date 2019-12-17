import cv2
import numpy as np


def hough(img, method):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    if method == "Lines":
        image = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
    elif method == "Cricles":
        image = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT,1, 20, param1=50,param2=30, minRadius=0, maxRadius=80)
    cv2.imshow("img", img)
    cv2.imshow('houghLine', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
