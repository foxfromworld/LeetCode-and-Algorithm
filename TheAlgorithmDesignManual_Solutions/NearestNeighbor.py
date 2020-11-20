# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 18/11/2020
# Second attempt 

import math
unvisited = [[1,1],[3,1],[2,3],[1,4],[4,4]]
def calc_dist(p1,p2): # Calculate the distance between two points
  return math.sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)
def nearest_neighbor(unvisited):
  p = [4,4]
  route = []
  route.append(p)
  unvisited.remove(p) # Choose one point and set it as visited
  dist = float('inf')
  length = len(unvisited)
  i = 0
  while i < length:
    for num in unvisited: # Start visiting every unvisited point
      dist_temp = calc_dist(p,num)
      if dist >= dist_temp: # Store the shortest distance and point so far
        dist = dist_temp
        p1 = num
    # Finish one round
    p = p1 
    route.append(p) 
    unvisited.remove(p)
    # Reset variables
    dist = float('inf')    
    i+=1
  return route
print(nearest_neighbor(unvisited))
