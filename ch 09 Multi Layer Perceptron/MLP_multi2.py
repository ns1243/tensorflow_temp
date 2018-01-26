#-*- coding: utf-8 -*-
#MLP_multi2.py
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#이전과 같이 파일에서 자료를 불러 들입니다.


data_file_name = 'x_square.txt'  # 데이터 파일 이름을 변수에 입력한다.
xy = np.genfromtxt(data_file_name, dtype='float32')  # 파일의 데이터를 불러 들인다.

# x값과 y값을 불러와서 임시로 저장한다
temp_x =  xy[:, 0]  # 첫째 칼럼을 x_temp로 저장
temp_y =  xy[:, 1]  # 둘째 칼럼을 y_temp로 저장

x_data = [temp_x ]
y_data = [temp_y ]

x = tf.placeholder(dtype=tf.float32, shape=[1,None])
y = tf.placeholder(dtype=tf.float32, shape=[1,None])

# setup variables
number_of_hidden = 1
number_of_out = 1


# setup hidden layer1
a_hidden = tf.Variable(tf.random_normal([number_of_hidden, 1]))
b_hidden = tf.Variable(tf.random_normal([number_of_hidden, 1]))
hidden_layer1 = tf.nn.sigmoid(tf.matmul(a_hidden, x ) + b_hidden)


# setup hidden layer2
a_middle = tf.Variable(tf.random_normal([number_of_out, number_of_hidden ]))
b_middle = tf.Variable(tf.random_normal([number_of_out,1]))
hidden_layer2 = tf.nn.sigmoid(tf.matmul(a_middle,hidden_layer1) + b_middle)

# setup output layer
a_out = tf.Variable(tf.random_normal([1,number_of_out]))
b_out = tf.Variable(tf.random_normal([1,1]))
y_out = tf.matmul(a_out,hidden_layer2) + b_out

cost = tf.nn.l2_loss(y_out-y)

opt= tf.train.AdamOptimizer(0.1)
do_train = opt.minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  for i in range(45000):
    sess.run(do_train,feed_dict={x: x_data, y: y_data})

  x_temp =  np.linspace(0, 20, 50)
  x_test = [x_temp]
  y_test = sess.run(y_out,feed_dict={x: x_test})
plt.plot(x_data,y_data,'ro',alpha = 0.05)
plt.plot( x_test,y_test,'b<', alpha = 1, label='test')
plt.show()

