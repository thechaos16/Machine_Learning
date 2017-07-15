# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Activation, MaxPooling2D, AveragePooling2D, Flatten
from keras.optimizers import RMSprop
from keras.constraints import non_neg
from keras.layers.advanced_activations import PReLU
from keras.layers.normalization import BatchNormalization
from keras_models.neural_network import NeuralNetwork


class ConvolutionalNeuralNetwork(NeuralNetwork):
    def __init__(self, feature_list_or_size, output_list_or_size, hidden_layer=3,
                 number_of_nodes=50, loss_function='categorical_crossentropy', learning_rate=0.01,
                 optimizer=RMSprop, activation='relu', bias_term=non_neg, batch_normalization=False):
        # TODO: add batch size, padding, kernel size, pooling strategy (and size), dropout
        # TODO: add data_augmentation feature (maybe in train)
        self.batch_size = 32
        self.kernel_size = 3
        self.padding = 'same'
        self.pooling = MaxPooling2D
        self.pooling_size = 2
        self.dropout = False
        self.dropout_ratio = 0.25
        super.init(feature_list_or_size, output_list_or_size, hidden_layer, number_of_nodes, loss_function,
                   learning_rate, optimizer, activation, bias_term, batch_normalization)

    def _initialize_model(self):
        # override to add convolutional layers
        # input layer
        self.model.add(Conv2D(self.batch_size, (self.kernel_size, self.kernel_size), padding=self.padding,
                              input_shape=self.feature_size))
        if self.batch_normalization:
            self.model.add(BatchNormalization())
        self.model.add(Activation(self.activation))
        self.model.add(self.pooling(pool_size=(self.pooling_size, self.pooling_size)))
        if self.dropout:
            self.model.add(Dropout(self.dropout_ratio))
        # hidden layers
        for layer_num in range(self.hidden_layer):
            self.model.add(Conv2D())
        # output layer (normally it is classifier)
        self.model.add(Dense())
        self.model.add(Activation('softmax'))  # FIXME: should it be set by user?
        self.model.compile(loss=self.loss_function, optimizer=self.optimizer(lr=self.learning_rate))

    def fit(self, input_image, **kwargs):
        pass

    def predict(self, test_image):
        pass


if __name__ == "__main__":
    # TODO: use either MNIST or CIFAR for example (should be small)
    pass
