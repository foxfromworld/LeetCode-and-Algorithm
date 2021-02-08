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

<h4>3-10.</h4> 

