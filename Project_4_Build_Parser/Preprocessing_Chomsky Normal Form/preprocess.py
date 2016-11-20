#!/usr/bin/env python

import sys, fileinput
import tree

filename = "C:/Users/Xin/Desktop/Github-repo/Natural_Language_Processing_Projects/Project_4_Build_Parser/hw4-data/train.trees"

f = open("train.trees.pre",'w')

for line in fileinput.input(filename):
    t = tree.Tree.from_str(line)

    # Binarize, inserting 'X*' nodes.
    t.binarize()

    # Remove unary nodes
    t.remove_unit()

    # The tree is now strictly binary branching, so that the CFG is in Chomsky normal form.

    # Make sure that all the roots still have the same label.
    assert t.root.label == 'TOP'

    print (t)
    t_string = str(t)+"\n"
    f.write(t_string)

f.close()
    
