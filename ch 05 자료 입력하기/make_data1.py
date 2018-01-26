#-*- coding: utf-8 -*-
# make_data1.py
import numpy as np
import matplotlib.pyplot as plt

# 변수 선언과정
xy = []
n_count = 1999
x = 0.01
a = 3
b = 4

# 자료 만드는 과정 반복
for i in range(n_count):
    new_row = [x, a*x, a*x + b]
    xy.append(new_row)
    x = x + 0.01

# 그래프로 그리기     
xy = np.array(xy)
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 2] # 둘째 칼럼을 y_data로 저장
plt.plot(x_data, y_data, 'bo', alpha= 0.3 )
plt.show()


