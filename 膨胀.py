import cv2
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    origin_img = cv2.imread('img/dige.png')  # 原图
    # 先腐蚀把毛刺去掉，但会把图像变细
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(origin_img, kernel, iterations=1)
    cv_show('erosion', erosion)
    # 通过膨胀操作把图像变粗 (腐蚀膨胀互为逆运算)
    dilate = cv2.dilate(erosion, kernel, iterations=1)
    cv_show('dilate', dilate)
    cv2.destroyAllWindows()

    # 对圆的不同膨胀
    origin_img = cv2.imread('img/pie.png')  # 原图
    kernel = np.ones((30, 30), np.uint8)
    cv_show('origin_img', origin_img)
    erosion1 = cv2.dilate(origin_img, kernel, iterations=1)
    erosion2 = cv2.dilate(origin_img, kernel, iterations=2)
    erosion3 = cv2.dilate(origin_img, kernel, iterations=3)
    res = np.hstack([erosion1, erosion2, erosion3])
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
