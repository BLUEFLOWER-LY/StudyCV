import cv2
# 读取出来的通道格式是BGR


# 定义一个函数用来显示图像 并且创建一个窗口 按任意键关闭窗口
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # img = cv2.imread('xiong.jpg')  # 默认彩色模式，数据为BGR格式
    img = cv2.imread('img/xiong.jpg', cv2.IMREAD_GRAYSCALE)  # 灰度图模式
    cv_show('我的头像', img)
    # 图片的H W C 高 宽 通道(灰度图没有通道值)
    print(img.shape)
    # 图片的像素点个数
    print(img.size)
    # 数据类型
    print(img.dtype)



