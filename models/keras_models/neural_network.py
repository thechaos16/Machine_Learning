# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
from keras.constraints import non_neg
from keras.layers.advanced_activations import PReLU
from keras.layers.normalization import BatchNormalization


class NeuralNetwork:
    def __init__(self, feature_list_or_size, output_list_or_size, hidden_layer=3,
                 number_of_nodes=50, loss_function='mse', learning_rate=0.01,
                 optimizer=RMSprop, activation='relu', bias_term=non_neg, batch_normalization=False):
        """
        Initialize neural network with structure-related variables
        
        :param feature_list_or_size: feature size (input dimension of input layer) or name of features if structured
        :param output_list_or_size: output size (output dimension of last layer) or name of target if structured
        :param hidden_layer: number of hidden layers (except input and output layer)
        :param number_of_nodes: number of nodes in each hidden layer
        :param loss_function: optimizing criteria
        :param learning_rate: learning rate of model (by epoch)
        :param optimizer: optimizer in keras
        :param activation: activation function (e.g. relu, softmax, sigmoid)
        :param bias_term: bias constraint 
        :param batch_normalization: If true, run batch normalization
        """
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
        self.activation = activation
        self.bias_constraint = bias_term
        self.batch_normalization = batch_normalization
        # initialize model
        self.model = Sequential()
        self._initialize_model()

    def _initialize_model(self):
        """
        Initialize model based on user input
        
        :return: 
        """
        # FIXME: more detailed interface is required in future
        self.model.add(Dense(self.number_of_nodes, input_dim=self.feature_size, activation=self.activation))
        for layer_idx in range(self.hidden_layer):
            if self.batch_normalization:
                self.model.add(Dense(self.number_of_nodes, activation='linear', kernel_initializer='uniform'))
                self.model.add(BatchNormalization())
                self.model.add(PReLU())  # for now, after batch normalization, always use prelu
            else:
                self.model.add(Dense(self.number_of_nodes, activation=self.activation, kernel_initializer='uniform'))
        self.model.add(Dense(self.output_size, activation='linear'))  # force to linear for output layer (or softmax?)
        self.model.compile(loss=self.loss_function, optimizer=self.optimizer(lr=self.learning_rate))

    def fit(self, input_matrix, output_matrix=None, **kwargs):
        """
        fit neural network
        
        :param input_matrix: numpy matrix or data frame (if structured)
        :param output_matrix: numpy matrix
        :param kwargs: hyperparameters for fitting (number of epochs, batch size, verbose)
        :return: 
        """
        # if data is structured
        if type(input_matrix) == pd.DataFrame and output_matrix is None:
            if self.targets is None or self.features is None:
                raise KeyError("You must set feature and target first!")
            output_matrix = input_matrix[self.targets].as_matrix()
            input_matrix = input_matrix[self.features].as_matrix()

        # check if data size is correct
        assert self.feature_size == input_matrix.shape[1]
        assert self.output_size == output_matrix.shape[1]

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
        if "verbose" in kwargs:
            verbose = kwargs["verbose"]
        else:
            verbose = False
        self.model.fit(x=input_matrix, y=output_matrix,
                       batch_size=batch_size, epochs=epochs, verbose=verbose)

    def predict(self, test_data):
        return self.model.predict(test_data[self.features].as_matrix())


if __name__ == "__main__":
    data_size = 100
    sample_frame = pd.DataFrame({'aaa': np.random.random(data_size), 'bbb': np.random.random(data_size)})
    sample_frame['ccc'] = (sample_frame['aaa'] > 0.5).astype(int)
    nn_instance = NeuralNetwork(['aaa', 'bbb'], ['ccc'], batch_normalization=True)
    nn_instance.fit(sample_frame)
    predicted = nn_instance.predict(sample_frame)
    from evaluation.error_based import mse, mae
    print(mse(predicted.ravel(), np.array(sample_frame['ccc'])))
