# -*- coding: utf-8 -*-
# @Time : 2021/1/31 13:51
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : main.py
# @Software: PyCharm
import os
import cv2
import numpy as np


# 读取图像，解决imread不能读取中文图像的问题
def cv_imread(file_path=""):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img


def binary_processing(f_path, s_path, value):
    """
    二值处理图像，并保存图像
    :param f_path: 待处理的图像的路径
    :param s_path: 图像要保存的路径
    :return:
    """
    image = cv2.imread(f_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    thresh = cv2.erode(thresh, kernel)
    thresh = cv2.dilate(thresh, kernel)
    mask = cv2.merge([thresh, thresh, thresh])
    re_img = cv2.bitwise_or(image, mask)
    # print(image.shape)
    # 保存处理后的图像
    if cv2.imwrite(s_path, re_img):
        print("二值处理图片生成+1")


def otsu_binary_processing(f_path, s_path):
    """
    Otsu处理图像，但图像必须是单通道
    :param f_path: 待处理的图像的路径
    :param s_path: 图像要保存的路径
    :return:
    """
    # 图片处理为单通道灰度图片，再读取
    image = cv2.imread(f_path, cv2.IMREAD_GRAYSCALE)
    t, rst = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # 保存处理后的图像
    if cv2.imwrite(s_path, rst):
        print("Otsu处理图片生成+1")


def adaptive_binary_processing(f_path, s_path, athd):
    """
    :param f_path: 图像处理的路径
    :param s_path: 图像处理后保存路径
    :param athd: 邻域像素的处理方式
    :return:
    """
    image = cv2.imread(f_path, 0)
    if athd == "MEAN":
        # 邻域所有像素点的权重值是一致的
        athd_data = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
    elif athd == "GAUS":
        # 邻域各个像素点到中心点的距离有关，通过高斯方程得到各个点的权重值
        athd_data = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
        # 保存处理后的图像
    if cv2.imwrite(s_path, athd_data):
        print("自适应处理athdMEAN 图片生成+1")


def covert_3(f_path, s_path):
    image = cv2.imread(f_path, cv2.IMREAD_COLOR)
    if cv2.imwrite(s_path, image):
        print("转3通道，处理图片生成+1")


def show_red(f_path, s_path):
    """
    显示红色的ROI，并保存
    :param f_path: 待处理的图像路径
    :param s_path: 保存的图像路径
    :return:
    """
    image = cv2.imread(full_path)
    # 转换为HSV色彩控件
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 指定红色范围
    minRed = np.array([0, 50, 50])
    maxRed = np.array([30, 255, 255])
    # 确定红色区域
    mask = cv2.inRange(hsv, minRed, maxRed)
    # 通过掩码控制的按位与运算，锁定红色区域
    red = cv2.bitwise_and(image, image, mask=mask)
    if cv2.imwrite(s_path, red):
        print("显示红色ROI，图片生成+1")


if __name__ == "__main__":
    print("*****************************")
    print("当前路径为%s" % os.getcwd())
    # 待处理的图像路径
    process_path = "original-img/true"
    # 图像处理后保存的路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\select"
    os.chdir("select/")
    # 处理的图像计数
    p_number = 0
    # 256个灰度值，分别试一试
    for g_value in range(256):
        # 遍历处理全部图片
        os.mkdir(str(g_value))
        print("创建文件后的路径：%s" % os.getcwd())
        # 到文件处理路径
        os.chdir(os.pardir)
        os.chdir(process_path)
        print("*****************************")
        print("当前处理图片的路径为%s" % os.getcwd())
        # 处理60例图片
        for p_path in os.listdir(os.getcwd()):
            if p_path.find('png') != -1:
                p_number += 1
                # 待处理图片的全路径
                full_path = os.path.join(os.getcwd(), p_path)
                # 保存处理后图片的全路径
                path = os.path.join(save_path+'/'+str(g_value), p_path)
                # 图片处理并保存
                binary_processing(full_path, path, g_value)
        print("共生成图片%s张" % p_number)
        # 转换到处理图片路径
        os.chdir(os.pardir)
        os.chdir(os.pardir)
        print(os.getcwd())
        os.chdir("select")
        print("一个灰度值生成后，当前路径为%s" % os.getcwd())








