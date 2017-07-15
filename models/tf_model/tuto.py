from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.python.platform
import tensorflow as tf
from tf_model import input_data as ind
import numpy as np
import os


class TensorflowExample:
    def __init__(self, file_path):
        if not os.path.isdir(file_path):
            raise FileNotFoundError(file_path + ' does not exist!')
        self.data = self.__read_input(file_path)
        
    def __read_input(self, file_path):
        mnist = ind.read_data_sets(file_path, one_hot=True)
        return mnist
        
    def regression_model(self):
        x = tf.placeholder('float',[None, len(self.data.train.images[0])])
        label_num = len(self.data.train.labels[0])
        W = tf.Variable(tf.zeros([len(self.data.train.images[0]),label_num]))
        b = tf.Variable(tf.zeros([label_num]))
        y = tf.nn.softmax(tf.matmul(x,W)+b)
        
        # training
        y_ = tf.placeholder('float',[None,label_num])
        cross_entropy = -tf.reduce_sum(y_*tf.log(y))
        train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
        
        init = tf.initialize_all_variables()
        # launch session
        sess = tf.InteractiveSession()
        #sess = tf.Session()
        init.run()
                
        ## train
        number_of_try = 1000
        for i in range(number_of_try):
            batch_xs, batch_ys = self.data.train.next_batch(100)
            # train_step.run({x:batch_xs,y_:batch_ys})
            sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
        
        # Test trained model
        correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(accuracy.eval({x: self.data.test.images, y_: self.data.test.labels}))
        
    def convolutional_neural_network(self):
        x = tf.placeholder('float',[None, len(self.data.train.images[0])])
        label_num = len(self.data.train.labels[0])
        patch_size = 5
        # first layer
        number_of_features = 32
        one_line = int(np.sqrt(len(self.data.train.images[0])))
        W_conv1 = weight_variable([patch_size, patch_size, 1, number_of_features])
        b_conv1 = bias_variable([number_of_features])
        x_image = tf.reshape(x, [-1, one_line, one_line, 1])        
        h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
        h_pool1 = max_pool_2x2(h_conv1)
        
        # second layer
        second_features = 64
        W_conv2 = weight_variable([patch_size, patch_size, number_of_features, second_features])
        b_conv2 = bias_variable([second_features])
        h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
        h_pool2 = max_pool_2x2(h_conv2)
        
        # densely connected layer
        number_of_neurons = 1024
        W_fc1 = weight_variable([7 * 7 * second_features, number_of_neurons])
        b_fc1 = bias_variable([number_of_neurons])
        
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*second_features])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
        
        # dropout
        keep_prob = tf.placeholder(tf.float32)
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
        
        # readout layers
        W_fc2 = weight_variable([number_of_neurons, label_num])
        b_fc2 = bias_variable([label_num])
        y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
        
        # train and evaluate model
        y_ = tf.placeholder('float',[None,label_num])
        sess = tf.InteractiveSession()
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1]))
        train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        sess.run(tf.initialize_all_variables())
        for i in range(20000):
            batch = self.data.train.next_batch(50)
            if i%100 == 0:
              train_accuracy = accuracy.eval(feed_dict={x:batch[0], y_: batch[1], keep_prob: 1.0})
              print("step %d, training accuracy %g"%(i, train_accuracy))
            train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
        
        print("test accuracy %g"%accuracy.eval(feed_dict={x: self.data.test.images, y_: self.data.test.labels, keep_prob: 1.0}))

# some functions for neural network
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
    
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

if __name__=='__main__':
    aaa = TensorflowExample('./MNIST_data')
    aaa.convolutional_neural_network()
