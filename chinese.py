import re
import os

def shift_deck(fn):
	f = open(fn,"r")
	for l in f.readlines():
		c = l.index(',')
		if "(" in l:
			p1 = l.index('(')
			print(l[c+1:p1-1] + "," + l[:c] + " " +l[p1:],end='')
		else:
			print(l[c+1:-1] + "," + l[:c])

for d in os.walk('words/'):
	for f in d[2]:
		shift_deck("words/"+f)
#shift_deck("words/A5_2.txt")


'''
f = open("words/A5_2(raw).txt")
f2 = open("words/A5_2(u).txt","w")
while True:
	l1 = f.readline()
	l2 = f.readline()
	if not l2:
		break 
	l1 = l1.replace("*","")
	f2.write(l1[:-1] +" "+ l2)
'''

