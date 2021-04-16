<h3>Applications of Sorting</h3>

<h4>4-1.</h4> 

For example, use merge sort and split the list in halves.

<h4>4-2.</h4> 

(a) Go through the list and find the max and min at the same time. At the end, get the value of |max-min|.

(b) Find the difference of the first and the last element.

(c) For example, sort the list using heap sort and check the difference by going through the list to find the min value with. 

(d) Use the (c) method (without sorting), the time complexity becomes O(n).

<h4>4-3.</h4> 

Sort the list with quicksort. And get the last and the first as a pair. Contiune this operation until it becomes a list of n pairs.

<h4>4-4.</h4> 

Go through the list and take red, blue, yellow items out, then put them into respective buckets. Lastly, append those items back together following the sequence: red, blue, yellow.

<h4>4-5.</h4> 

1. Sort the list with O(nlogn) sorting algorithm and go through the list to find the mode.

2. Use the dictionary to count.

<h4>4-6.</h4> 

1. Sort S1 O(nlogn)

2. Go through S2 and calculate the difference of S2[i] and x.

  2-1. Do the Binary search n times to find if it's in S1 (logn)

O(nlogn) + O(nlogn) -> O(nlogn)

<h4>4-7.</h4> 

All can be done by using hash maps, O(n) or sorting algorithms, O(nlogn). Do the counting by go through the list.

<h4>4-8.</h4> 

(a) Sort the list and find the x-S[i] using binary search.

(b) Create a list to keep the difference of x with every element of S and go through S to check if it exists.

<h4>4-9.</h4> 

(a) Sort A and B then merge them using the method of (b)

(b) Use a union list to keep the union numbers. set 3 indexes for A, B, union (i, j, k) to find the number to add into the union. 

    1. A[i] = B[j] -> U[k] = A[i]; i++; j++; k++
   
    2. A[i] < B[j] -> U[k] = A[i]; i++; k++

    3. A[i] > B[j] -> U[k] = B[j]; j++; k++

<h4>4-10.</h4> 

Use k-1 loops and then use binary search to find the (T-loop1value-loop2value..)

<h4>4-11.</h4> 

Use a dictionary to do the counting

<h3>Heaps</h3>

<h4>4-12.</h4> 

Create a heap with the min value on the top using O(n) and extract the kth smallest item using O(klogn) time.

Similiar to:

| #	| Title	| 
| --- | --- |
| 215 | [Kth Largest Element in an Array](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/LeetCode_Solutions/215.%20Kth%20Largest%20Element%20in%20an%20Array.py "link") | 

<h4>4-13.</h4> 

(a) A max-heap VS sorted array -> O(1) to get the max value "draw"

(b) A max-heap -> O(logn) to delete; asorted aray -> O(n) "max-heap wins"

(c) Build up a max-heap -> O(nlogn); Sort an array -> O(nlogn) "draw"

(d) Finding the min value for a max-heap takes O(n) time; O(1) for a sorted array "sorted array" wins

<h4>4-14.</h4> 

1. Take the first element of each sorted list and build a min-heap using these elemnts. O(klogk)

2. Put the min value into the merged list and delete it from the heap. Take the first element from the sorted list where the last first element was deleted into the min-heap. O(logk)

3. Repeat for n times. O(nlogk)

<h4>4-15.</h4> 

Use the heap sort to find the second-largest and the third-largest key.

<h3>Quicksort</h3>

<h4>4-16.</h4> 

We need to find the kth largest element which means k = n/2

First select one pivot and divide the list into two arrays. Check the length of the list. 

 smaller |p| larger

1 - k-1  |p| (k+1) - n

If the length of smaller equals to k -1 then the p is the kth element. If not, keep divide the smaller/larger array until the condition is satisified.

<h4>4-17.</h4> 

(a) O(logn) comparisons x n times => O(nlogn) run time

(b) O(log base3/2 (n)) x n times => O(logn/log(3/2)) x n ~= O(logn/0.58496250072) x n ~= O(1.709511291354834xlogn)xn

<h4>4-18.</h4> 

Go through the list and use three pointers to keep the position of the first red, white, and blue items. Swap all the red from left to right first and check blue from right to left.

<h4>4-19.</h4> 

(a) The permutation has (n-1) + (n-2) + (n-3) + ... + (n - n) inversions 

2S = (n-1 + n-(n-1)) + ... + (n-(n-1) + (n-1)) = (n-1) x n /2

(b) P: x inversions -> Pr: (n-1)n/2 - x; total inversions: x + (n-1)n/2 - x = (n-1)n/2

(c) (n-1)n/2 x 1/2 possibility = (n-1)n/4

<h4>4-20.</h4> 

Use 0 use the pivot point => "larger than or equals to  0": right side, "less than 0": left side

<h3>Other Sorting Algorithms</h3>

<h4>4-21.</h4> 

Settle the ties by choosing the item with a lower index value

<h4>4-22.</h4> 

Create a heap with k elements (1-k). Go through the heap (O(logk)) n times  and the count will be counted each time. -> O(nlogk)

<h4>4-23.</h4> 

Similiar to 4-22. Use a balanced tree and k = logn. Insert the element or increase the count accordingly.

<h4>4-24.</h4> 

The square root of n -> sqrt(n)

Sort the unsorted array with O(sqrt(n)log(sqrt(n))) and merge the two lists with O(n) + O(sqrt(n)log(sqrt(n))) -> O(n)

<h4>4-25.</h4> 

Create a heap and go through it and increase the count accordingly. This takes O(n x log(log log n))

<h4>4-26.</h4> 



<h4>4-27.</h4> 



<h3>Lower Bounds</h3>

<h4>4-28.</h4> 



<h4>4-29.</h4> 

The lower bound O(nlogn) applies to only all comparison based sorting algorithms, with no assumptions on the values of the elements. It is possible to do faster than n log n if we make assumptions on the values. We can use the decision tree to prove it. It's not possible to just insert n numbers and extract and then extract the max value.

<h3>Searching</h3>

<h4>4-30.</h4> 

The time complexity of binary search is O(logn) so 10,000 sorted names -> log(10000) = 13.2877123795

Worst case: log(4000) + log(6000) = 11.9657842847 + 12.5507467854 

So the option 1 is better and there is no difference for the linear search.

<h4>4-31.</h4> 

<h4>4-32.</h4> 

<h4>4-33.</h4> 

<h4>4-34.</h4> 

<h4>4-35.</h4> 

<h3>Implementation Challenges</h3>

<h4>4-36.</h4> 

<h4>4-37.</h4> 

<h4>4-38.</h4> 

<h4>4-39.</h4> 

<h3>Interview Problems</h3>

<h4>4-40.</h4> 

<h4>4-41.</h4> 

<h4>4-42.</h4> 

<h4>4-43.</h4> 

<h4>4-44.</h4> 

<h4>4-45.</h4> 

<h4>4-46.</h4> 
