import cv2
import numpy as np


def detectEdge(img, method, k):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = None
    if method == "Sobel_X":
        image =  cv2.Sobel(img, ddepth = cv2.CV_64F, dx = 1, dy = 0, ksize=k)

    elif  method == "Sobel_Y":
        image = cv2.Sobel(img, ddepth = cv2.CV_64F, dx = 0, dy = 1, ksize= k)

    elif method == "Laplacian":
        image = cv2.Laplacian(img, ddepth = cv2.CV_64F, ksize = 5)

    elif method == "Sobel":
        sobel_x = cv2.Sobel(img, ddept = cv2.CV_64F, dx = 0, dy = 1, ksize = k)
        sobel_y = cv2.Sobel(img, ddept = cv2.CV_64F, dx = 1, dy = 0, ksize = k)
        image =  cv2.bitwise_or(sobel_x, sobel_y)

    cv2.imshow('img', img)
    cv2.imshow('detect', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def candy(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(img, (5, 5), 1)

    canny = cv2.Canny(image, 30, 150)

    cv2.imshow("img", img)
    cv2.imshow('canny', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
