import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


top, bottom, left, right = (50, 50, 50, 50)
img = cv2.imread('img/xiong.jpg')
if __name__ == '__main__':
    # 复制法，复制最边缘的像素
    REPLICATE = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_REPLICATE)
    cv_show('REPLICATE', REPLICATE)
    # 反射法，对图像的像素在两边进行复制，fedcba|abcdefgh|hgfedcb
    REFLECT = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_REFLECT)
    cv_show('REFLECT', REFLECT)
    # 反射法，以最边缘的像素为轴对称，gfedcba|abcdefgh|gfedcba
    REFLECT101 = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_REFLECT_101)
    cv_show('REFLECT101', REFLECT101)
    # 外包装法，cdefgh|abcdefgh|abcdefg
    WARP = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_WRAP)
    cv_show('WARP', WARP)
    # 常量法，用常数进行填充
    CONSTANT = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=0)
    cv_show('CONSTANT', CONSTANT)
