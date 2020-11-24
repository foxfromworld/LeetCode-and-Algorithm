# Author : foxfromworld
# Date   : 23/11/2020
# O(nm)

t = "aababba" # len = 7
p = "abba" # len = 4

t = "ababca" # len = 6
p = "abc" # len = 3

def string_pattern_matching_original(t,p):
  for i in range(len(t)-len(p)+1): # pointer of the beginning of the string to be compared with
    j = 0
    while j<len(p) and t[i+j] == p[j]: # check character one by one with p
      j+=1
    if j == len(p): return i
  return -1

def string_pattern_matching(t,p):
  for i in range(len(t)-len(p)+1):
    j = 0
    if t[i+j:i+j+len(p)] == p: # compare the string using Python's syntax
      return i
  return -1  

print(string_pattern_matching_original(t,p))
