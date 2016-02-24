from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
from skimage import io
import matplotlib.cm as cm
import os
import glob




filename = 'C:\\Users\\schan3\\Desktop\\New folder (2)\\'
imgname = 'SBU_2015.01.26_18.21.27_flake_11032_cam_1'


file_processed = 0

for fname in glob.glob(filename + '*.png'):
    count = 0
    print fname
    image = io.imread(fname)
    image_gray = rgb2gray(image)

    blobs_doh = blob_doh(image_gray, max_sigma=1000, min_sigma =40, threshold=.00045, overlap = .25)
    
    blobs_list = [blobs_doh]
    colors = ['red']
    titles = ['Snow flake counts using Determinant of Hessian']
    sequence = zip(blobs_list, colors, titles)
    
    for blobs, color, title in sequence:
        fig, ax = plt.subplots(1, 1)
        ax.set_title(title)
        ax.imshow(image, interpolation='nearest', cmap = cm.Greys_r)
        for blob in blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
    
            ax.add_patch(c)
            count += 1
    
    
    plt.text(1000, 1250, 'Snow flake counts:' + str(count), color='white', fontsize = 15)
    
    plt.savefig(fname)
    plt.close('all')
    
    file_processed += 1
    print file_processed


