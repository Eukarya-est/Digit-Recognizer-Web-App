# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:26:21 2022

@author: pdg26
"""

# import libraries
import pandas as pd 
import numpy as np
import random as rd
from ipycanvas import Canvas

def Visualization(X, label_):
    n_sample = 100; #The number of sample 
    label_idx=label_.index; # Extract index of data 'label_'
    label_rd = rd.sample(list(label_idx),100); # 100 random samples of label 'n'
    label_sp = pd.DataFrame();

    for A1 in range (0,n_sample):
        label_sp = pd.concat([label_sp, X.iloc[label_rd[A1]]],axis=1).astype(int)
    label_sp = label_sp.iloc[1:,:]
    label_sp = label_sp.transpose()
    label_xy = np.array((label_sp + 31)// 32).astype(int);

    reshapemat = np.array([]);
    mat_x = 0;
    mat_y = 0;
    dot_x1 =  np.array([]);
    dot_y1 =  np.array([]);
    dot_x2 =  np.array([]);
    dot_y2 =  np.array([]);
    dot_x3 =  np.array([]);
    dot_y3 =  np.array([]);
    dot_x4 =  np.array([]);
    dot_y4 =  np.array([]);
    dot_x5 =  np.array([]);
    dot_y5 =  np.array([]);
    dot_x6 =  np.array([]);
    dot_y6 =  np.array([]);
    dot_x7 =  np.array([]);
    dot_y7 =  np.array([]);
    dot_x8 =  np.array([]);
    dot_y8 =  np.array([]);

    for A2 in range(0, n_sample):
        reshapemat = label_xy[A2,:].reshape((28,28)).transpose()
        for A3 in range(0, 28):
            for A4 in range(0, 28):
                if reshapemat[A3,A4] == 1:
                    dot_x1 = np.append(dot_x1, A3+2+mat_x).astype(int)
                    dot_y1 = np.append(dot_y1, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] ==  2:
                    dot_x2 = np.append(dot_x2, A3+2+mat_x).astype(int)
                    dot_y2 = np.append(dot_y2, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] ==  3:
                    dot_x3 = np.append(dot_x3, A3+2+mat_x).astype(int)
                    dot_y3 = np.append(dot_y3, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] ==  4:
                    dot_x4 = np.append(dot_x4, A3+2+mat_x).astype(int)
                    dot_y4 = np.append(dot_y4, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] ==  5:
                    dot_x5 = np.append(dot_x5, A3+2+mat_x).astype(int)
                    dot_y5 = np.append(dot_y5, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] ==  6:
                    dot_x6 = np.append(dot_x6, A3+2+mat_x).astype(int)
                    dot_y6 = np.append(dot_y6, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] ==  7:
                    dot_x7 = np.append(dot_x7, A3+2+mat_x).astype(int)
                    dot_y7 = np.append(dot_y7, A4+2+mat_y).astype(int)
                elif reshapemat[A3,A4] == 8:
                    dot_x8 = np.append(dot_x8, A3+2+mat_x).astype(int)
                    dot_y8 = np.append(dot_y8, A4+2+mat_y).astype(int)
        mat_x = mat_x + 56
        if mat_x % 560 == 0:
            mat_x = 0
            mat_y = mat_y + 56

    canvas = Canvas(width=560, height=560)

    canvas.fill_style = "blue"

    canvas.fill_style = "#DFDFDF"
    canvas.fill_rects(dot_x1, dot_y1, 2)
    canvas.fill_style = "#BFBFBF"
    canvas.fill_rects(dot_x2, dot_y2, 2)
    canvas.fill_style = "#9F9F9F"
    canvas.fill_rects(dot_x3, dot_y3, 2)
    canvas.fill_style = "#7F7F7F"
    canvas.fill_rects(dot_x4, dot_y4, 2)
    canvas.fill_style = "#5F5F5F"
    canvas.fill_rects(dot_x5, dot_y5, 2)
    canvas.fill_style = "#3F3F3F"
    canvas.fill_rects(dot_x6, dot_y6, 2)
    canvas.fill_style = "#1F1F1F"
    canvas.fill_rects(dot_x7, dot_y7, 2)
    canvas.fill_style = "#000000"
    canvas.fill_rects(dot_x8, dot_y8, 2)

    return canvas