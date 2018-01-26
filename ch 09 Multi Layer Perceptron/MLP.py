#-*- coding: utf-8 -*-
#MLP.py
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#자료를 불러옵니다.
data_file_name = 'x_square.txt'  
xy = np.genfromtxt(data_file_name, dtype='float32') 

# x값과 y값을 불러와서 임시로 저장한다
temp_x =  xy[:, 0]  # 첫째 칼럼을 x_temp로 저장
temp_y =  xy[:, 1]  # 둘째 칼럼을 y_temp로 저장

# reshape data
x_data = np.reshape(temp_x, [1,-1])
y_data = np.reshape(temp_y, [1,-1])

# setup input layer
x = tf.placeholder(dtype=tf.float32, shape=[1,None])
y = tf.placeholder(dtype=tf.float32, shape=[1,None])

number_of_hidden = 10

# setup hidden layer
a_hidden = tf.Variable(tf.random_normal([number_of_hidden, 1]))
b_hidden = tf.Variable(tf.random_normal([number_of_hidden, 1]))
layer1_out = tf.nn.sigmoid(tf.matmul(a_hidden, x ) + b_hidden)

# setup output layer
a_out = tf.Variable(tf.random_normal([1,number_of_hidden]))
b_out = tf.Variable(tf.random_normal([1,1]))
y_out = tf.matmul(a_out,layer1_out) + b_out

# setup cost
cost = tf.nn.l2_loss(y_out-y)

# setup optimizer
optimizer= tf.train.AdamOptimizer(0.1)
do_train = optimizer.minimize(cost)


init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  for i in range(5000):
    sess.run(do_train,feed_dict={x: x_data, y: y_data})
  # generate test data
  x_temp =  np.linspace(0, 20, 50)
  x_test = [x_temp]
  y_test = sess.run(y_out,feed_dict={x: x_test})

# 그래프 그리기
plt.plot(x_data,y_data,'ro',alpha=0.05)
plt.plot(x_test,y_test,'b^',alpha=1)
plt.show()

