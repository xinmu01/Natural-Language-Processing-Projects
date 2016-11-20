#!/usr/bin/env python

import sys, fileinput
import tree

filename = "C:/Users/Xin/Desktop/Github-repo/Natural_Language_Processing_Projects/Project_4_Build_Parser/hw4-data/train.trees.pre"
f = open("train.trees.transform_back","w")
for line in fileinput.input(filename):
    try:
        t = tree.Tree.from_str(line)

        t.restore_unit()
        t.unbinarize()

        print (t)
        t_string = str(t)+"\n"
        f.write(t_string)        
        
    except:
        print ("")

f.close()
    
    
