# -*- coding: utf-8 -*-
# @Time : 2021/3/17 19:53
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : main.py
# @Software: PyCharm

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    path = os.getcwd()
    os.chdir("division/true")
    print(os.getcwd())
    o = cv2.imread(os.path.join(os.getcwd(), '11.png'))
    cv2.imshow("original", o)
    gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("binary", binary)
    retval, labels = cv2.connectedComponents(binary)
    print(retval)
    print(labels)
    # labels = np.uint8(labels)
    # cv2.imshow("labels", labels)

    # 构造颜色
    colors = []
    for i in range(retval):
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))
    colors[0] = (0, 0, 0)
    # 画出连通图
    h, w = gray.shape
    image = np.zeros((h, w, 3), dtype=np.uint8)
    for row in range(h):
        for col in range(w):
            image[row, col] = colors[labels[row, col]]
    cv2.imshow("colored labels", image)

    # contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(t_o, contours, -1, (0, 0, 255), 5)
    # n = len(contours)
    # contoursImg = []
    # max_area = 0
    # max_i = 0
    # print(o.shape)
    # for i in range(n):
    #     temp = np.zeros(o.shape, np.uint8)
    #     contoursImg.append(temp)
    #     contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), -1)
    #     if cv2.contourArea(contours[i]) > max_area:
    #         max_area = cv2.contourArea(contours[i])
    #         max_i = i

    # plt.figure("图像分割")
    # plt.subplot(111)
    # plt.imshow(o), plt.axis('off')
    # plt.subplot(132)
    # plt.imshow(binary), plt.axis('off')
    # plt.subplot(133)
    # plt.imshow(contoursImg[max_i]), plt.axis('off')
    # plt.show()
    # cv2.imshow("contours[" + str(max_i) + "]", contoursImg[max_i])

    cv2.waitKey()
    cv2.destroyAllWindows()

