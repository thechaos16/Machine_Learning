# -*- coding: utf-8 -*-

import numpy as np
import copy
from keras_models.neural_network import NeuralNetwork


class CartPoleAgent(NeuralNetwork):
    def __init__(self, env, discount_rate=0.9, epsilon=1.0,
                 learning_rate=0.01, hidden_layers=3, number_of_nodes=128):
        """
        This specific agent uses neural network by using keras. It uses deep q-learning from deepmind
        
        :param env: environment (in this case, cartpole from gym)
        :param discount_rate: decay rate for future q-value
        :param epsilon: exploration (epsilon-greedy method)
        :param learning_rate: learning rate of neural network
        :param hidden_layers: number of hidden layers 
        :param number_of_nodes: number of nodes for all layer (currently, all layers have same number of nodes)
        """
        self.env = env
        # initialize model
        super().__init__(4, env.action_space.n,
                         hidden_layer=hidden_layers, number_of_nodes=number_of_nodes, learning_rate=learning_rate)
        # initialize parameters
        self.memory = []
        # hyperparameter
        self.epsilon = epsilon
        self.discount_rate = discount_rate

    def run(self, episodes=10, max_time=1000):
        for i in range(episodes):
            state = self.env.reset()
            state = np.reshape(state, [1, 4])
            for time in range(max_time):
                # model evaluation by time it stays alive relative to max_time
                cur_act = self.action(state)

                next_state, reward, done, _ = self.env.step(cur_act)
                next_state = np.reshape(state, [1, 4])

                self.add_memory(state=state, action=cur_act, reward=reward, next_state=next_state, done=done)
                state = copy.deepcopy(next_state)

                if done:
                    print("Score: {fin_time}/{time_limit}".format(fin_time=time, time_limit=max_time))
                    break
            # train after one episode
            self.train()

    def train(self, batch_size=500):
        """
        Train model using experience replay (same as classical q-learning)
        
        :param batch_size: model will train randomly selected batch from memory
        :return: 
        """
        memory_size = len(self.memory)
        if memory_size == 0:
            raise IndexError("You must ")
        batch_size = min(memory_size, batch_size)
        random_memory_idx = np.random.choice(memory_size, batch_size)
        for idx in random_memory_idx:
            replay = self.memory[idx]
            # Following lines are basis of Q-learning
            # compute q-value
            q_value = replay['reward']  # old q-value
            # if an agent is still alive (have future), then update q-value
            if not replay['done']:
                # FIXME: shouldn't be there learning rate from future?
                q_value += self.discount_rate * np.max(self.model.predict(replay['next_state'])[0])  # add future value
            # Q-value update
            prediction = self.model.predict(replay['state'])
            prediction[0][replay['action']] = q_value
            # train with revised reward
            self.model.fit(replay['state'], prediction, epochs=1, verbose=False)

    def add_memory(self, **kwargs):
        """
        takes some actions and add result in memory
        
        :param kwargs: state: 4-length list, action: int, reward: int, next_state: 4-length list, done: bool
        :return: 
        """
        # memory contains dictionary to keep order of variables
        self.memory.append(kwargs)

    def action(self, state):
        """
        determine action that agent will do in current state
        
        :param state: current state
        :return: 
        """
        # epsilon-greedy (exploration)
        if np.random.random() <= self.epsilon:
            return self.env.action_space.sample()
        # expected reward
        prediction = self.model.predict(state)
        return np.argmax(prediction[0])


if __name__ == "__main__":
    agent = CartPoleAgent(None)
