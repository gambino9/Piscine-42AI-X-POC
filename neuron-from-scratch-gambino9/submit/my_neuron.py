# -*- coding: utf-8 -*-
import numpy as np

LR = 0.01


def getData():
	return np.linspace(-6, 6, 30), np.linspace(-6, 6, 30)


def linear_activation(input):
	return  # Need Some Code


def d_linear_d_input(input):
	#  Need Some Code
	return  # Need Some Code


def mean_squared_error(predict, target):
	return  # Need Some Code


# Biais de perceptron : facilite a activer un neurone. Si biais fort, le neurone
# va etre active sans probleme. Sinon, le neurone ne s'activera pas
class Neurone:
	def __init__(self, nb_features):
		self.weight = np.ones(nb_features, 1)
		self.bias = np.ones(1)
		self.grad_w = np.zeros((nb_features, 1))
		self.grad_b = np.zeros(1)
		pass

	def forward(self, input):
		return  # Need Some Code

	def backward(self, pre_activation, activation, inputs, target):
		"""
		This function computes the gradient of the weights $W$ and the gradient
		of the bias $b$ then stores them inside the class variables created in
		the constructor.
		"""
		pass
		# Need Some Code

	def resetGrad(self):
		self.grad_w = np.zeros((self.nb_features, 1))
		self.grad_b = np.zeros(1)


if __name__ == '__main__':
	pass
	# Your main function
