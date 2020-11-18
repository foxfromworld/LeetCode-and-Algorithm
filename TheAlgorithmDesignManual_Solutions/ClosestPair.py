import math
nums = [[10,0],[11,0],[0,0],[8,0],[15,0]]

def calc_dist(p1,p2):
  return math.sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)
def closest_pair(nums):
  connected = []
  new_list = nums.copy() # Copy a nums. Don't use new_list = nums!
  dist = float('inf')
  for i in range(len(nums)):
    new_list.pop(i)
    for j in range(len(new_list)): # Find closest pairs
      dist_temp = calc_dist(nums[i],new_list[j]) 
      if dist > dist_temp:
        dist = dist_temp
        p = new_list[j]
    connected.append([nums[i],p])
    new_list = nums.copy()
    dist = float('inf')
  return connected
print(closest_pair(nums))  
