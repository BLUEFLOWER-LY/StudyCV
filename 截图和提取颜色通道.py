import cv2

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('img/ly.jpg')
    cutImg = img[0:200][0:200]
    cv_show('my', cutImg)
    # 单独提取颜色通道
    b, g, r = cv2.split(img)
    colorImg = cv2.merge((b, g, r))
    # 对颜色通道进行显示
    # 0  1  2
    # B  G  R
    imgR = colorImg.copy()
    # 保留R通道，把BG通道清零
    imgR[:, :, 0] = 0
    imgR[:, :, 1] = 0
    cv_show('R', imgR)
    # 保留G通道，把RB通道清零
    imgG = colorImg.copy()
    imgG[:, :, 0] = 0
    imgG[:, :, 2] = 0
    cv_show('G', imgG)
    # 保留G通道，把RB通道清零
    imgB = colorImg.copy()
    imgB[:, :, 1] = 0
    imgB[:, :, 2] = 0
    cv_show('B', imgB)
