import random
import sys

k = 20

w = 300
numFlows = 0
max31 = (2 ** 32) - 1

# sys.stdout  =  open("CounterSketchPython.txt","w")

hashes=[]
for i in range(k):
  hashes.append(random.randint(1, sys.maxsize))
counters=[[0 for _ in range(w)] for __ in range(k)]

f = open("project3input.txt","r")


flag = True

ipMap = []
randomValSet = set()
ips = {}
for line in f:
  if flag == True:
    numFlows = int(line)
    flag = False
  else:
    line = line.split()
    if line[0] not in ips:
      someRandom = random.randint(0, max31)
      while (someRandom in randomValSet):
        someRandom = random.randint(0, max31)
      ips[line[0]] = someRandom
      ipMap.append([line[0], someRandom, int(line[1])])
    else:
      someRandom = ips[line[0]]
    for c in range(k):
      hash = someRandom ^ hashes[c]
      location = hash % w
      if (hash >> 31) & 1 == 1:
        counters[c][location] -= int(line[1])
      else:
        counters[c][location] += int(line[1])


error = 0
for ip in ipMap:
  expected = []
  for c in range(k):
    hash = ip[1] ^ hashes[c]
    location = hash % w
    if (hash >> 31) & 1 == 1:
      expected.append(-counters[c][location])
    else:
      expected.append(counters[c][location])
  expected.sort()
  median = 0
  if len(expected) % 2 == 0:
    median = (expected[int(len(expected) / 2) - 1] + expected[int(len(expected) / 2)] ) / 2
  else:
    median = expected[int(len(expected) / 2)]
  error += abs(median - ip[2])
  ip.append(expected[1])
  
  

print(int(error / len(ipMap)) )
# ipMap.sort(key = lambda x: -x[3])
# for i in range(100):
#   print(ipMap[i][0], ipMap[i][3], ipMap[i][2])

# sys.stdout.close()