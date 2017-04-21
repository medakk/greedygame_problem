#!/usr/bin/python3

# Karthik Karanth, 2017
# This is my solution to problem statement 2 in "image processing"
# Usage: test_zoom.py

import matplotlib.pyplot as plt
from scipy.misc import imread

from zoom import zoom

plt.rcParams['image.cmap'] = 'gray'

file_count = 4
filepaths = ['images/cat1.jpg', 'images/cat2.jpg', 'images/cat3.jpg', 'images/cat4.jpg']
pivots = [(256, 256), (450, 220), (50, 50), (320, 100)]
scales = [1.5, 4.67, 9, 2]

for i in range(file_count):
    filepath, pivot, scale = filepaths[i], pivots[i], scales[i]

    img = imread(filepath)
    zoomed_img = zoom(img, *pivot, scale)

    plt.subplot(2, file_count, i + 1)
    plt.imshow(img)
    plt.plot([pivot[0]], [pivot[1]], 'o', c='r')
    plt.axis('off')
    plt.title('{}x{}'.format(img.shape[1], img.shape[0]))

    plt.subplot(2, file_count, i + 1 + file_count)
    plt.imshow(zoomed_img)
    plt.axis('off')
    plt.title('Scale: {}'.format(scale))

plt.tight_layout()
plt.show()
