#-*- coding: utf-8 -*-
# my_convolutional.py
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


#prepare input layer
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])




# reshape image
x_image = tf.reshape(x, [-1,28,28,1])

# set my parameter
num_1 = 8
num_2 = 16
num_3 = 512


#prepare 1st set of weight and bias
W_conv1 = tf.Variable(tf.truncated_normal([5,5,1,num_1], stddev=0.1))
b_conv1 = tf.Variable(tf.constant(0.1, shape= [num_1]))

# get first operation
h_conv1 = tf.nn.relu(tf.nn.conv2d(x_image, W_conv1,strides=[1, 1, 1, 1], padding='SAME') + b_conv1)

# shrink image by 2X2
h_pool1 =  tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# prepare 2nd set of weight and bias
W_conv2 = tf.Variable(tf.truncated_normal([5,5,num_1,num_2], stddev=0.1))
b_conv2 =tf.Variable(tf.constant(0.1, shape= [num_2]))

# get second operation
h_conv2 = tf.nn.relu(tf.nn.conv2d(h_pool1, W_conv2,strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# prepare 3rd set of weights and bias
W_fc1 = tf.Variable(tf.truncated_normal([7*7*num_2,num_3], stddev=0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape= [num_3]))

# reshape for 3rd operation
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*num_2])

# get 3rd operation
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# prepare drop out
keep_prob = tf.placeholder(tf.float32)

# get drop out
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

#prepare  4th set of weights and bias
W_fc2 = tf.Variable(tf.truncated_normal([num_3,10], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape= [10]))

# get 4th operation
y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)


# define cost
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1]))
# define training step
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# define evaluation scheme
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# session start 
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())


# start training
for i in range(20000):
  batch = mnist.train.next_batch(50)
  # get accuracy of test set
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))
