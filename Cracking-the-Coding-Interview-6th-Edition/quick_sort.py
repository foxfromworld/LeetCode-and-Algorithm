# Author : foxfromworld
# Date   : 05/02/2022
# Worst-case performance:	O(n**2) 
# Best-case performance: O(nlogn)
# Average performance: O(nlogn)
# Worst-case space complexity: O(n) auxiliary (naive), O(log n) auxiliary
# Stable: No

# randomly take the element as the pivot
import random
def quickSort(l, left, right):
    def partition(left, right):
        p_val = l[p_idx] # take the last element as the pivot
        l[p_idx], l[right] = l[right], l[p_idx]
        j = left -1
        for i in range(left, right):
            if l[i] <= p_val:
                j = j + 1
                l[j], l[i] = l[i], l[j]
        l[j+1], l[right] = l[right], l[j+1]
        return j + 1
    if left < right:
        p_idx = random.randint(left, right)
        p_idx = partition(left, right)
        quickSort(l, left, p_idx)
        quickSort(l, p_idx + 1, right)

# take the last element as the pivot
def quickSort(l, left, right):
    def partition(left, right):
        p_val = l[right] 
        j = left -1
        for i in range(left, right):
            if l[i] <= p_val:
                j = j + 1
                l[j], l[i] = l[i], l[j]
        l[j+1], l[right] = l[right], l[j+1]
        return j + 1
    if left < right:
        p_idx = partition(left, right)
        quickSort(l, left, p_idx - 1)
        quickSort(l, p_idx + 1, right)
