# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time : 2021/4/11 14:51
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : batch_extraction.py
# @Software: PyCharm

import os
import cv2
import numpy as np


def process_picture(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event == cv2.EVENT_RBUTTONDOWN :
        print("单击了鼠标右键")
    elif flags == cv2.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")
    elif event == cv2.EVENT_MBUTTONDOWN :
        print("单击了中间键")


def picture_contours(o_img):
    """
    提取V字特征图像特征轮廓
    :param o_img: 要处理的图片
    :return: 全部的轮廓特征
    """
    # print("原图类型%s" % str(o_img.shape))
    gray = cv2.cvtColor(o_img, cv2.COLOR_BGRA2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("binary-img", binary)
    cts, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return cts


# def intercept_contour(p_contours, index, c_contours):
#     n = len(contours)
#     # 原图像大小相同的画布
#     contours_img = []
#     max_area = 0
#     max_i = 0
#     for i in range(n):
#         temp = np.zeros(o_img.shape, np.uint8)
#         contours_img.append(temp)
#         contours_img[i] = cv2.drawContours(contours_img[i], contours, i, (255, 255, 255), -1)
#         if cv2.contourArea(contours[i]) > max_area:
#             max_area = cv2.contourArea(contours[i])
#             max_i = i
#     # 获取最大轮廓的矩形边界值
#     x, y, w, h = cv2.boundingRect(contours[max_i])
#     # 画矩形
#     cv2.rectangle(o_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     # 取最小矩形轮廓
#     # rect = cv2.minAreaRect(contours[max_i])
#     # # 矩形四个角点取整
#     # box = np.int0(cv2.boxPoints(rect))
#     # cv2.drawContours(o, [box], 0, (0, 255, 0), 2)
#     # cv2.imshow("feature-img", contours_img[max_i])
#     cv2.imshow("finally-img", o_img)
#     # 截取图片并保存（截取面积最大的）
#     if cv2.imwrite(os.path.join(s_path, p_name), o_img[y:y + h, x:x + w]):
#         print("保存图像V特征%s", p_name)
#     print("最大轮廓面积%s" % max_area)


if __name__ == "__main__":
    # 要处理的图片路径
    process_path = "G:\\MyProjects\\python\\Breakout-Identification\\morphologyEX"
    # 要保存的图片路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\v_feature"
    os.chdir(process_path)
    print("当前路径%s" % os.getcwd())
    print("当前路径下的文件%s" % os.listdir(os.getcwd()))
    # 图片路径列表
    picture_path_list = os.listdir(os.getcwd())
    # 排除不是png图片的文件或文件夹
    picture_path_list = [picture_path_list[i] for i in range(0, len(picture_path_list))
                         if picture_path_list[i].find('png') != -1]
    # 图片个数
    picture_list_number = len(picture_path_list)
    # 图片路径列表的索引
    picture_path_index = 0
    # 轮廓索引
    c_index = 0
    # 当前轮廓索引
    n_index = 0
    # 原图像大小相同的画布
    contours_img = []
    # 实时显示的轮廓索引列表
    n_s_index_list = []
    # 要保存的轮廓图像矩阵
    save_temp = []
    while (1):
        # 图片索引超出时跳出循环
        if picture_path_index > picture_list_number-1:
            print("图片已经全部处理完")
            break
        # 读取图片
        img = cv2.imread(os.path.join(process_path, picture_path_list[picture_path_index]))
        # 图片文件名
        img_name = picture_path_list[picture_path_index]
        # 图片的全部轮廓
        contours = picture_contours(img)
        # 轮廓个数
        c_num = len(contours)
        # 等待键盘输入
        k_value = cv2.waitKey(1) & 0xFF
        # 显示原图
        cv2.imshow(img_name, img)
        # 实时显示要保存的特征图
        if n_s_index_list:
            # 将保存的轮廓放一块显示
            temp = np.zeros(img.shape, np.uint8)
            for i in  n_s_index_list:
                temp = cv2.drawContours(temp, contours, i, (255, 255, 255), -1)
            save_temp = temp
            cv2.imshow("save-contour", temp)
        else:
            cv2.imshow("save-contour", np.zeros(img.shape, np.uint8))
        # 实时显示单个轮廓图片
        if contours_img:
            cv2.imshow("single-contour", contours_img[n_index])
        else:
            cv2.imshow("single-contour", np.zeros(img.shape, np.uint8))
        # 读取后一张后一张
        if k_value == ord('d'):
            picture_path_index += 1
            c_index = 0
            contours_img.clear()
            n_s_index_list.clear()
            cv2.destroyAllWindows()
            print("后一张")
        # 保存图片V特征
        elif k_value == ord('s'):
            ret, binary = cv2.threshold(save_temp, 127, 255, cv2.THRESH_BINARY_INV)
            loc = cv2.bitwise_or(img, binary)
            if cv2.imwrite(os.path.join(save_path, img_name), loc):
                print("保存V字特征轮廓+1")
        # 查看一个轮廓的特征
        elif k_value == ord('n'):
            if c_index == c_num:
                print("已显示全部轮廓")
                c_index = 0
                contours_img.clear()
                n_s_index_list.clear()
                cv2.destroyAllWindows()
                continue
            temp = np.zeros(img.shape, np.uint8)
            contours_img.append(temp)
            cv2.drawContours(contours_img[c_index], contours, c_index, (255, 255, 255), -1)
            n_index = c_index
            c_index += 1
        # 记录要保存的轮廓索引
        elif k_value == ord('m'):
            # 添加保存轮廓的在contours的索引
            n_s_index_list.append(n_index)
            print("记录当前轮廓")
        # 按ESC退出
        elif k_value == 27:
            break
    cv2.destroyAllWindows()
