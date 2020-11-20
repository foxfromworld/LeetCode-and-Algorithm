# Author : foxfromworld
# Date  : 20/11/2020
# Second attempt 

import collections
def Three_n_PlusOne(i,j):
  cache = collections.defaultdict() # use this to memorise lifeCycle of calculated numbers
  length = float('-inf') 
  cache[1] = 4 # when n is 1
  cache[2] = 2 # when n is 2
  for k in range(3,j+1): # calcuate the lifeCycle of this number
    n = k
    listCycle = []
    listCycle.append(n)
    while n not in cache :
      if n%2 == 0:
        n//=2
      else:
        n = n*3+1
      listCycle.append(n)
    val = cache[listCycle.pop()] # If the val is in the dictionary, the following while loop will not be executed
    while len(listCycle)>0:
      val+=1
      cache[listCycle.pop()] = val
  for x in range(i,j+1): # find the max lifeCycle
    length_temp = cache[x]
    if length_temp>length:
      length = length_temp 
  return length
i, j = 1, 10 # output: 20
i, j = 100, 200 # output: 125
i, j = 201, 210 # output: 89
i, j = 900, 1000 # output: 174
print(Three_n_PlusOne(i,j))
