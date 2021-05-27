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

    4
   / \
  2   6
 / \ / \
1  3 5  7
preorder: 4213657
inorder: 1234567
postorder: 1325764

<h4>5-8.</h4> 


