import cv2

if __name__ == '__main__':
    # 显示出带有椒盐的图片
    img = cv2.imread('img\lenaNoise.png')
    cv2.imshow('lenaNoise.png', img)
    cv2.waitKey(0)
    # 采用高斯滤波
    # 高斯滤波--有一个权重矩阵，对一个像素点进行卷积，距离这个像素点越近权重越大，得到一个新的值。
    # 高斯模糊里的卷积核是数值，满足高斯分布，卷积核越大越模糊，(sigma = 1 方向的方差，用来控制权重，更重视中间的)
    aussian = cv2.GaussianBlur(img, (3, 3), 1)
    cv2.imshow('aussian', aussian)
    cv2.waitKey(0)
    # 把卷积矩阵从大到小排列，选出中位数，用中值代替
    median = cv2.medianBlur(img, 5)
    cv2.imshow('median', median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
