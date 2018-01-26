#-*- coding: utf-8 -*-
# make_data2.py
import numpy as np
import matplotlib.pyplot as plt


# 변수 선언과정
xy = []
n_count = 1999
a = 3
b = 4
mean, std = 20, 3 # mean and standard deviation

temp_x = np.random.normal(mean, std, n_count)
temp_b = np.random.normal(0,3, n_count)

# 반복해서 자료 만들기
for i, x  in enumerate(temp_x):
    y = a*x + b + temp_b[i]
    new_row = [x,y]
    xy.append(new_row)


# 그래프로 그리기     
xy = np.array(xy)
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 1] # 둘째 칼럼을 y_data로 저장
plt.plot(x_data, y_data, 'bo', alpha= 0.3 )
plt.show()
