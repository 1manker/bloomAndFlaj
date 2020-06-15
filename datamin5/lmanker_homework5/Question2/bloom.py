#Lucas Manker
#part 2 homework 5
from numpy import log as ln
import math
import mmh3 
from bitarray import bitarray 


def getK(m):
	f = open("listed_username_30.txt","r",encoding='utf-8')
	lines = f.readlines()
	n = len(lines)
	k = (m/n)*ln(2)
	k = int(round(k))
	inner = 1 - pow(1-(1/m),(k*n))
	p = pow(inner, k)
	print("m = ", m)
	print("n = ", n)
	print("k = ", k)
	print("False Positive Rate: ", p)
	f.close()
	return k

def initArray(m):
	bit_arr = bitarray(m)
	bit_arr.setall(0)
	return bit_arr

def fillBloom(bit_arr, k):
	f = open("listed_username_30.txt","r",encoding='utf-8')
	lines = f.readlines()
	count = 0
	for x in lines:
		digests = []
		for i in range(k):
			digest = mmh3.hash(x, i) % len(bit_arr)
			digests.append(digest)
			bit_arr[digest] = True
	f.close()
	return bit_arr



def streamToBloom(bit_arr, k):
	f = open("listed_username_365.txt","r",encoding='utf-8')
	lines = f.readlines()
	found = 0
	allTrue = 0
	count = 0
	for x in lines:
		allTrue = 0
		digests = []
		for i in range(k):
			digest = mmh3.hash(x, i) % len(bit_arr)
			digests.append(digest)
			if(bit_arr[digest] == True): allTrue += 1
		if(allTrue == 3): found += 1
		else: count += 1
	f.close()
	print("There were ", found, "matches found within the original dataset.")
	print(count)

def check(toCheck):
	f = open("listed_username_30.txt","r",encoding='utf-8')
	lines = f.readlines()
	falseP = 0
	for x in toCheck:
		if(x not in lines): falseP += 1
	print(falseP)
	print(len(toCheck))

m = 5000000
k= getK(m)

bit_arr = initArray(m)

bit_arr = fillBloom(bit_arr, k)
streamToBloom(bit_arr, k)

