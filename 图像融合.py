import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('img/xiong.jpg')
    img2 = cv2.imread('img/songshu.jpg')
    print("两张图片的shape:")
    print(img.shape)
    print(img2.shape)
    print("变换大小后的shape")
    img = cv2.resize(img, (600, 600))
    img2 = cv2.resize(img2, (600, 600))
    print(img.shape)
    print(img2.shape)
    # 融合图片1，图片1权重，融合图片2，图片2权重，微调参数
    res = cv2.addWeighted(img, 0.4, img2, 0.6, 0)
    cv_show('addWeight',res)
