from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.python.platform
import tensorflow as tf
import input_data as ind
import numpy as np

## read input
mnist = ind.read_data_sets('./MNIST_data',one_hot=True)

## tensorflow
x = tf.placeholder('float',[None,len(mnist.train.images[0])])

## regression parameters
LabelNum = len(mnist.train.labels[0])
#LabelNum = 10
# weight
W = tf.Variable(tf.zeros([len(mnist.train.images[0]),LabelNum]))
# regularization
b = tf.Variable(tf.zeros([LabelNum]))

## regression model (softmax)
y = tf.nn.softmax(tf.matmul(x,W)+b)

## training
y_ = tf.placeholder('float',[None,LabelNum])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

## run
# initialize
init = tf.initialize_all_variables()
# launch session
sess = tf.InteractiveSession()
#sess = tf.Session()
init.run()

## train
tTry = 1000
for i in range(tTry):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	train_step.run({x:batch_xs,y_:batch_ys})
#	sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})

# Test trained model
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))
