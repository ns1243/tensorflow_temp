#-*- coding: utf-8 -*-
# KNN_dots.py
import numpy as np
import tensorflow as tf
from random import shuffle

data_file_name= 'label_dots.txt' # 학습용 데이터 파일 이름을 변수에 입력
xy=np.genfromtxt(data_file_name,dtype='float32') #파일의 데이터를 불러 들인다.

data_file_name2= 'test_dots.txt' # 테스트 데이터 파일 이름을 변수에 입력
xy2=np.genfromtxt(data_file_name2,dtype='float32') #파일의 데이터를 불러 들인다.


number_of_test = 20
count = len(xy2)
indices = list(range(count))
shuffle(indices)

# x값과 y값을 불러 온다.
x_data = xy[: , 0:2] # 첫째 둘째 칼럼을 x_data로 저장
y_data = xy[: , 2:5]

x_data2 = xy2[:, 0:2]
y_data2 = xy2[:, 2:5]

x_train = tf.constant(x_data)
y_train = tf.constant(y_data)

#Broadcasting과 거리 구하기
x_test = tf.placeholder(tf.float32,[2])
reshape_x_train = tf.reshape(x_train,[1,-1,2])
reshape_x_test = tf.reshape(x_test, [1,-1,2])
tf_sub = tf.subtract(reshape_x_train,reshape_x_test)

#거리 구하기
distances_array =  tf.reduce_sum(tf.square(tf_sub),2)
assignments = tf.arg_min(distances_array,1)

# ========================================================  2부

sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)

correct_prediction = 0

# 테스트 진행
for step in range(number_of_test):
    index = indices[step]
    feed = {x_test: x_data2[index]}
    distances_out = sess.run(distances_array, feed_dict=feed)
    assignments_out = sess.run(assignments, feed_dict=feed)
    guess = y_data[assignments_out]
    y = y_data2[index]
    t_sub_out, x_test_out, x_train_out = sess.run([tf_sub,x_test, x_train], feed_dict=feed)

    a = 1
    if (np.argmax(y,0) == np.argmax(guess,1)):
        correct_prediction = correct_prediction + 1
#결과 출력
print ("test ended")
print ("correct prediction rate is ", 100* correct_prediction/number_of_test)
