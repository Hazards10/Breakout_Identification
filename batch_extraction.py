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


if __name__ == "__main__":
    # 要处理的图片路径
    process_path = "G:\\MyProjects\\python\\Breakout-Identification\\division\\true"
    # 要保存的图片路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\extract"
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
    while (1):
        # 图片索引超出时跳出循环
        if picture_path_index > picture_list_number-1:
            print("图片已经全部处理完")
            break
        # 读取图片
        img = cv2.imread(os.path.join(process_path, picture_path_list[picture_path_index]))
        # 图片文件名
        img_name = picture_path_list[picture_path_index]
        cv2.imshow(img_name, img)
        # 等待键盘输入
        k_value = cv2.waitKey(1) & 0xFF
        # print(k_value)
        # 读取前一张图片
        if k_value == ord('a'):
            picture_path_index += 1
            cv2.destroyWindow(img_name)
            print("前一张")
        # 读取后一张后一张
        elif k_value == ord('d'):
            picture_path_index -= 1
            cv2.destroyWindow(img_name)
            print("后一张")
        # 保存图片
        elif k_value == ord('s'):
            if cv2.imwrite(os.path.join(save_path, img_name), img):
                print("保存图片%s" % img_name)
        # 按ESC退出
        elif k_value == 27:
            break
    cv2.destroyAllWindows()
