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
#                                                  Ｏ (3 pointers x 4 bytes + 1 data field x 4bytes)
#                                                 /  \
# (3 pointers X 4 bytes + 1 data field $ 4bytes) Ｏ  Ｏ (3 pointers x 4 bytes + 1 data field x 4bytes)
#                                               / \ / \
#                                              Ｏ ＯＯ Ｏ ...(same)
```
(b)

![image]()
