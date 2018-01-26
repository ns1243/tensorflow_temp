#-*- coding: utf-8 -*-
# make_data3.py
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#변수선언과정
xy = []
n_count = 1999
x = 0.01

# 자료 만드는 과정 반복
for i in range(n_count):
    y = math.pow(x-5, 2) + random.random()*5
    new_row = [x, y]
    xy.append(new_row)
    x = x + 0.01

    
# 그래프로 그리기     
xy = np.array(xy)
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 1] # 둘째 칼럼을 y_data로 저장
plt.plot(x_data, y_data, 'bo', alpha= 0.3 )
plt.show()


