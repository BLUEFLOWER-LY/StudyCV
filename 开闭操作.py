import cv2
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 开闭操作就是腐蚀膨胀的连用

if __name__ == '__main__':
    origin_img = cv2.imread('img/dige.png')  # 原图
    cv_show('origin_img', origin_img)
    kernel = np.ones((5, 5), np.uint8)
    # 开操作 先腐蚀在膨胀
    opening = cv2.morphologyEx(origin_img, cv2.MORPH_OPEN, kernel)
    cv_show('opening', opening)
    # 闭操作，先膨胀再腐蚀
    closing = cv2.morphologyEx(origin_img, cv2.MORPH_CLOSE, kernel)
    cv_show('closing', closing)
