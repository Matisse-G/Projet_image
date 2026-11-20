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
from skimage.morphology import binary_dilation, disk
from skimage.transform import resize

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

def masque(
    masque_actuel, zone_detectee=None, forme_cible=None, rayon_dilatation=5 ):

  nouveau_masque = masque_actuel.copy()

  if zone_detectee is not None:
    if rayon_dilatation > 0:
      zone_a_masquer = binary_dilation(zone_detectee, disk(rayon_dilatation))
    else:
      zone_a_masquer = zone_detectee

    nouveau_masque[zone_a_masquer] = False

  if forme_cible is not None:
    nouveau_masque = resize(
        nouveau_masque,
        forme_cible,
        order=0, 
        preserve_range=True,
    ).astype(bool)

  return nouveau_masque
    

def decimation(img):
    return img[::2, ::2]

    

img= io.imread('images/laitcodejpg.jpg')
if len(img.shape) == 3:
    img = color.rgb2gray(img)
    

Gflitre = gauss(1)


img_flitrer = scipy.signal.convolve2d(img, Gflitre, mode='same')
img_div2 = decimation(img_flitrer)

img_flitrer = scipy.signal.convolve2d(img_div2, Gflitre, mode='same')
img_div4 = decimation(img_flitrer)

img_flitrer = scipy.signal.convolve2d(img_div4, Gflitre, mode='same')
img_div8 = decimation(img_flitrer)


plt.figure()
plt.imshow(img_div8, cmap='gray')
plt.figure()
plt.imshow(img, cmap='gray')