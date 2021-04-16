# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time : 2021/4/16 16:21
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : feature_extraction.py
# @Software: PyCharm

import os
import cv2
import numpy as np

if __name__ == "__main__":
    # 要处理的图片路径
    process_path = "G:\\MyProjects\\python\\Breakout-Identification\\morphologyEX\\1.png"
    # 要保存的图片路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\extract"
    o = cv2.imread(process_path, cv2.IMREAD_UNCHANGED)
    cv2.imshow("original-img", o)
    print("原图类型%s" % str(o.shape))
    gray = cv2.cvtColor(o, cv2.COLOR_BGRA2GRAY)
    cv2.imshow("gray-img", gray)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("binary-img", binary)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    n = len(contours)
    # 原图像大小相同的画布
    contoursImg = []
    max_area = 0
    max_i = 0
    for i in range(n):
        temp = np.zeros(o.shape, np.uint8)
        contoursImg.append(temp)
        contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), -1)
        if cv2.contourArea(contours[i]) > max_area:
            max_area = cv2.contourArea(contours[i])
            max_i = i
    # 获取最大轮廓的矩形边界值
    x, y, w, h = cv2.boundingRect(contours[max_i])
    cv2.rectangle(o, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 取最小矩形轮廓
    # rect = cv2.minAreaRect(contours[max_i])
    # # 矩形四个角点取整
    # box = np.int0(cv2.boxPoints(rect))
    # cv2.drawContours(o, [box], 0, (0, 255, 0), 2)
    cv2.imshow("feature-img", contoursImg[max_i])
    cv2.imshow("finally-img", o)
    # print(x, y, w, h)
    # 截取图片并保存（截取面积最大的）
    cv2.imwrite(os.path.join(save_path, '1.png'), o[y:y+h, x:x+w])
    print("最大轮廓面积%s" % max_area)
    cv2.waitKey()
    cv2.destroyAllWindows()
