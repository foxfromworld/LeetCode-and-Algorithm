<h3>Stacks, Queues, and Lists</h3>

<h4>3-1.</h4> 

| #	| Title	| 
| --- | --- | 
| 20 | [Valid Parentheses](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/LeetCode_Solutions/20.%20Valid%20Parentheses.py "link") |

<h4>3-2.</h4> 

| #	| Title	| 
| --- | --- | 
| 206 | [Reverse Linked List](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/LeetCode_Solutions/206.%20Reverse%20Linked%20List.py "link") | 

<h4>3-3.</h4> 

(a) Consider an underflow strategy that cuts the array size in half whenever the array falls below half full. Give an example sequence of insertions and deletions where this strategy gives a bad amortized cost.

--> When cutting the array size in half can never happen. Ex: size 4 array with 3 elements. Remove 1, insert 1, and so on.

(b) Then, give a better underflow strategy than that suggested above, one that achieves constant amortized cost per deletion. 

--> Ex: when the size 4 array is one-fourth full, cut its size in half, and so on.

<h3>Trees and Other Dictionary Structures</h3>

<h4>3-4.</h4> 

https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/

Use the hash map to memorise the index of a value. When you add a new value, append it and memorise the lennght-1 as the index. When you remove the value, get the key using get() function. Delete the key in the hash map, swap the value and the last value and delete the value in the list. 

<h4>3-5.</h4> 

```python
#                                                  Ｏ (3 pointers x 4 bytes + 1 data field x 4bytes)
#                                                 /  \
# (3 pointers X 4 bytes + 1 data field $ 4bytes) Ｏ  Ｏ (3 pointers x 4 bytes + 1 data field x 4bytes)
#                                               / \ / \
#                                              Ｏ ＯＯ Ｏ ...(same)
```
(a) nx1x4/(nx1x4+nx3x4) = 1/4

```python
#                                                  Ｏ        ┐
#                                                 /  \       │
#                                                Ｏ  Ｏ　　　 ├─ n-1 internal nodes (2 pointers x 2bytes)
#                                               / \ / \      ┘
#                                              Ｏ ＯＯ Ｏ    ──  n leave nodes (1 data field x 4bytes)
```
(b) nx1x4/(nx1x4+(n-1)x2x2) = n/(2n-1) if n->∞ then 1/2

<h4>3-６.</h4> 

Use a double-linked list to access the predecessor and the successor

```python
#    Ｏ predecessor
#   /  \↖
#  Ｏ  Ｏ
#  / \ / \↘      
# Ｏ ＯＯ Ｏ successor
```

<h4>3-7.</h4> 

Sounds like a tree structure

1. Keep the value of the min and max value and update them at deletion or insertion

2. Use the doubly-linked list so the beginning and end node will be min and max repectively

3. Use max/min heap

Reference: https://github.com/abdulapopoola/TADMBook/blob/master/Chapter%203/3.07.md

<h4>3-8.</h4> 

"All operations must take O(log n) time on an n-element set." A self-balancing binary search tree will do. (Binary search tree has its limit with the worst case complexity of O(n) https://en.wikipedia.org/wiki/Binary_search_tree)

https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree

Some examples of the self-balancing binary search tree:

https://en.wikipedia.org/wiki/AVL_tree (https://www.programiz.com/dsa/avl-tree#code)

https://en.wikipedia.org/wiki/Red%E2%80%93black_tree (https://www.programiz.com/dsa/red-black-tree)

http://www.btechsmartclass.com/data_structures/red-black-trees.html

https://www.youtube.com/watch?v=5IBxA-bZZH8

My notes:

![image](https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/TheAlgorithmDesignManual_Solutions/AVL%20Tree1.jpg)

![image](https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/TheAlgorithmDesignManual_Solutions/AVL%20Tree2.jpg)

![image](https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/TheAlgorithmDesignManual_Solutions/Red-black%20Tree.jpg)

<h4>3-9.</h4> 

```Python
#    (S1)                     (S2)
#     2                        5
#    /  \                     /  \
#   1    3                   4    6
#               (Solution 1)                                        (Solution2 - more balanced)
#                      5                                            4 (min in S2)           3 (max in S1)
#                     / \                                          / \                    /   \  
# (smallest child)   4   6                                        2    5          or     2     5
#                  /                                            / \     \               /     / \
#                 2                                            1  3      6             1     4   6
#                / \
#               1  3 
#
#
#
```
<h3>Applications of Tree Structures</h3>

<h4>3-10.</h4> 

*Best-fit

Use a binary search tree. 

1. Start with the full capacity at the beginning

2. Find the right bin (enough capacity) for the item

3. Find the bin and remove the respective node

4. Minus the weigh and re-insert the node

5. Repeat 2-4

Or use a self-balancing tree?

*Worst-fit

Always choose the node with the least space

<h4>3-11.</h4> 

(a) Create a table to store every smallest value corresponging to the (i, j) combination 

(b) Use the a Cartesian tree https://www.youtube.com/watch?v=2R1vV00SQ6g

<h4>3-12.</h4> 

1. Input the S. If it returns False, it means S doesn't contain any subset that adds up to k.

2. Remove elements one by one to check if the element is necessary to add up k. If it still returns True after removing the element then that means the element is not necessary.

3. After checking all elemnets, you will get the right subset.

<h4>3-13.</h4> 

![image](https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/TheAlgorithmDesignManual_Solutions/Excercises%203-13.jpg)

<h4>3-14.</h4> 

Similiar to 3-13.

Add(k,y): find the node and add value "y" to every node on the path to the node

Insert(k,y): find the place to insert the node, balance the tree, and update the values of the nodes

Delete(k): find the node and subtract the value "y" from every node on the path to the node

Partial-sum(k): "With the left sub tree sum values stored in the nodes this operation only involves searching for the element with the specified key, and summing sub tree sums along the way."

https://www.algorist.com/algowiki/index.php/3.29

<h3>Applications of Tree Structures</h3>

<h4>3-15.</h4> 
Important elements:

1. counter, occurance

2. A: to keep the counter

3. B: to keep the value

ADD

c = c+1

A[X] = c

B[c] = X

Delete ==> A[B[c]] = A[X];  B[A[X]] = B[c]; c = c-1;

<h3>Implementation Projects</h3>

<h4>3-17.</h4> 

https://en.wikipedia.org/wiki/Caesar_cipher

Since there are only a limited number of possible shifts (25 in English), they can each be tested in turn in a brute force attack.

<h3>Interview Problems</h3>

<h4>3-18.</h4> 

Sorted Binary Search Tree

<h4>3-19.</h4> 

Sort shirts by colour and do sub-class sorting 

<h4>3-20.</h4> 

https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/LeetCode_Solutions/876.%20Middle%20of%20the%20Linked%20List.py

<h4>3-21.</h4> 

This is very similiar this symmietric tree problem

Just change the comparison from "left.left vs. right.right" and "left.right vs. right.left" to "left.left vs. right.left" and "left.right vs. right.right" considering one tree as left sub-tree and the other as the right sub-tree

https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/LeetCode_Solutions/101.%20Symmetric%20Tree.py

<h4>3-22.</h4> 



<h4>3-23.</h4> 



<h4>3-24.</h4> 



<h4>3-25.</h4> 



<h4>3-26.</h4> 

<h4>3-27.</h4> 

<h4>3-28.</h4> 

<h4>3-29.</h4> 

