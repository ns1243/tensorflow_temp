#-*- coding: utf-8 -*-
# chap10
#k_means.py

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from random import choice, shuffle



data_file_name= 'label_dots.txt' # 데이터 파일 이름을 변수에 입력한다.
xy=np.genfromtxt(data_file_name,dtype='float32') #파일의 데이터를 불러 들인다.

#shuffle(xy)

# x값과 y값을 불러 온다.
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 1] # 둘째 칼럼을 y_data로 저장

plt.plot(x_data, y_data, 'ro', alpha = 0.3)
plt.legend()
plt.show()
