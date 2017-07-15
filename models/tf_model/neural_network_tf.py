# -*- coding: utf-8 -*-

import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.python.training.adam import AdamOptimizer


class NeuralNetworkTensorFlow:
    def __init__(self, feature_list_or_size, output_list_or_size, hidden_layer=3,
                 number_of_nodes=50, loss_function='mse', learning_rate=0.01, optimizer=AdamOptimizer,
                 activation=tf.nn.relu):
        if type(feature_list_or_size) is list:
            self.features = feature_list_or_size
            self.feature_size = len(feature_list_or_size)
        else:
            self.feature_size = feature_list_or_size
            self.features = None
        if type(output_list_or_size) is list:
            self.targets = output_list_or_size
            self.output_size = len(output_list_or_size)
        else:
            self.output_size = output_list_or_size
            self.targets = None
        self.number_of_nodes = number_of_nodes
        self.hidden_layer = hidden_layer
        self.loss_function = loss_function
        self.learning_rate = learning_rate
        self.activation = activation
        self.optimizer = optimizer
        self.model = self._initialize_model()

    def _initialize_model(self):
        all_layers = []
        # input layer
        input_shape = [self.number_of_nodes, self.feature_size]
        print(input_shape)
        bias_val = 0.1  # FIXME: set value of bias from input parameter
        self.input_placeholder = tf.placeholder('float', [self.feature_size, None])
        weight = tf.placeholder('float', input_shape)
        bias = tf.Variable(tf.constant(bias_val, shape=[self.feature_size]))
        input_layer = self.activation(tf.matmul(weight, self.input_placeholder) + bias)
        all_layers.append(input_layer)
        # hidden layers
        for layer_num in range(self.hidden_layer):
            shape = [self.number_of_nodes, self.number_of_nodes]
            # set space for weight and bias
            weight = tf.placeholder('float', shape)
            bias = tf.Variable(tf.constant(bias_val, shape=[self.number_of_nodes]))
            hidden_layer = self.activation(tf.add(tf.matmul(weight, all_layers[layer_num]), bias))
            all_layers.append(hidden_layer)
        # output layer
        shape = [self.patch_size, self.patch_size, self.number_of_nodes, self.output_size]
        # set space for weight and bias
        weight = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
        bias = tf.Variable(tf.constant(bias_val, shape=[self.output_size]))
        output_layer = self.activation(tf.matmul(all_layers[-1] * weight) + bias)
        all_layers.append(output_layer)
        return all_layers  # NOTE: probably only output layer is valuable to return

    def train(self, input_matrix, output_matrix, **kwargs):
        # if data is structured
        if type(input_matrix) == pd.DataFrame and output_matrix is None:
            if self.targets is None or self.features is None:
                raise KeyError("You must set feature and target first!")
            output_matrix = input_matrix[self.targets].as_matrix()
            input_matrix = input_matrix[self.features].as_matrix()

        # check if data size is correct
        assert self.feature_size == input_matrix.shape[1]
        assert self.output_size == output_matrix.shape[1]

        # output placeholder
        y_out = tf.placeholder(float, [None, self.output_size])
        # loss function
        if self.loss_function == 'mse':
            loss = tf.sqrt(tf.reduce_mean(tf.square(tf.sub(y_out, self.model[-1]))))
        else:
            raise NotImplementedError()
        # optimizer
        train_opt = self.optimizer().minimize(loss)
        sess = tf.InteractiveSession()
        sess.run(tf.initialize_all_variables())
        # run train
        train_opt.run(feed_dict={self.input_placeholder: input_matrix,
                                 y_out: output_matrix})  # FIXME: refactor to use mini-batch

    def predict(self, input_data):
        y_pred = tf.placeholder(float, [None, self.output_size])
        sess = tf.InteractiveSession()
        sess.run(tf.initialize_all_variables())


if __name__ == "__main__":
    data_size = 100
    sample_frame = pd.DataFrame({'aaa': np.random.random(data_size), 'bbb': np.random.random(data_size)})
    sample_frame['ccc'] = (sample_frame['aaa'] > 0.5).astype(int)
    nn_instance = NeuralNetworkTensorFlow(['aaa', 'bbb'], ['ccc'])
    # nn_instance.fit(sample_frame)
    # predicted = nn_instance.predict(sample_frame)
    from evaluation.error_based import mse, mae
    # print(mse(predicted.ravel(), np.array(sample_frame['ccc'])))
