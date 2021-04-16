# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time : 2021/4/14 21:59
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : morphologyEx.py
# @Software: PyCharm

import cv2
import os
import numpy as np


if __name__ == "__main__":
    # 处理后的文件保存路径
    save_path = "G:\\MyProjects\\python\\Breakout-Identification\\morphologyEX"
    threshold_value = '196'
    # 读取要处理的图片
    os.chdir("process_pictures\\true\\%s" % threshold_value)
    # 生成图片计数
    p_number = 0
    # 遍历当前路径图片
    for p_path in os.listdir(os.getcwd()):
        if p_path.find('png') != -1:
            p_number += 1
            # 待处理图片的全路径
            full_path = os.path.join(os.getcwd(), p_path)
            # 保存处理后图片的全路径
            path = os.path.join(save_path, p_path)
            img = cv2.imread(full_path, cv2.IMREAD_UNCHANGED)
            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
            # 形态学开运算
            r = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
            # 保存图片
            if cv2.imwrite(path, r):
                print("形态学开运算处理图片生成+1")
    with open(os.path.join(save_path, '说明.txt'), 'w') as f:
        f.write("处理图片的阈值为%s" % threshold_value)
    print("共生成图片%s张" % p_number)