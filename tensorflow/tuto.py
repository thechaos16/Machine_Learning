from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.python.platform
import tensorflow as tf
import input_data as ind
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
        tTry = 1000
        for i in range(tTry):
        	batch_xs, batch_ys = self.data.train.next_batch(100)
        	train_step.run({x:batch_xs,y_:batch_ys})
        #	sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
        
        # Test trained model
        correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(accuracy.eval({x: self.data.test.images, y_: self.data.test.labels}))

if __name__=='__main__':
    TensorflowExample('./MNIST_data').regression_model()
