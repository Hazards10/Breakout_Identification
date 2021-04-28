# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time : 2021/4/11 11:36
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : matplotlib.py
# @Software: PyCharm
import os
import cv2


if __name__ == "__main__":
    # 处理后的文件保存路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\select"
    threshold_value = '235'
    # 读取要处理的图片
    os.chdir("original-img\\true")
    print(os.getcwd())
    img = cv2.imread("48.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", img)
    cv2.imshow("gray", gray)
    ret, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
    # 用椭圆矩阵保存特征
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    print(kernel)
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    thresh = cv2.erode(thresh, kernel)
    thresh = cv2.dilate(thresh, kernel)
    mask = cv2.merge([thresh, thresh, thresh])
    re_img = cv2.bitwise_or(img, mask)
    cv2.imshow('mask', thresh)
    g = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    cv2.imshow("g", g)
    cv2.imshow("re-img", re_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
