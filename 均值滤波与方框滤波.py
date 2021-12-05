import cv2

if __name__ == '__main__':
    # 显示出带有椒盐的图片
    img = cv2.imread('img\lenaNoise.png')
    cv2.imshow('lenaNoise.png', img)
    cv2.waitKey(0)
    # 采用均值滤波 约等于 简单的平均卷积操作
    # 对图片的像素点矩阵进行一个平均卷积，卷积核为（3,3）===》[[1,1,1,1,1,1,1,1,1]] 与像素矩阵求内积
    blur = cv2.blur(img, (3, 3))
    cv2.imshow('blur', blur)
    cv2.waitKey(0)

    # 方框滤波，基本与均值滤波一样，只是多了一个可以选择归一化的参数
    # -1表示得到的结果与原始输入颜色通道数在颜色通道上是一致的，normalize 归一化开关，TRUE是做归一化，FALSE不做归一化越界取255
    box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
    cv2.imshow('box', box)
    cv2.waitKey(0)
    box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
    cv2.imshow('box2', box2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
