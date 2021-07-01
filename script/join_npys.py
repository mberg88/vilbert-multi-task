# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:02:18 2021

@author: MattiaL
"""

import numpy as np
import os
import sys

if __name__ == "__main__":
    '''
    Joins NPYs.
    Run as
    python join_npys.py folder-NPYs-are-saved-to
    From https://github.com/facebookresearch/...
    ...vilbert-multi-task/issues/77#issuecomment-805822681
    '''
    f_list = []
    
    # NPY joining all NPYs
    globalFil = os.path.join(sys.argv[1], 'globalFil.npy')
    
    for dirpath, dirnames, filnames in os.walk(sys.argv[1]):
        for fil in filnames:
            if (fil.endswith('.npy')) and \
                (os.path.join(dirpath, fil) != globalFil):
                # load NPY
                # 0-D array
                va = np.load(os.path.join(dirpath, fil), allow_pickle = True)
                print(fil)
                print(va[()].keys())
                
                f_list.append({
                            "file_name" : va[()]['image_id'],
                            "file_path" : va[()]['file_path'],
                            "bbox"      : va[()]['bbox'],
                            "num_box"   : va[()]['num_boxes']
                            })
    
    print('save list')
    np.save(globalFil, f_list)
            
    