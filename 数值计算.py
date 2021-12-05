import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('img/xiong.jpg')
    img2 = cv2.imread('img/songshu.jpg')
    # 打印前五行
    print(img[:5, :, 0])
    # 把图片的每个像素的亮度加十
    img += 10
    # 打印前五行
    print(img[:5, :, 0])
    print('--------------------分割-------------------------')
    print('---------------------img------------------------')
    print(img[:5, :, 0])
    print('---------------------img2------------------------')
    print(img2[:5, :, 0])
    # 会有亮度越界，这种加法会保留越界的值（-256）
    print('---------------------img1+img2------------------------')
    print((img + img2)[:5, :, 0])
    print('---------------------cv2.add(img1+img2)------------------------')
    # 加到255的就保留255，否则为原值
    print(cv2.add(img, img2))
