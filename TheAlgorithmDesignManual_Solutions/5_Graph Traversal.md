<h3>Simulating Graph Algorithms</h3>

<h4>5-1.</h4> 

(a) BFS

G1: A B D I C E G J F H

G2: A B E C F I D G J M H K N L O P

(b) DFS

G1: A B C E D G H F J I

G2: A B C D H G F E I J K L P O N M

<h4>5-2.</h4> 

According  to the errata, the direction between F and H should be reversed.

BFS:

A in 0; H in 0; B in 1: A; C in 2: B, E; D in 2: A, B; E in 2: B, D; F in 4: C, E, G, H; G in 3: D, E, H; I in 1: G; J in 1: I

DFS: A: [B, D]; D: [E, G]; E: [C, F, G]; C: [F]; B: [C, E]; G: [I]; I: [J]; H: [F, G, J]

Result: H A B D E G I J C F

<h3>Traversal</h3>

<h4>5-3.</h4> 

The tree contains nodes and leaves. Child nodes can only be accessed through the same parent. So the path is unique.

<h4>5-4.</h4> 

In a breadth-first search on a undirected graph G, every edge is either a tree edge or a cross edge. For example, in 5-1 G1. You can see the edges between A, B and A, D are tree edges and the edge between B and D is a cross edge. These edges are interchangeable.

<h4>5-5.</h4> 

No.

Definition of the bipartite graph: https://en.wikipedia.org/wiki/Bipartite_graph

<h4>5-6.</h4> 

(a) The node v is directly connected to all n nodes.

(b) The node v is connected to a chain of linked n nodes.

(c) The node v is connected to two chains which have the length of n/2

<h4>5-7.</h4> 

```python
    4
   / \
  2   6
 / \ / \
1  3 5  7
```

preorder: 4213657

inorder: 1234567

postorder: 1325764

It is possible to reconstruct the tree using the pre-order and in-order traversals of the binary tree.

1. Use preorder to indentify the root node and find the left subtree and right subtree using the root node in the inorder traversal.

2. Repeat 1

Not possible the pre-order and post-order traversals.

<h4>5-8.</h4> 

adjacency matrix -> weight matrix relateion between vertices

https://en.wikipedia.org/wiki/Adjacency_matrix

adjacency list -> the set of neighbors

https://en.wikipedia.org/wiki/Adjacency_list

incidence matrix -> relation between vertices and edges (direction and connection)

https://en.wikipedia.org/wiki/Incidence_matrix

Ex:

  a b c d
  
a 0 1 1 0

b 1 0 0 1

b 1 0 0 1

c 0 1 1 0

1. adjacency matrix to adjacency lists

Check each row from a to d and find the value 1

a: b, c; b: a, d: c: a, d; d: c, b

2. adjacency list to an incidence matrix

  e1 e2 e3 e4

a  1  1  0  0 

b  1  0  1  0

c  0  1  0  1

d  0  0  1  1

Find the edges and fill the vertex in.

3. incidence matrix to adjacency lists

Go throuh the edges and find the paired vertices and fill in the list.

<h4>5-9.</h4> 

Time complexity: O(n) 

Recursive

https://www.geeksforgeeks.org/evaluation-of-expression-tree/

```python
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def eval_tree(node):
    if not node: return 0
    if not node.left and not node.right: return int(node.data)
    left_num = eval_tree(node.left)
    right_num = eval_tree(node.right)
    if node.data == '+': return left_num + right_num
    elif node.data == '-': return left_num - right_num
    elif node.data == '*': return left_num * right_num
    else: return left_num / right_num
    
root = node('+')
root.left = node('/')
root.left.left = node('*')
root.left.left.left = node('3')
root.left.left.right = node('4')
root.left.right = node('5')
root.right = node('+')
root.right.left = node('2')
root.right.right = node('*')
root.right.right.left = node('3')
root.right.right.right = node('4')   
```

<h4>5-10.</h4> 

Same as 5-9

```python
root = node('+')
root.left = node('+')
root.left.left = node('2')
root.right = node('/')
root.left.right = root.right.left = node('*')
root.right.right = node('5')
root.left.right.left = node('3')
root.left.right.right = node('4')
```

<h4>5-31.</h4> 

https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/

BFS: queue

DFS: stack 

<h4>5-32.</h4> 

https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/LeetCode_Solutions/230.%20Kth%20Smallest%20Element%20in%20a%20BST.py
