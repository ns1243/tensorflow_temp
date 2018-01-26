#-*- coding: utf-8 -*-
# read_data2.py

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


data_file_name= 'linear_random.txt' # 데이터 파일 이름을 변수에 입력한다.
#data_file_name= 'x_square.txt'
xy=np.genfromtxt(data_file_name,dtype='float32') #파일의 데이터를 불러 들인다.


# x값과 y값을 불러 온다.
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 1] # 둘째 칼럼을 y_data로 저장

plt.plot(x_data, y_data, 'bo', alpha= 0.3 )
plt.show()






