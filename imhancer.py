"""
VEViD test script 1:
All steps (load_img -> init_kernel -> apply_kernel) are performed in a single run method.
This is for users who want to get the result on a single image with indicated VEViD parameters.

"""
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import torch

from phycv import VEVID, VEVID_GPU
from phycv import PST, PST_GPU
from phycv import PAGE

# VEViD parameters
# vS = 0.1
# vT = 0.01
# vb = 0.16
# vG = 1.4


# run VEVID CPU version
vevid_cpu = VEVID()
def enhance(img_file, vS, vT, vb, vG):
    vevid_output_cpu = vevid_cpu.run(img_file=img_file, S=vS, T=vT, b=vb, G=vG)
    return vevid_output_cpu



# pst_S = 0.3
# pst_W = 15
# pst_sigma_LPF = 0.15
# pst_thresh_min = 0.05
# pst_thresh_max = 0.9
# pst_morph_flag = 1

def pst(img_file, pst_S, pst_W, pst_sigma_LPF, pst_thresh_min, pst_thresh_max, pst_morph_flag):
    # indicate image file, height and width of the image, and GPU device (if applicable)
    # PST parameters
    # run PST CPU version
    pst_cpu = PST()
    pst_output_cpu = pst_cpu.run(
        img_file,
        pst_S,
        pst_W,
        pst_sigma_LPF,
        pst_thresh_min,
        pst_thresh_max,
        pst_morph_flag,
    )
    return pst_output_cpu

def page(img_file, mu_1, mu_2, sigma_1, sigma_2, S1, S2, sigma_LPF,thresh_min, thresh_max, morph_flag):

    page_cpu = PAGE(direction_bins=10)
    page_edge_cpu = page_cpu.run(
        img_file,
        mu_1,
        mu_2,
        sigma_1,
        sigma_2,
        S1,
        S2,
        sigma_LPF,
        thresh_min,
        thresh_max,
        morph_flag,
    )
    return page_edge_cpu



