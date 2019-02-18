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

def shift_2(fn):
	f = open("words/"+fn+".txt","r")
	for l in f.readlines():
		c = l.index(',')
		if "(" in l:
			p1 = l.index('(')
			print( l[:c]+" "+l[c+1:p1-1]  +","  + " " +l[p1:],end='')
		else:
			print(l[c+1:-1] + "," + l[:c])

def concat(): 
	for d in os.walk('words/'):
		for f in d[2]:
			for l in open("words/"+f,"r").readlines():
				print(l,end="")
			print("")

	#shift_deck("words/"+f)
	#shift_deck("words/A5_2.txt")


def proc(n):
	f = open("words/"+n+"(raw).txt")
	f2 = open("words/"+n+".txt","w")
	while True:
		l1 = f.readline()
		l2 = f.readline()
		num = f.tell()
		l3 = f.readline()
		if not l2:
			break 
		if "|" in l3:
			l2 = l2[:-1]+" "+l3
		else:
			f.seek(num)
		l1 = l1.replace("*","")
		f2.write(l1[:-1] +" "+ l2)

shift_2("A8_2")
