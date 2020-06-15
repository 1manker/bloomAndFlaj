#Lucas Manker
#Homework 5 code
import random
import re

#2.3.1

def twoThreeOneA():
	f = open("ex.txt", "w+")
	for x in range(1,1000000):
		f.write(str(random.randint(1, 99999)))
		f.write(",")
	f.close
	numDict = {}
	f = open("ex.txt", "r")
	lines = f.read()
	split = lines.split(",")
	for x in split[:-1]:
		key, value = x, int(x)
		numDict[x] = int(x)
	allvals = numDict.values()
	maxval = max(allvals)
	print(maxval)
	f.close()

def twoThreeOneB():
	f = open("ex.txt", "w+")
	for x in range(1,1000000):
		f.write(str(random.randint(1, 99999)))
		f.write(",")
	f.close
	numDict = {}
	f = open("ex.txt", "r")
	lines = f.read()
	split = lines.split(",")
	for x in split[:-1]:
		if x in numDict.keys():
			numDict[x] += 1
		else:
			numDict[x] = 1
	sum, totals = 0, 0
	for key in numDict:
		sum += int(key) * numDict[key]
		totals += numDict[key]
	avg = sum/totals;
	print(avg)
	f.close()

def twoThreeOneC():
	f = open("ex.txt", "w+")
	for x in range(1,1000000):
		f.write(str(random.randint(1, 99)))
		f.write(",")
	f.close
	numDict = {}
	f = open("ex.txt", "r")
	lines = f.read()
	split = lines.split(",")
	for x in split[:-1]:
		key, value = x, int(x)
		numDict[x] = int(x)
	print(sorted(numDict))
	f.close()

def twoThreeOneD():
	f = open("ex.txt", "w+")
	for x in range(1,1000000):
		f.write(str(random.randint(1, 99)))
		f.write(",")
	f.close
	numDict = {}
	f = open("ex.txt", "r")
	lines = f.read()
	split = lines.split(",")
	for x in split[:-1]:
		key, value = x, int(x)
		numDict[x] = int(x)
	print(len(numDict))
	f.close()

def threeTwoOne():
	sentence = ("The most eﬀective way to represent documents as sets, "
	"for the purpose of identifying lexically similar documents is to "
	"construct from the document the set of short strings that appear within it.")
	sentence = re.sub(r'[^\w\s]','',sentence).lower()
	print(sentence)
	shingles = 3
	words = sentence.split()
	kshingles = []
	for x in range(len(words) - 3):
		temp = []
		temp.append(words[x])
		temp.append(words[x+1])
		temp.append(words[x+2])
		kshingles.append(temp)

	print(kshingles[:10])

def threeThreeThree():
	matrix = [[0,1,0,1],[0,1,0,0],[1,0,0,1],[0,0,1,0],[0,0,1,1],[1,0,0,0]]
	minhashVals1 = []
	minhashVals2 = []
	minhashVals3 = []
	sig1 = []
	sig2 = []
	sig3 = []
	for x in range(len(matrix)):
		minhashVals1.append(((2*x)+1)%6)
		minhashVals2.append(((3*x)+2)%6)
		minhashVals3.append(((5*x)+2)%6)
	for x in range(len(matrix[0])):
		sig1.append(999999999)
		sig2.append(999999999)
		sig3.append(999999999)
	for xs in range(len(matrix)):
		for x in range(len(matrix[xs])):
			if(matrix[xs][x] == 1):
				if(sig1[x] > minhashVals1[xs]):
					sig1[x] = minhashVals1[xs]
				if(sig2[x] > minhashVals2[xs]):
					sig2[x] = minhashVals2[xs]
				if(sig3[x] > minhashVals3[xs]):
					sig3[x] = minhashVals3[xs]
	print(sig1)
	print(sig2)
	print(sig3)

def fourFourOne():
	nums = [3,1,4,1,5,9,2,6,5]
	hash1 = []
	hash2 = []
	hash3 = []

	for x in nums:
		hash1.append(((2*x)+1)%32)
		hash2.append(((3*x)+7)%32)
		hash3.append((4*x)%32)
	print(hash1)
	print(hash2)
	print(hash3)
	for x in hash3:
		print((format(x, '#010b')))

fourFourOne()