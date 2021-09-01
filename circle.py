import cv2 as cv
import numpy as np
from scipy.spatial.distance import pdist, squareform
import math

# 是否开始画图
drawing = False
start = (-1, -1)

area = []


def mouse_event(event, x, y, flags, param):
    global start, drawing
    # 左键按下：开始画图
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 鼠标移动，画图
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x, y), 2, (0, 0, 255), -1)
            area.append([x, y])
    # 左键释放：结束画图
    elif event == cv.EVENT_LBUTTONUP:

        cv.circle(img, (x, y), 2, (0, 0, 255), -1)
        drawing = False


img = np.zeros((512, 512, 3), np.uint8)

cv.namedWindow('image')
cv.setMouseCallback('image', mouse_event)

while True:
    cv.imshow('image', img)
    # 按ESC键退出程序

    if cv.waitKey(1) == 27:
        ans = 0

        ans = cv.contourArea(np.array(area))
        radia = squareform(pdist(area)).max() / 2

        circle_area = 3.14 * (radia ** 2)

        score = (ans / circle_area) * 100
        print(f"画圆的得分是:{math.floor(score)}")
        break

