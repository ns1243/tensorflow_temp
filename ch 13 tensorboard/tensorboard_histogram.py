#-*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

data_file_name = 'x_square.txt'  # 데이터 파일 이름을 변수에 입력한다.
xy = np.genfromtxt(data_file_name, dtype='float32')  # 파일의 데이터를 불러 들인다.

# x값과 y값을 불러 온다.

x_data = np.zeros((len(xy),1))
y_data = np.zeros((len(xy),1))
x_data[:,0] = xy[:, 0]  # 첫째 칼럼을 x_data로 저장
y_data[:,0] = xy[:, 1]  # 둘째 칼럼을 y_data로 저장





x = tf.placeholder(dtype=tf.float32, shape=[None,1])
y = tf.placeholder(dtype=tf.float32, shape=[None,1])

number_of_hidden = 10
a_hidden = tf.Variable(tf.random_normal([1,number_of_hidden]))
b_hidden = tf.Variable(tf.random_normal([1,number_of_hidden]))

a_out = tf.Variable(tf.random_normal([number_of_hidden,1]))
b_out = tf.Variable(tf.random_normal([1,1]))

#추가되는 부분

with tf.name_scope('a_hidden_layer'):
  tf.summary.histogram('show_a_hidden', a_hidden)
with tf.name_scope('a_out_layer'):
  tf.summary.histogram('show_a_out', a_out)
#hidden_layer = tf.nn.tanh(tf.matmul(x, W) + b)

layer1 = tf.nn.sigmoid(tf.matmul(x, a_hidden) + b_hidden)
y_out = tf.matmul(layer1,a_out) + b_out


cost = tf.nn.l2_loss(y_out-y)

opt= tf.train.AdamOptimizer(0.1)
#train_op = tf.train.RMSPropOptimizer(learning_rate=0.1, decay=0.8).minimize(lossfunc)
do_train = opt.minimize(cost)

init = tf.global_variables_initializer()


#추가되는 부분
summary_op = tf.summary.merge_all()
writer = tf.summary.FileWriter('./histogram/ml', graph=tf.get_default_graph())


with tf.Session() as sess:
  sess.run(init)
  for i in range(5000):
    sess.run(do_train,feed_dict={x: x_data, y: y_data})
    # 추가되는 부분
    if (i % 1000 == 0):
      summary = sess.run(summary_op, feed_dict={x: x_data, y: y_data})
      writer.add_summary(summary, i)

  x_temp =  np.linspace(0, 20, 50)
  x_test = np.zeros((len(x_temp), 1))
  x_test[:, 0] = x_temp
  y_test = sess.run(y_out,feed_dict={x: x_test})
plt.plot(x_data,y_data,'ro', x_test,y_test,'bo',alpha=0.3)
plt.show()

# 맨 마지막에 추가    
writer.close()
