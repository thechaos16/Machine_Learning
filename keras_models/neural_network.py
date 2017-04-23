# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop


class NeuralNetwork:
    def __init__(self, feature_list, output_list, hidden_layer=3, number_of_nodes=50):
        self.features = feature_list
        self.feature_size = len(feature_list)
        self.targets = output_list
        self.output_size = len(output_list)
        self.number_of_nodes = number_of_nodes
        self.hidden_layer = hidden_layer
        self._initialize_model()

    def _initialize_model(self):
        self.model = Sequential()
        self.model.add(Dense(self.number_of_nodes, input_dim=self.feature_size, activation='sigmoid'))
        for layer_idx in range(self.hidden_layer):
            self.model.add(Dense(self.number_of_nodes, activation='sigmoid', init='uniform'))
        self.model.add(Dense(self.output_size, activation='softmax'))
        self.model.compile(loss='mse', optimizer=RMSprop())

    def fit(self, input_data, **kwargs):
        """
        
        :param input_data: Dataframe currently, including feature list and output list in beginning
        :param kwargs: 
        :return: 
        """

        data_length = len(input_data)
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
        print(batch_size)
        print(input_data[self.features])
        self.model.fit(x=input_data[self.features], y=input_data[self.targets], batch_size=batch_size, epochs=epochs)

    def predict(self, test_data):
        return self.model.predict(test_data)


if __name__ == "__main__":
    pass
