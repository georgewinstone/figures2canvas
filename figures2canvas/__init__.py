# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:36:12 2017

@author: george
"""

import numpy as np
import matplotlib.pyplot as plt
import os 
import matplotlib._pylab_helpers
import os
import pip

from PIL import Image

def install(package):
    pip.main(['install', package])



def merge_images(file1, file2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result
    
    


def names(start,stop):
    """generates list of saved figurenames"""
    
    names=[]
    
    for i in np.arange(start,stop):
        names.append('temp_'+str(i)+'.png')
        
    return names 
    

def images(namelist):
    """returns a list of images from filenames in names """
    
    figurenames=[]
    for i in namelist:
        
        figurenames.append(Image.open(i))
        
    return figurenames



"""@@@@@@"""


def merge(selection='all'):

    
    figures=[manager.canvas.figure
             for manager in matplotlib._pylab_helpers.Gcf.get_all_fig_managers()]
    
    
    print(figures)
    
    
    
    
    
    number=len(figures) # number of images to merge, msut b in 1.png 2.png etc etc 
    
    shape=[2,number/2] #x andy 
    
    fnames=names(1,number+1)
    
    #need to save all open figures to fnames
    
    for i in np.arange(len(figures)):
        f=figures[i]
        f.savefig(fnames[i])
    
    
    
    
    
    
    
    
    figures=images(fnames)
    
    
    widths=[]
    for i in np.arange(shape[0]):
        widths.append(figures[i].size[0])
    totalwidth=np.sum(widths)
        
        
    heights=[]
    for i in np.arange(shape[1]):
        heights.append(figures[i].size[1])
    totalheight=np.sum(heights)
        
    newfigure=Image.new('RGB',(totalwidth,totalheight))
    
    """ rehape the lsit to be compatible so they can be called with shape """
    
    
    
    reshape=[]
    for j in np.arange(shape[1]):
        xlist=[]
        for i in np.arange(shape[0]):
            print shape[0]*j + i
            xlist.append(figures[shape[0]*j + i])
            
        reshape.append(xlist)
    
    
    for j in np.arange(shape[1]):
        
        for i in np.arange(shape[0]):
            
            newfigure.paste(im=reshape[j][i],box=(widths[0]*i,heights[0]*j)) #fix this properly sometime
    
    
    newfigure.save('mergedfigure.png')
    
    
if __name__ == "__main__":
    print 'running directly'
    
    
    
    
    