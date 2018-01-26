#-*- coding: utf-8 -*-
# chap10
#k_means.py

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from random import choice, shuffle



data_file_name= 'label_dots.txt' # 데이터 파일 이름을 변수에 입력한다.
xy=np.genfromtxt(data_file_name,dtype='float32') #파일의 데이터를 불러 들인다.


# x값과 y값을 불러 온다.
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 1] # 둘째 칼럼을 y_data로 저장


number_of_cluster = 3
count = len(xy)

#
centroid_x = []
centroid_y = []

# 자료 뒤섞기
indices = list(range(len(xy)))
shuffle(indices)

# 첫 centroid 지정하기
for i in range(0,number_of_cluster):
    centroid_x.append(x_data[indices[i]])
    centroid_y.append(y_data[indices[i]])


# 입력 텐서 설정하기
x_points = tf.constant(x_data)
y_points = tf.constant(y_data)

# centroid 입력하기
centroid_x_point = tf.placeholder(tf.float32,[number_of_cluster,])
centroid_y_point = tf.placeholder(tf.float32,[number_of_cluster,])


# reshape tensors 
reshape_x_points = tf.reshape(x_points, [1, -1])
reshape_y_points = tf.reshape(y_points, [1, -1])

reshape_centroid_x_points = tf.reshape(centroid_x_point, [-1,1])
reshape_centroid_y_points = tf.reshape(centroid_y_point, [-1,1])

# cetroid로부터의 거리 구하기 
tf_sub_x = tf.subtract(reshape_x_points,reshape_centroid_x_points)
tf_sub_y = tf.subtract(reshape_y_points, reshape_centroid_y_points)

distances_array =  tf.square(tf_sub_x) +tf.square(tf_sub_y)

# 최단거리 정하기 
assignments = tf.arg_min(distances_array,0)
# ========================================================  2부

# session 정의하기 
sess = tf.Session()
init_op = tf.initialize_all_variables()
sess.run(init_op)

# Sorting and regrouping
for step in range(100):
    sorted_clusters_x = []
    sorted_clusters_y = []
    # 점들을 모을 리스트 새로 선언하기 
    for i in range(0, number_of_cluster):
        sorted_clusters_x.append([])
        sorted_clusters_y.append([])
        
     # 최근접 점들의 index 구하기
    feed_dic = {centroid_x_point:centroid_x,centroid_y_point:centroid_y}
    assignments_out = sess.run(assignments,feed_dict=feed_dic)
    
    # 리스트에 점들을 모으기 
    for i in range(0, count):
        add_index = assignments_out[i]
        sorted_clusters_x[add_index].append(x_data[i])
        sorted_clusters_y[add_index].append(y_data[i])
    # 새 centroid 구하기 (점좌표들의 평균)
    for i in range(0, number_of_cluster):
        centroid_x[i] = np.mean(sorted_clusters_x[i])
        centroid_y[i] = np.mean(sorted_clusters_y[i])
    print (step, "th finished, centroid x ",centroid_x)

# 그래프로 확인하기     
color = ['ro', 'b^', 'gs','c*','mv','y<','k>','rh','bd','g^','cP','mX','y*','k^']
for i in range (number_of_cluster):
    plt.plot(sorted_clusters_x[i], sorted_clusters_y[i], color[i], alpha = 0.4)
plt.show()
print ("program ended")
