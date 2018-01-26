#-*- coding: utf-8 -*-
#기존 그래프가 출력되지 않습니다.

import numpy as np
import tensorflow as tf


data_file_name= 'simple_linear.txt' # 데이터 파일 이름을 변수에 입력한다.
xy=np.genfromtxt(data_file_name,dtype='float32') #파일의 데이터를 불러 들인다.

# x값과 y값을 불러 온다.
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 2] # 셋째 칼럼을 y_data로 저장


# 데이터를 담을 tensor 변수를 선언한다.
#X = tf.placeholder("float32")
#Y = tf.placeholder("float32")

# 데이터를 담을 tensor 변수를 선언한다.
X = tf.placeholder("float32", name="X")
Y = tf.placeholder("float32", name="Y")
# 첫 a값과 b값을 주었다. 다른 값을 주어도 괜찮다.
temp_a =0.5
temp_b =0.5

# a값과 b값을 tensor로 변수를 선언한다.
#a = tf.Variable(temp_a)
#b = tf.Variable(temp_b)
#y = a * X + b
#cost = tf.reduce_mean(tf.square(y - Y))
# cost를 정의한다.


# a값과 b값을 tensor로 변수를 선언한다.
with tf.name_scope ("a_value"):
    a = tf.Variable(temp_a, name="temp_a")

with tf.name_scope ("b_value"):
    b = tf.Variable(temp_b, name="temp_b")

with tf.name_scope ("Main_function"):
    y = a * X + b

with tf.name_scope("get_cost"):
    cost = tf.reduce_mean(tf.square(y - Y))


# optimizer를 정의한다.
opt = tf.train.GradientDescentOptimizer(0.001)

# session에 이용한 train 정의
do_train = opt.minimize(cost)
init = tf.global_variables_initializer()

with tf.Session() as sess:
        sess.run(init)
        for i in range(0,5000):
            sess.run(do_train, feed_dict={X: x_data, Y: y_data})
            if (i % 100 ==0):
                cost_out = sess.run(cost, feed_dict={X:x_data, Y:y_data})
                a_out = sess.run(a, feed_dict={X:x_data, Y:y_data})
                b_out = sess.run(b, feed_dict={X:x_data, Y:y_data})
                print (i, "session is performed.. cost is ", cost_out, ", a is ", a_out,", b is ", b_out )


writer = tf.summary.FileWriter('./graphs', graph=tf.get_default_graph())
writer.close()


#import os
#os.system('tensorboard --logdir=graphs')