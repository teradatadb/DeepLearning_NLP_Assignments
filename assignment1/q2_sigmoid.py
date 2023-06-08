
#!/usr/bin/env python

import numpy as np


def sigmoid(x):
    """
    Compute the sigmoid function for the input here.

    Arguments:
    x -- A scalar or numpy array.

    Return:
    s -- sigmoid(x)
    """

    ### YOUR CODE HERE
    # normal implementation
    # s = 1.0 / (1.0 + np.exp(-x))
    pos_mask = (x >= 0)
    neg_mask = (x < 0)
    z = np.zeros_like(x, dtype=np.float64)
    z[pos_mask] = np.exp(-x[pos_mask])