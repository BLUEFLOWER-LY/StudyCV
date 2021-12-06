import cv2
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 礼帽 = 原始输入 - 开运算 (eg：带刺的 - 不带刺的 = 刺)
# 黑帽 = 闭运算 - 原始输入

if __name__ == '__main__':
    origin_img = cv2.imread('img/dige.png')  # 原图
    cv_show('origin_img', origin_img)
    kernel = np.ones((3, 3), np.uint8)
    tophat = cv2.morphologyEx(origin_img, cv2.MORPH_TOPHAT, kernel)
    cv_show('tophat', tophat)
    blackhat = cv2.morphologyEx(origin_img, cv2.MORPH_BLACKHAT, kernel)
    cv_show('blackhat', blackhat)
