import re
import os
import random
import unidecode
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
		if ',' not in l: 
			print("-------")
			continue
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

def concat2(units):
	wordlist = ""
	for unit in units:
		f = open("words/"+unit+".txt","r")
		wordlist+=f.read()
		if wordlist[-1:] != "\n":
			wordlist+="\n"
		f.close()
	print(wordlist)

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


def is_alpha(word):
	word = unidecode.unidecode(word)
	try:
		return word.encode('ascii').isalpha()
	except:
		return False

def proc2(n):
	f = open("words/"+n+"(raw).txt")
	f2 = open("words/"+n+".txt","w")
	r=0
	for l1 in f.readlines():
		l1 = l1.replace("*","")
		ss1 = l1.find("(")
		ss2 = l1.find("（")

		if not (ss1>-1 and is_alpha(l1[ss1+1])):
			ss1 = 100000
		if not (ss2>-1 and is_alpha(l1[ss2+1])):
			ss2 = 100000
		s1 = ss1 if ss1 < ss2 else ss2

		s2 = l1.find(",")
		c = l1[:s1].strip()
		p = l1[s1+1:s2-1]
		e = l1[s2+1:].strip("\n")
		if "(r)" in e:
			e = e.replace("(r)","").strip()
			e = "(" + e + ")"
			e += " (r)"
			r +=1
		else:
			e = "(" + e + ")"
		st = c+","+ p + " "+e
		
		f2.write(st+"\n")
	print(r)

def askRandom(units,missed=False):
	if missed:
		with open("missed_words.txt","r") as f:
			wordlist=f.read() 
	else:
		wordlist = ""
		for unit in units:
			f = open("words/"+unit+".txt","r")
			wordlist+=f.read()
			if wordlist[-1:] != "\n":
				wordlist+="\n"
			f.close()
	words = wordlist.split("\n")
	print("total words: %d"%len(words))
	nums = list(range(len(words)))
	while(nums):
		ind = random.randint(0,len(nums)-1)
		line = nums.pop(ind)
		word = words[line]
		if "(" in word and "," in word:
			c = word.index(',')
			p = word.index('(')
			chara = word[:c]
			pin = word[c+1:p]
			eng = word[p:]
			print(eng,end="",flush=True)
			input()
			print(pin,chara,"got it?(],q): ",end="",flush=True)
			resp=input()
			if resp == "]":
				with open("nums.txt","w+") as f2:
					f2.write(str(nums))
				print("yay")
			elif resp == "q":
				nums.append(line)
				print(nums)
				exit()
			else: 
				print("you suck")
				nums.append(line)

			print("------------------")
			print("num left to get: ",len(nums))
			print("------------------")
		else:
			print("huh: ", word)



def unitRange(st,en):
	units = []
	for i in range(st,en+1):
		units.append("%s%d_%d"%("A"if i<16 else "B",int(i/2)+1,i%2+1))
	return units

#concat2(unitRange(10,18))
#proc2("B14_1")
shift_2("B14_1")
#askRandom(unitRange(6,10))