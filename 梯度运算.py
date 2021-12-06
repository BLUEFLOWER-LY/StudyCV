import cv2
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 梯度运算约等于 膨胀-腐蚀=轮廓 (有异议)

if __name__ == '__main__':
    origin_img = cv2.imread('img/pie.png')  # 原图
    cv_show('origin_img', origin_img)
    kernel = np.ones((7, 7), np.uint8)
    gradient = cv2.morphologyEx(origin_img, cv2.MORPH_GRADIENT, kernel)
    cv_show('gradient', gradient)