#-*- coding: utf-8 -*-
#logistic_regression.py
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# 입력층 정의 
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])

# 가중치 a와 편차 b 정의하기 
a = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


# 모델 정의  
temp_y = tf.matmul(X,a) + b
y = tf.nn.softmax(temp_y)
guess = tf.argmax(y, 1)

# cost 정의
Y_log_y = Y * tf.log(y)
temp_cost = -tf.reduce_sum(Y_log_y, reduction_indices=[1])
cost = tf.reduce_mean(temp_cost)
do_train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
sess = tf.InteractiveSession()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
  x_data, y_data = mnist.train.next_batch(100)
  sess.run(do_train, feed_dict={X: x_data, Y: y_data})
  #cost를 기록한다.
  print (i,"th step finished.. cost is", sess.run(cost, feed_dict={X: x_data, Y: y_data}))
  # 데이터 검증 test set으로 정확도를 평가 한다.
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(Y, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  print( "accuracy is", sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))


