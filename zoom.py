#!/usr/bin/python3

# Karthik Karanth, 2017
# This is my solution to problem statement 2 in "image processing" for GreedyGame
# Usage: zoom.py <path to image> <pivot x> <pivot y> <scale>

# Problem statement on python without library
# 1. Take any image as input and give a zoomed image as output. 
# 2. Width and height needs to be same of input and output image. 
# 3. Take pivot point (where to zoom) and scale as parameters. 
# 4. You can only use image libraries for loading and saving images, NOT for the function part.

import sys
from math import ceil, floor

import numpy as np
from scipy.misc import imread, imsave

def resize(img, new_size):
    """
    Resizes an image using nearest neighbour interpolation

    img: a numpy array of dimensions (w, h, c) with the image
    new_size: a tuple of the form (h, w) where h is the width of
              the new image, and w is the width of the new image
    """
    # Width, height, channels
    h, w = img.shape[0], img.shape[1]
    new_h, new_w = new_size

    if len(img.shape) == 3:
        # Color image
        c = img.shape[2]
        new_img = np.zeros((new_h, new_w, c), dtype='uint8')
    else:
        # Grayscale image
        new_img = np.zeros((new_h, new_w), dtype='uint8')

    scale_w = new_w / w
    scale_h = new_h / h

    for i in range(new_w):
        for j in range(new_h):
            # Nearest neighbour interpolation
            pixel = img[floor(j / scale_h), floor(i / scale_w)]
            new_img[j, i] = pixel
            continue
    return new_img

def zoom(img, px, py, scale):
    """
    Zooms into an image

    img: a numpy array of dimensions (w, h, c) with the image
    px: x coordinate of the pivot (topleft corner is 0,0)
    py: y coordinate of the pivot (topleft corner is 0,0)
    scale: factor by which to scale image
    """
    # height, width
    h, w = img.shape[0], img.shape[1]

    # Bounding box width and height
    bb_w = ceil(w / scale)
    bb_h = ceil(h / scale)
    
    # Move the pivot to ensure that we can zoom into that part
    px = max(bb_w // 2, px)
    px = min(w - bb_w // 2, px)
    py = max(bb_h // 2, py)
    py = min(h - bb_h // 2, py)

    # Crop out the region of interest
    new_img = img[py - bb_h // 2: py + bb_h // 2, px - bb_w // 2:px + bb_w //2]

    new_img = resize(new_img, (h, w))

    return new_img

def main(argv):
    if len(sys.argv) != 5:
        print('Usage: zoom.py <path to image> <pivot x> <pivot y> <scale>',
              file=sys.stderr)
        sys.exit(1)

    filepath, px, py, scale = sys.argv[1:]
    px, py, scale = int(px), int(py), float(scale)

    input_img = imread(filepath)
    output_img = zoom(input_img, px, py, scale)

    extension = filepath.split('.')[-1]
    output_filepath = filepath[:filepath.rindex('.')] + '_zoomed.' + extension
    print('Saving to {}'.format(output_filepath))
    imsave(output_filepath, output_img)

if __name__ == '__main__':
    main(sys.argv)
