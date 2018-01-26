#-*- coding: utf-8 -*-
# make_data4.py
import numpy as np
import matplotlib.pyplot as plt

#변수 선언하기
xy = []
n_count = 300

#첫번째 군집 만들기 
temp_x = np.random.normal(3, 1, n_count)
temp_y = np.random.normal(3, 1, n_count)
for i in range(n_count):
    x = temp_x[i]
    y = temp_y[i]
    new_row = [x, y, 1, 0, 0]
    xy.append(new_row)

#두번째 군집 만들기 
temp_x = np.random.normal(6, 1, n_count)
temp_y = np.random.normal(6, 1, n_count)
for i in range(n_count):
    x = temp_x[i]
    y = temp_y[i]
    new_row = [x, y, 0, 1, 0]
    xy.append(new_row)

# 세번째 군집 만들기     
temp_x = np.random.normal(1, 1, n_count)
temp_y = np.random.normal(7, 1, n_count)
for i in range(n_count):
    x = temp_x[i]
    y = temp_y[i]
    new_row = [x, y, 0, 0, 1]
    xy.append(new_row)


# 그래프로 그리기     
xy = np.array(xy)
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 1] # 둘째 칼럼을 y_data로 저장
plt.plot(x_data, y_data, 'bo', alpha= 0.3 )
plt.show()




