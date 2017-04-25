from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.python.platform
import tensorflow as tf
import input_data as ind
import numpy as np
import os

class TensorflowWithGraph:
    def __init__(self, file_path, batch_size=1000):
        if not os.path.isdir(file_path):
            raise FileNotFoundError(file_path + ' does not exist!')
        self.data = self.__read_input(file_path)
        self.batch_size = batch_size
        # make empty structure
        self.images = tf.placeholder(tf.float32, shape=(self.batch_size, len(self.data.train.images[0])))
        self.labels = tf.placeholder(tf.float32, shape=(self.batch_size))
    
    def __read_input(self, file_path):
        mnist = ind.read_data_sets(file_path, one_hot=True)
        return mnist
        
    def graph_structure(self):
        pass


if __name__ == '__main__':
    aaa = TensorflowWithGraph('./MNIST_data')
