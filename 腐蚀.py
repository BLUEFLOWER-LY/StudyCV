import cv2
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    origin_img = cv2.imread('img/dige.png')  # 原图
    cv_show('origin_img', origin_img)
    # 腐蚀的核，越大腐蚀程度越大
    kernel = np.ones((5, 5), np.uint8)
    # 迭代次数越多，腐蚀程度越大
    erosion = cv2.erode(origin_img, kernel, iterations=1)
    cv_show('erosion', erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 对圆的不同腐蚀
    origin_img = cv2.imread('img/pie.png')  # 原图
    kernel = np.ones((30, 30), np.uint8)
    cv_show('origin_img', origin_img)
    erosion1 = cv2.erode(origin_img, kernel, iterations=1)
    erosion2 = cv2.erode(origin_img, kernel, iterations=2)
    erosion3 = cv2.erode(origin_img, kernel, iterations=3)
    res = np.hstack([erosion1, erosion2, erosion3])
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
