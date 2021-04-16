# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time : 2021/3/17 18:43
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : smooth.py
# @Software: PyCharm

import os
import cv2
import numpy as np


def blur_processing(f_path, s_path):
    """
    均值滤波处理
    :param f_path:待处理的图像路径
    :param s_path:保存的图像路径
    :return:
    """
    image = cv2.imread(f_path, -1)
    r = cv2.blur(image, (5, 5))
    # 保存处理后的图像
    if cv2.imwrite(s_path, r):
        print("均值处理图片生成+1")


def box_filter_processing(f_path, s_path):
    """
    方框滤波处理
    :param f_path: 待处理的图像路径
    :param s_path: 保存的图像路径
    :return:
    """
    image = cv2.imread(f_path, -1)
    r = cv2.boxFilter(image, -1, (5, 5), normalize=0)
    # 保存处理后的图像
    if cv2.imwrite(s_path, r):
        print("方框滤波处理图片生成+1")


def gaussian_blur_processing(f_path, s_path):
    """
    高斯滤波处理
    :param f_path: 待处理的图像
    :param s_path: 保存的图像
    :return:
    """
    image = cv2.imread(f_path, -1)
    r = cv2.GaussianBlur(image, (5, 5), 0, 0)
    # 保存处理后的图像
    if cv2.imwrite(s_path, r):
        print("高斯滤波处理图片生成+1")


if __name__ == "__main__":
    print("*****************************")
    print("当前路径为%s" % os.getcwd())
    # 待处理的图像路径
    process_path = "original-img/false"
    # 图像处理后保存的路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\smooth\\gaus-blur-false"
    # 改变当前路径
    os.chdir(process_path)
    print("*****************************")
    print("当前路径为%s" % os.getcwd())
    # 处理的图像计数
    p_number = 0
    # 遍历处理全部图片
    for p_path in os.listdir(os.getcwd()):
        if p_path.find('png') != -1:
            p_number += 1
            full_path = os.path.join(os.getcwd(), p_path)
            path = os.path.join(save_path, p_path)
            # 图片处理并保存
            # blur_processing(full_path, path)
            # box_filter_processing(full_path, path)
            gaussian_blur_processing(full_path, path)
    print("共生成图片%s张" % p_number)
