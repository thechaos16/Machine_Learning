from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.python.platform
import tensorflow as tf
import input_data as ind
import numpy as np

## regression
def weight_variable(shape):
	initial = tf.truncated_normal(shape,sttdev=0.1)
	return tf.Variable(initial)

def bias_variable(shape):
	initial = tf.constant(0.1,shape=shape)
	return tf.Variable(initial)

## convolution and pooling
def conv2d(x,W):
	return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding = 'SAME')
def max_pool_2x2(x):
	return tf.nn.max_pool(x,ksize[1,2,2,1],strides=[1,2,2,1],padding='SAME')

sess = tf.InteractiveSession()

x = tf.placeholder("float",shape=[None,784])
y_ = tf.placeholder("float",shape=[None,10])


