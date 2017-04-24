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
        self.model.add(Dense(self.output_size, activation='linear'))
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
        self.model.fit(x=input_data[self.features].as_matrix(), y=input_data[self.targets].as_matrix(),
                       batch_size=batch_size, epochs=epochs)

    def predict(self, test_data):
        return self.model.predict(test_data[self.features].as_matrix())


if __name__ == "__main__":
    sample_frame =  pd.DataFrame({'aaa':np.random.random(1000), 'bbb':np.random.random(1000)})
    sample_frame['ccc'] = (sample_frame['aaa'] > 0.5).astype(int)
    nn_instance = NeuralNetwork(['aaa', 'bbb'], ['ccc'])
    nn_instance.fit(sample_frame)
