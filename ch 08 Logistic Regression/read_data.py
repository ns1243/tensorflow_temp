#-*- coding: utf-8 -*-
# read_data.py
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# download or read data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# 자료를 읽어서 변수에 저장하기 
train_x_data_all = mnist.train.images
train_y_data_all = mnist.train.labels

# 자료 구조 확인하기 
print ("train_x_data shape is ", np.shape(train_x_data_all), ", train_y_data shape is", np.shape(train_y_data_all))

# 자료 변형하기 
temp_x = np.reshape(train_x_data_all, (55000, 28, 28))
view_1st_digit= temp_x[0]

# 첫째 글자 확인하기 
view_1st_digit_label= train_y_data_all[0]
print ("temp_x[0] label is", view_1st_digit_label)

# 둘째 글자 확인하기 
view_2nd_digit= temp_x[1]
view_2nd_digit_label= train_y_data_all[1]
print ("temp_x[1] label is", view_2nd_digit_label)

