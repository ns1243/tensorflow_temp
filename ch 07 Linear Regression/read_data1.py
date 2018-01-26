#-*- coding: utf-8 -*-


import numpy as np

import tensorflow as tf

data_file_string= 'simple_linear.txt'
xy=np.genfromtxt(data_file_string,dtype='str')
float_xy = xy.astype(np.float) # 문자형 자료를 숫자 실수형으로 변환한다.

print (np.shape(float_xy))

x_data = float_xy[:,0] # 첫째 칼럼을 x_data로 저장
y_data = float_xy[:,2] # 셋째 칼럼을 y_data로 저장

import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'o', label='made from exel ')
plt.legend()
plt.show()
