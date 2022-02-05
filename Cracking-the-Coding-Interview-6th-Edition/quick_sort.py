# Author : foxfromworld
# Date   : 05/02/2022
# Worst-case performance:	O(n**2) 
# Best-case performance: O(nlogn)
# Average performance: O(nlogn)
# Worst-case space complexity: O(n) auxiliary (naive), O(log n) auxiliary
# Stable: No

def quickSort(l, left, right):
    def partition(left, right):
        p_val = l[right] # take the last element as the pivot
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
