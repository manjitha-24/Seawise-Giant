import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread, imshow

image = imread('apple.jpg', as_gray=True)
imshow(image)