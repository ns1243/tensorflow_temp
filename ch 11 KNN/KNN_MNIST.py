#-*- coding: utf-8 -*-
# KNN_MNIST.py

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from random import choice, shuffle
from tensorflow.examples.tutorials.mnist import input_data



mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


x_data2 = mnist.test.images
y_data2 = mnist.test.labels

x_data, y_data = mnist.train.next_batch(55000)


number_of_test = 100
count = len(x_data2)
indices = list(range(count))
shuffle(indices)


x_train = tf.constant(x_data)
y_train = tf.constant(y_data)

# 자료 shape 변환
x_test = tf.placeholder(tf.float32,[784])

reshape_x_train = tf.reshape(x_train,[1,-1,784])
reshape_x_test = tf.reshape(x_test, [1,1,-1])
tf_sub = tf.subtract(reshape_x_train,x_test)

distances_array =  tf.sqrt(tf.reduce_sum(tf.square(tf_sub),2))
assignments = tf.arg_min(distances_array,1)

# ========================================================  2부
sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)

correct_prediction = 0
false_prediction = 0


for step in range(number_of_test):
    index = indices[step]
    feed = {x_test: x_data2[index]}
    distances_out = sess.run(distances_array, feed_dict=feed)
    assignments_out = sess.run(assignments, feed_dict=feed)
    guess = y_data[assignments_out]
    y = y_data2[index]
    t_sub_out, x_test_out, x_train_out = sess.run([tf_sub,x_test, x_train], feed_dict=feed)


    if(np.argmax(y,0) == np.argmax(guess,1)):
        correct_prediction = correct_prediction + 1
    else:
        false_prediction = false_prediction +1

    accuracy = 100 * correct_prediction/number_of_test
print ("test ended")
print ("correct prediction rate is ", accuracy, " %")

