import cv2
import matplotlib.pyplot as plt


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('img/songshu.jpg', cv2.IMREAD_GRAYSCALE)
    cv_show('img',img)
    # src 输入图 dst 输出图 thresh 阈值 maxval 不等于阈值的情况所赋的值 type 二值化的类型
    # ret ,dst  = cv2.thresholed(src,thresh,maxval,type)
    #
    ret, dst1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, dst2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, dst3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, dst4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, dst5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, dst1, dst2, dst3, dst4, dst5]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
