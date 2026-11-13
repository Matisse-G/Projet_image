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
import math
import scipy

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
    return img[::2, ::2]

img= io.imread('images/laitcodejpg.jpg')
if len(img.shape) == 3:
    img = color.rgb2gray(img)
    

Gflitre = gauss(1)

img_flitrer = scipy.signal.convolve2d(img, Gflitre, mode='same')
img_div2 = decimation(img_flitrer)

plt.figure()
plt.imshow(img_div2)
plt.figure()
plt.imshow(img_div2)