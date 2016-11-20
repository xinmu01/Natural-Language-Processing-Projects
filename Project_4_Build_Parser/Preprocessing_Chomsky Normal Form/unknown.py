#!/usr/bin/env python

import sys, fileinput
import collections
import tree

count = collections.defaultdict(int)

f = open("train.trees.pre.unk","w")

filename = "C:/Users/Xin/Desktop/Github-repo/Natural_Language_Processing_Projects/Project_4_Build_Parser/hw4-data/train.trees.pre"

trees = []
for line in fileinput.input(filename):
    t = tree.Tree.from_str(line)
    for leaf in t.leaves():
        count[leaf.label] += 1
    trees.append(t)

for t in trees:
    for leaf in t.leaves():
        if count[leaf.label] < 2:
            leaf.label = "<unk>"
    sys.stdout.write("{0}\n".format(t))
    f.write("{0}\n".format(t))

f.close()
