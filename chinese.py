import re
import os

def shift_deck(fn):
	f = open(fn,"r")
	for l in f.readlines():
		p1 = l.index('(')
		c = l.index(',')
		print(l[c+1:p1-1] + "," + l[:c] + " " +l[p1:],end='')


