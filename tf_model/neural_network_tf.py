# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.python.training.adam import AdamOptimizer


class NeuralNetworkTensorFlow:
    def __init__(self, feature_list_or_size, output_list_or_size, hidden_layer=3,
                 number_of_nodes=50, loss_function='mse', learning_rate=0.01, optimizer=AdamOptimizer,
                 activation=tf.nn.relu, patch_size=5):
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
        self.patch_size = patch_size  # Note: why patch size is needed?
        self.model = self._initialize_model()

    def _initialize_model(self):
        all_layers = []
        # input layer
        input_shape = [self.patch_size, self.patch_size, 1, self.feature_size]
        bias_val = 0.1  # FIXME: set value of bias from input parameter
        input_placeholder = tf.placeholder('float', [None, self.feature_size])
        weight = tf.Variable(tf.truncated_normal(input_shape, stddev=0.1))
        bias = tf.Variable(tf.constant(bias_val, shape=[self.feature_size]))
        input_layer = self.activation(tf.matmul(input_placeholder, weight) + bias)
        all_layers.append(input_layer)
        # hidden layers
        for layer_num in range(self.hidden_layer):
            if layer_num == 0:
                input_size = self.feature_size
            else:
                input_size = self.number_of_nodes
            shape = [self.patch_size, self.patch_size, input_size, self.number_of_nodes]
            # set space for weight and bias
            weight = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
            bias = tf.Variable(tf.constant(bias_val, shape=[self.number_of_nodes]))
            hidden_layer = self.activation(tf.matmul(all_layers[layer_num], weight) + bias)
            all_layers.append(hidden_layer)
        # output layer
        shape = [self.patch_size, self.patch_size, self.number_of_nodes, self.output_size]
        # set space for weight and bias
        weight = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
        bias = tf.Variable(tf.constant(bias_val, shape=[self.output_size]))
        output_layer = self.activation(tf.matmul(all_layers[-1] * weight) + bias)
        all_layers.append(output_layer)
        return all_layers

    def train(self, input_data, **kwargs):
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

    def predict(self, input_data):
        pass


if __name__ == "__main__":
    pass
