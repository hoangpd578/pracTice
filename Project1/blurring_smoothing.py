import cv2
import numpy as np

def blurring(img, method, kernel = 3):
    image = None
    if method == "Avarage":
        image = cv2.blur(img, ksize = (kernel, kernel))
    elif method == "Gaussian":
        image = cv2.GaussianBlur(img, (kernel, kernel), 1)
    elif method == "Median":
        image = cv2.medianBlur(img, kernel)
    if method == "Bilateral":
        image = cv2.bilateralFilter(img, 9, 75, 75)

    cv2.imshow('img', img)
    cv2.imshow('blurring', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
