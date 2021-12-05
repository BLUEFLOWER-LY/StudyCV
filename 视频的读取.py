import cv2

if __name__ == '__main__':
    vc = cv2.VideoCapture('video.mp4')
    if vc.isOpened():  # 是否正确打开视频
        open, frame = vc.read()
    else:
        open = False
    while open:  # 遍历视频里的每一帧，如果有处理为灰度图然后显示，等待N秒后进行下一帧，可以按Esc退出
        ret, frame = vc.read()
        if frame is None:
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)
            if cv2.waitKey(10) & 0xFF == 27:
                break
    vc.release()
    cv2.destroyAllWindows()
