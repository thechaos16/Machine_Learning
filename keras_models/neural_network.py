# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop


class NeuralNetwork:
    def __init__(self, feature_list_or_size, output_list_or_size, hidden_layer=3,
                 number_of_nodes=50, loss_function='mse', learning_rate=0.01,
                 optimizer=RMSprop):
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
        self.optimizer = optimizer
        self._initialize_model()

    def _initialize_model(self):
        self.model = Sequential()
        self.model.add(Dense(self.number_of_nodes, input_dim=self.feature_size, activation='sigmoid'))
        for layer_idx in range(self.hidden_layer):
            self.model.add(Dense(self.number_of_nodes, activation='sigmoid', init='uniform'))
        self.model.add(Dense(self.output_size, activation='linear'))
        self.model.compile(loss=self.loss_function, optimizer=self.optimizer(lr=self.learning_rate))

    def fit(self, input_matrix, output_matrix=None, **kwargs):
        if type(input_matrix) == pd.DataFrame and output_matrix is None:
            if self.targets is None or self.features is None:
                raise KeyError("You must set feature and target first!")
            output_matrix = input_matrix[self.targets].as_matrix()
            input_matrix = input_matrix[self.features].as_matrix()

        data_length = len(output_matrix)
        # initialize parameters
        if "epochs" in kwargs:
            epochs = kwargs["epochs"]
        else:
            epochs = 10
        if "batch_size" in kwargs:
            batch_size = kwargs["batch_size"]
            batch_size = np.min(batch_size, data_length)
        else:
            batch_size = data_length-1
        self.model.fit(x=input_matrix, y=output_matrix,
                       batch_size=batch_size, epochs=epochs)

    def predict(self, test_data):
        return self.model.predict(test_data[self.features].as_matrix())


if __name__ == "__main__":
    sample_frame =  pd.DataFrame({'aaa':np.random.random(1000), 'bbb':np.random.random(1000)})
    sample_frame['ccc'] = (sample_frame['aaa'] > 0.5).astype(int)
    nn_instance = NeuralNetwork(['aaa', 'bbb'], ['ccc'])
    nn_instance.fit(sample_frame)
