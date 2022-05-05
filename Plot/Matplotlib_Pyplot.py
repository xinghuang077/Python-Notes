## !/usr/bin/env python
## -*- coding: utf-8 -*-
## Author: Xing Huang
## Email: xinghuang077@gmail.com
## Date: May 4th, 2022
## Affiliation: University of California, Santa Barbara
## Description:
## This notes is based on: https://matplotlib.org/3.5.0/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt
import numpy as np

# ##
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# ##
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

##
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()