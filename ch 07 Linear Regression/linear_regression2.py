#-*- coding: utf-8 -*-
#그래프 출력
# linear_regression2.py

import numpy as np
import tensorflow as tf


data_file_name= 'simple_linear.txt' # 데이터 파일 이름을 변수에 입력한다.
xy=np.genfromtxt(data_file_name,dtype='float32') #파일의 데이터를 불러 들인다.

# x값과 y값을 불러 온다.
x_data = xy[: , 0] # 첫째 칼럼을 x_data로 저장
y_data = xy[: , 2] # 셋째 칼럼을 y_data로 저장


# 데이터를 담을 tensor 변수를 선언한다.
X = tf.placeholder("float32")
Y = tf.placeholder("float32")

# 첫 a값과 b값을 주었다. 다른 값을 주어도 괜찮다.
temp_a =0.5
temp_b =0.5

# a값과 b값을 tensor로 변수를 선언한다.
a = tf.Variable(temp_a)
b = tf.Variable(temp_b)
y = a * X + b

# cost를 정의한다.
cost = tf.reduce_mean(tf.square(y - Y))

# optimizer와 학습 정의
opt = tf.train.GradientDescentOptimizer(0.001)
do_train = opt.minimize(cost)

# session 초기화 정의
init = tf.global_variables_initializer()

# set graphic parameter
a_out = 0.1
b_out = 0.1

with tf.Session() as sess:
        sess.run(init)
        # loop 과정
        for i in range(0,5000):
            sess.run(do_train, feed_dict={X: x_data, Y: y_data})
            # loggging part
            if (i % 100 ==0):
                cost_out = sess.run(cost, feed_dict={X:x_data, Y:y_data})
                a_out = sess.run(a, feed_dict={X:x_data, Y:y_data})
                b_out = sess.run(b, feed_dict={X:x_data, Y:y_data})
                print (i, "session is performed.. cost is ", cost_out, ", a is ", a_out,", b is ", b_out )


                
import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'ro', alpha= 0.01)

x_sample = np.linspace( np.amin(x_data)  , np.amax(x_data), 20)
y_sample = a_out * x_sample + b_out

plt.plot(x_sample, y_sample, '*', label="x_sample")
plt.legend()
plt.show()
