#예제 1
import tensorflow as tf
a = tf.constant([ [1 , 2], [2 , 3] ])
b = tf.constant([ [1 , 2], [2 , 3] ])
add = tf.add(a , b)
sub = tf.subtract(a , b)
# session 정의 
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
# 실제 연산 
add_out = sess.run(add)
sub_out = sess.run(sub)
print(add_out)
print(sub_out)


#예제 2
import tensorflow as tf
a = tf.constant([ [1 , 2], [3 , 4] ])
b = tf.constant([ [1 , 2], [3 , 4] ])
y1 = tf.multiply(a , b)
y2 = tf.matmul(a , b)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y1_out = sess.run(y1)
y2_out = sess.run(y2)
print(y1_out)
print(y2_out)


#예제 3
import tensorflow as tf
a = tf.constant([ [1 , 2], [3 , 4] ])
b = tf.constant([ [1 , 1], [1 , 1] ])
y = tf.div(a , b)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y_out = sess.run(y)
print(y_out)


#예제 4
import tensorflow as tf

data = [[1],[2],[3],[4]]
print ("input data type is", type(data))
a = tf.placeholder(dtype=tf.float32,shape=[None,1])

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
a_out = sess.run(a,feed_dict={a:data})

print ("output type is", type( a_out))

#예제 5

import numpy as np
a = [ [1 , 2], [3 , 4] ]
b = [ [1 , 2], [3 , 4] ]
c = (1,2,3,4)
d = (2,3,4,5)
y1 = np.multiply(a , b)
y2 = np.matmul(a , b)
print(y1)
print(y2)



#예제 6
import tensorflow as tf

data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
a = tf.placeholder(dtype=tf.float32,shape=[None,None])
b  =tf.Variable([0,1,2],dtype=tf.float32)
y = tf.add(a,b)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y_out = sess.run(y,feed_dict={a:data})
print (y_out)



#예제 7
import tensorflow as tf

data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
a = tf.placeholder(dtype=tf.float32,shape=[None,3])
b  =tf.Variable([0,1,2,3],dtype=tf.float32)
y = tf.add(a,b)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y_out = sess.run(y,feed_dict={a:data})
print (y_out)


#예제 8
import tensorflow as tf

data = [[1],[2],[3],[4]]
a = tf.placeholder(dtype=tf.float32,shape=[4,1])
b  =tf.Variable([0,1,2],dtype=tf.float32)
y = tf.add(a,b)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y_out = sess.run(y,feed_dict={a:data})
print (y_out)




# 예제 9
a = np.arange(6)
print ("first \n",a)
a = np.reshape(a, [2,3])
print ("second \n",a)
a = np.reshape(a, [3,2])
print ("third \n",a)


#예제 10
import tensorflow as tf
data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
a = tf.placeholder(dtype=tf.float32,shape=[None,3])
b  =tf.Variable([0,1,2,4],dtype=tf.float32)
b  = tf.reshape(b, [-1, 1])
y = tf.add(a,b)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y_out = sess.run(y,feed_dict={a:data})
print (y_out)

#예제 11
import tensorflow as tf

data = [1,2,3,4]
a = tf.placeholder(dtype=tf.float32)
y1 = tf.arg_max(a,0)
y2 = tf.arg_min(a,0)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y1_out = sess.run(y1,feed_dict={a:data})
y2_out = sess.run(y2,feed_dict={a:data})
print (y1_out, y2_out)


#예제 12
import tensorflow as tf

data = [[0,2,4], [6,8,10]]
a = tf.placeholder(dtype=tf.float32)
y1 = tf.arg_max(a,0)
y2 = tf.arg_min(a,1)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y1_out = sess.run(y1,feed_dict={a:data})
y2_out = sess.run(y2,feed_dict={a:data})
print (y1_out, y2_out)


#예제 13
import tensorflow as tf

data = [1,2,3,4]
a = tf.placeholder(dtype=tf.float32)
y1 = tf.reduce_sum(a,0)
y2 = tf.reduce_mean(a,0)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y1_out = sess.run(y1,feed_dict={a:data})
y2_out = sess.run(y2,feed_dict={a:data})
print (y1_out, y2_out)

#예제 14
import tensorflow as tf

data = [[0,2,4], [6,8,10]]
a = tf.placeholder(dtype=tf.float32)
y1 = tf.reduce_sum(a,0)
y2 = tf.reduce_mean(a,1)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
y1_out = sess.run(y1,feed_dict={a:data})
y2_out = sess.run(y2,feed_dict={a:data})
print (y1_out, y2_out)
