# -*- coding: utf-8 -*-
# helper.py
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
temp_matmul = tf.matmul(X, a)
temp_y = temp_matmul + b
y = tf.nn.softmax(temp_y)
guess = tf.argmax(y, 1)

# cost 정의
Y_log_y = Y * tf.log(y)
temp_cost = -tf.reduce_sum(Y_log_y, reduction_indices=[1])
cost = tf.reduce_mean(temp_cost)
do_train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)

# session 정의
sess = tf.InteractiveSession()
init = tf.global_variables_initializer()
sess.run(init)

# 학습 실행
for i in range(1):
    x_data, y_data = mnist.train.next_batch(5)

    # 학습하기
    sess.run(do_train, feed_dict={X: x_data, Y: y_data})

    # a값, b값 확인하기
    a_out = sess.run(a, feed_dict={X: x_data})
    b_out = sess.run(b, feed_dict={X: x_data})

    # y값 확인하기
    temp_matmul_out = sess.run(temp_matmul, feed_dict={X: x_data})
    temp_y_out = sess.run(temp_y, feed_dict={X: x_data})
    y_out = sess.run(y, feed_dict={X: x_data})
    guess_out = sess.run(guess, feed_dict={X: x_data})

    # cross entropy, cost 확인하기
    Y_log_y_out = sess.run(Y_log_y, feed_dict={X: x_data, Y: y_data})
    temp_cost_out = sess.run(temp_cost, feed_dict={X: x_data, Y: y_data})
    cost_out = sess.run(cost, feed_dict={X: x_data, Y: y_data})

    # 결과 출력하기
    print("guess of the image ==> ", guess_out)


