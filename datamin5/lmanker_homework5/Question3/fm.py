#Lucas Manker
#part 3

import hashlib
import multiprocessing
import queue
import concurrent.futures
import math
import statistics
import mmh3
import fnv

def fnvHash(file):
    total = 0
    count = 0
    q = 0
    with open(file, "r",encoding='utf-8') as f:
        for line in f:
            if(line[0] == 'Q'):
                q += 1
                x = fnv.hash(line.encode(), algorithm=fnv.fnv_1a, bits=64)
                binVal = str(format(x, '#010b'))
                binVal = binVal.replace('0b', "")
                binVal = binVal.split('1')
                if(binVal[-1] != '') : 
                    total += pow(2,len(binVal[-1]))
                count += 1
    return ([total, count])

def mmh3Hash(file):
    total = 0
    count = 0
    with open(file, "r",encoding='utf-8') as f:
        for line in f:
            if(line[0] == 'Q'):
                x = mmh3.hash(line, signed=False)
                binVal = str(format(x, '#010b'))
                binVal = binVal.replace('0b', "")
                binVal = binVal.split('1')
                if(binVal[-1] != '') : 
                    total += pow(2,len(binVal[-1]))
                count += 1
    return ([total, count])

def fnv1Hash(file):
    total = 0
    count = 0
    with open(file, "r",encoding='utf-8') as f:
        for line in f:
            if(line[0] == 'Q'):
                x = fnv.hash(line.encode(), algorithm=fnv.fnv, bits=64)
                binVal = str(format(x, '#010b'))
                binVal = binVal.replace('0b', "")
                binVal = binVal.split('1')
                if(binVal[-1] != '') : 
                    total += pow(2,len(binVal[-1]))
                count += 1
    return ([total, count])

def sendToExecutor(funcName, tasks):
    returnVals = []
    with concurrent.futures.ThreadPoolExecutor(max_workers = 9) as executor:
        future_to_r = {executor.submit(funcName, names): names for names in tasks}
        for future in concurrent.futures.as_completed(future_to_r):
            result = future_to_r[future]
            data = future.result()
            returnVals.append(data)
        count = 0
        total = 0
        for x in returnVals:
            total += x[0]
            count += x[1]
        return (total/count)



tasks =  ["quotes_2009-01.txt","quotes_2009-02.txt","quotes_2009-03.txt",
          "quotes_2009-04.txt","quotes_2008-08.txt","quotes_2008-09.txt",
          "quotes_2008-10.txt","quotes_2008-11.txt","quotes_2008-12.txt",]

fnvAvgs = sendToExecutor(fnvHash, tasks)
print(fnvAvgs)
mmh3Avgs = sendToExecutor(mmh3Hash, tasks)
print(mmh3Avgs)
fnv1Avgs = sendToExecutor(fnv1Hash, tasks)
print(fnv1Avgs)
print(statistics.median([md5Avgs, sha1Avgs, sha512Avgs]))
