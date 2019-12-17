import numpy as np
import cv2
import argparse
import preprocessor_basic
import hough
import detect_edge
import blurring_smoothing


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = "path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args['image'])

print('''Option:
1. Resize
2. Histogram Equalization
3. Blurring
4. Hough
5. detect
''')
num_ = int(input("Nhap vao lua chon cua ban: "))
if num_ > 5:
    num_ = int(input("Nhap vao lua chon cua ban: "))

if num_ == 1:
    print("Nhap vao kich thuoc ban muon thay doi: ")
    width = int(input("Width:"))
    height = int(input("height:"))
    preprocessor_basic.resize(img, width, height)

elif num_ == 2:
    preprocessor_basic.histogramEqualization(img)

elif num_ == 3:
    print('''Ban muon Blurring theo phuong phap:
    1. Avarage
    2. Gaussian
    3. Median
    4. Bilateral ''')
    num = int(input("Chon: "))
    kernel = int(input("Kernel:"))
    if kernel % 2 == 0:
        kernel = int(input("Kernel:"))
    if num > 4:
        num = int(input("Chon: "))
    if num == 1:
        method = "Avarage"
        blurring_smoothing.blurring(img, method, kernel)
    elif num == 2:
        method = "Gaussian"
        blurring_smoothing.blurring(img, method, kernel)
    elif num == 3:
        method = "Median"
        blurring_smoothing.blurring(img, method, kernel)
    else:
        method = "Bilateral"
        blurring_smoothing.blurring(img, method, kernel)
elif num_ == 4:
    print('''Opion:
    1. Lines
    2. Circles''')
    num = int(input("Nhap vao lua chon cua ban:"))
    if num > 2:
        num = int(input("Nhap vao lua chon cua ban:"))
    if num == 1:
        method = "Lines"
        hough.hough(img, method)
    else:
        method = "Circles"
        hough.hough(img, method)
else:
    print('''Options:
    1. Sobel
    2. Candy''')
    num = int(input("Nhap vao lua chon cua ban: "))
    if num > 2:
        num = int(input("Nhap vao lua chon cau ban: "))
    if num == 1:
        print('''Options:
        1. Sobel_X
        2. Sobel_Y
        3. Sobel''')
        luachon = int(input("Nhap vao phuong thuc sobel ban muon su dung:"))
        k = int(input("Nhap vao gia tri cua Kernel :"))
        if k % 2 == 0:
            k = int(int("Nhap vao gia tri cua Kernel :"))

        if luachon > 3:
            luachon = int(input("Nhap vao phuong thuc sobel ban muon su dung:"))

        if luachon == 1:
            method = "Sobel_X"
            detect_edge.detectEdge(img, method, k)
        elif luachon == 2:
            method = "Sobel_Y"
            detect_edge.detectEdge(img, method, k)
        else:
            method = "Sobel"
            detect_edge.detectEdge(img, method, k)
    else:
        detect_edge.candy(img)
print("Da xu ly xong yeu cau cua ban")
