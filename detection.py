#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:43:34 2026

@author: aminfray
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from skimage import io, color, measure

img= io.imread('img/laitcode.jpg')




def fonctionGauss(X, Y, sigma):
    G = np.exp(-(X**2 + Y**2)/(2*sigma**2))
    return G


def gauss(sigma):
    ray = 3 * sigma
    x = range(-ray, ray+1)
    X, Y = np.meshgrid(x, x)
    G = fonctionGauss(X, Y, sigma)
    G = G / G.sum()
    return G

def decimation(img):
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 1:
                sup(i,j)
return img