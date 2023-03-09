
#!/usr/bin/env python

import numpy as np
import random

from q1_softmax import softmax
from q2_sigmoid import sigmoid, sigmoid_grad
from q2_gradcheck import gradcheck_naive


def forward_backward_prop(data, labels, params, dimensions):
    """
    Forward and backward propagation for a two-layer sigmoidal network

    Compute the forward propagation and for the cross entropy cost,
    and backward propagation for the gradients for all parameters.

    Arguments:
    data -- M x Dx matrix, where each row is a training example.
    labels -- M x Dy matrix, where each row is a one-hot vector.
    params -- Model parameters, these are unpacked for you.
    dimensions -- A tuple of input dimension, number of hidden units
                  and output dimension
    """

    ### Unpack network parameters (do not modify)
    ofs = 0
    Dx, H, Dy = (dimensions[0], dimensions[1], dimensions[2])

    W1 = np.reshape(params[ofs:ofs+ Dx * H], (Dx, H))
    ofs += Dx * H
    b1 = np.reshape(params[ofs:ofs + H], (1, H))
    ofs += H
    W2 = np.reshape(params[ofs:ofs + H * Dy], (H, Dy))
    ofs += H * Dy
    b2 = np.reshape(params[ofs:ofs + Dy], (1, Dy))

    ### YOUR CODE HERE: forward propagation
    h1_out = np.dot(data, W1) + b1
    h1_act = sigmoid(h1_out)
    h2_out = np.dot(h1_act, W2) + b2
    probs = softmax(h2_out)
    cost = np.mean(np.sum(-labels * np.log(probs), axis=1))
    ### END YOUR CODE

    ### YOUR CODE HERE: backward propagation
    M = data.shape[0]
    dh2_out = (probs - labels) / M
    gradW2 = np.dot(h1_act.T, dh2_out)
    gradb2 = np.sum(dh2_out, axis=0, keepdims=True)
    dh1_out = np.dot(dh2_out, W2.T) * sigmoid_grad(h1_act)
    gradW1 = np.dot(data.T, dh1_out)
    gradb1 = np.sum(dh1_out, axis=0, keepdims=True)
    ### END YOUR CODE

    ### Stack gradients (do not modify)
    grad = np.concatenate((gradW1.flatten(), gradb1.flatten(),