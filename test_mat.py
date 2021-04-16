# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Time : 2021/4/11 11:36
# @Author : 隋宇飞
# @Email : 799896781@qq.com
# @File : matplotlib.py
# @Software: PyCharm
import numpy as  np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    plt.plot(X, C)
    plt.plot(X, S)

    plt.show()