#! /usr/bin/env python

import sys
import os
import numpy as np
import cPickle as pickle
import argparse

from joblib import Parallel, delayed

from skimage.filters.rank import entropy
from skimage.morphology import remove_small_objects, disk
from skimage.measure import label, regionprops
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage import img_as_float

from sklearn import mixture

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Generate mask for thumbnail images')
parser.add_argument("stack_name", type=str, help="stack name")
parser.add_argument("input_dir", type=str, help="input dir")
parser.add_argument("first_sec", type=int, help="first section")
parser.add_argument("last_sec", type=int, help="last section")
args = parser.parse_args()

stack = args.stack_name
input_dir = args.input_dir
first_secind = args.first_sec
last_secind = args.last_sec

# stack = sys.argv[1]
# input_dir = sys.argv[2]
# # mask_dir = sys.argv[3]
# # masked_tb_dir = sys.argv[4]
# first_secind = int(sys.argv[3])
# last_secind = int(sys.argv[4])

def generate_mask(img):

    h, w = img.shape
    
    e = entropy(img, disk(5))
    
    clf = mixture.GMM(n_components=2, covariance_type='full')
    clf.fit(np.atleast_2d(e[e > 0.1]).T)

    means = np.squeeze(clf.means_)

    order = np.argsort(means)
    means = means[order]

    covars =np.squeeze(clf.covars_)
    covars = covars[order]
                
    weights = clf.weights_
    weights = weights[order]

    counts, bins = np.histogram(e.flat, bins=100, density=True);

    gs = np.array([w * 1./np.sqrt(2*np.pi*c) * np.exp(-(bins-m)**2/(2*c)) for m, c, w in zip(means, covars, weights)])

    thresh = bins[np.where(gs[-1] - gs[-2] < 0)[0][-1]]

    v = e > thresh

    l = label(v, background=0)
    mask = l == np.argmax([p.area for p in regionprops(l+1)])
    
    mask = ~remove_small_objects(~mask, min_size=10000, connectivity=8)
    
    l = label(v)
    l[v > 0] = -1
    props = regionprops(l)
    
    border_holes = np.where([np.any(p.coords[:,0] == 0) or np.any(p.coords[:,1] == 0) \
                             or np.any(p.coords[:,0] == h-1) or np.any(p.coords[:,1] == w-1) 
                             for p in props])[0]

    for i in border_holes:
        c = props[i].coords
        mask[c[:,0], c[:,1]] = 0
    
    return mask


def f(stack, sec):

    img = rgb2gray(imread(input_dir+'/'+stack+'_%04d_'%sec + suffix + '.tif'))
    
    try:
        mask = generate_mask(img)
    except:
        raise Exception('%d'%sec)
    
    img2 = img.copy()
    img2[~mask] = 0

    imsave(mask_dir+'/'+stack+'_%04d_'%sec + suffix + '_mask.png', img_as_float(mask))
    imsave(masked_img_dir+'/'+stack+'_%04d_'%sec + suffix + '_masked.png', img2)


suffix = '_'.join(os.path.split(input_dir)[-1].split('_')[1:])
mask_dir = os.environ['DATA_DIR'] + '/' + stack + '_' + suffix + '_mask'
masked_img_dir = os.environ['DATA_DIR'] + '/' + stack + '_' + suffix + '_masked'

if not os.path.exists(mask_dir):
    try:
        os.makedirs(mask_dir)
    except:
        pass

if not os.path.exists(masked_img_dir):
    try:
        os.makedirs(masked_img_dir)
    except:
        pass
    
_ = Parallel(n_jobs=16)(delayed(f)(stack, sec) for sec in range(first_secind, last_secind+1))