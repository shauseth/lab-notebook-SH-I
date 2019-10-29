# SH-I

import random
import numpy as np
import pandas as pd
import itertools

### Neural Net
class Network(object):

    def __init__(self, sizes):

        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):

        for b, w in zip(self.biases, self.weights):

            a = sigmoid(np.dot(w, a) + b)

        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data = None):

        training_data = list(training_data)
        n = len(training_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        for j in range(epochs):

            random.shuffle(training_data)

            mini_batches = [
                training_data[k:k + mini_batch_size]
                for k in range(0, n, mini_batch_size)]

            for mini_batch in mini_batches:

                self.update_mini_batch(mini_batch, eta)

            if test_data:

                print("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test))

            else:

                print("Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:

            delta_nable_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nable_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

            self.weights = [w - (eta / len(mini_batch)) * nw
                            for w, nw in zip(self.weights, nabla_w)]
            self.biases = [b - (eta / len(mini_batch)) * nb
                           for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        activation = x
        activations = [x]
        zs = []

        for b, w in zip(self.biases, self.weights):

            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])

        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers):

            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())

        return (nabla_b, nabla_w)

    def evaluate(self, test_data):

        test_results = [(np.argmax(self.feedforward(x)), np.argmax(y))
                        for (x, y) in test_data]

        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):

        return (output_activations - y)

def sigmoid(z):

    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):

    return sigmoid(z) * (1 - sigmoid(z))

# Data
data = pd.read_csv('rfu_norm.csv')
data = data.round(decimals = 4)

def vectorized_result(i):

    e = np.zeros((3, 1))

    if 0.66 <= i:

        e[0] = 1.0

    elif 0.33 <= i < 0.66:

        e[1] = 1.0

    elif i < 0.33:

        e[2] = 1.0

    return e

monomers = ['Fuc', 'GalNAc', 'Gal', 'GlcNAc', 'Glc', 'KDN', 'Man', 'Neu5,9Ac', 'Neu5Ac', 'Neu5Gc']
link_type = ['a', 'b']
link_pos = ['1-2', '1-3', '1-4', '1-5', '2-3', '2-6', '-']

units = []

for x, y, z in list(itertools.product(monomers, link_type, link_pos)):

    units.append(x + y + z)

linkages = ['Sp0', 'Sp8', 'Sp9', 'Sp10', 'Sp11', 'Sp12', 'Sp13', 'Sp14', 'Sp15', 'Sp16', 'Sp17', 'Sp18', 'Sp19', 'Sp20', 'Sp21', 'Sp22', 'Sp23', 'Sp24', 'Sp25', 'MDPLys']

def counter(glycan):

    count_list = []

    for unit in units + linkages:

        n = glycan.count(unit)

        count_list.append(n)

    return np.array(count_list, dtype = float).reshape((-1, 1))

input_data = list(data['Structure on Masterlist'].apply(counter))
output_data = list(data['MpL-1 (10ug/ml)'].apply(vectorized_result))

# Set Up
split = 510

training_data = zip(input_data[:split], output_data[:split])
test_data = zip(input_data[split:], output_data[split:])

net = Network([160, 30, 3])

net.SGD(training_data, 30, 1, 3.0, test_data = test_data)
