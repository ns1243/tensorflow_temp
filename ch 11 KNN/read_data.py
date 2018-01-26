#-*- coding: utf-8 -*-
#read_data.py
import numpy as np
#read training sets
data_file_string= 'label_dots.txt'
xy=np.genfromtxt(data_file_string,dtype='str')
float_xy = xy.astype(np.float) # 문자형 자료를 숫자 실수형으로 변환한다.
#read test sets
data_file_string_test= 'test_dots.txt'
xy_test=np.genfromtxt(data_file_string_test,dtype='str')
float_xy_test = xy_test.astype(np.float) 
# data 
x_data = float_xy[:,0] # 첫째 칼럼을 x_data로 저장
y_data = float_xy[:,1]
x_data_test = float_xy_test[:, 0]
y_data_test =float_xy_test[:, 1]

import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'ro', label='label_dots ',alpha=0.3)
plt.plot(x_data_test, y_data_test, 'b^', label ="test_dots")
plt.legend()
plt.show()
