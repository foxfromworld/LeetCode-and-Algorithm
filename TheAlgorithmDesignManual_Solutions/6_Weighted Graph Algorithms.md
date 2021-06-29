<h3>Simulating Graph Algorithms</h3>

<h4>6-1.</h4> 

![image](https://github.com/foxfromworld/LeetCode-and-Algorithm/blob/main/TheAlgorithmDesignManual_Solutions/Exercise%206-1.jpg)

<h3>Minimum Spanning Trees</h3>

<h4>6-2.</h4> 

In 6-1, path between the two vertices isn't always the shortest. For example, the path between G and H in G1 in (b). However, there is another way to link the tree. You can choose to link "D to G or R to G", or "G to I or G to J" because the weight of the path are the same.

<h4>6-3.</h4> 

For example, in the graph, "A—2—B—3—C—4—A", the minimum spanning tree has a total weight of 5 with edges {A,B},{B,C}; while in the full graph the minimum distance between A and C is 4.

<h4>6-4.</h4> 

If the weights of edges are unique, the result will be the same. If not, in Prim’s algorithm, you can choose a different edge with the same weight; while in Kruskal's algorithm, always the vertex with smaller number is selected first.

<h4>6-5.</h4> 

Yes. They can work with numerical weights.

<h4>6-6.</h4> 

Find the edge with the highest weight and replace it with the new one if the weight of the new one is lower than it.

<h4>6-7.</h4> 

(a) Yes. Because differences between weights are the same. If you sort all weights, they are still in the same order

(b) No. For example, in the graph, "A—(-1)—B—(-1)—C—(-1)—A", the shortest path has a total weight of -2 with edges {A,B},{B,C}. If the weights are increased, like "A—(1)—B—(1)—C—(1)—A". The shortest path will be {A,C}.

<h4>6-8.</h4> 

Find the edge, e, with the largest weighted in the MST and set the non-MST edge value smaller than the e's weight.

<h4>6-9.</h4> 

<h4>6-10.</h4> 

(a) Find the edge where the cycle exists and add the edge into the feedback-edge set.

(b) Find the edge where the cycle exists and add the edge into the feedback-edge set (starts from the edge with the larger weight).

https://algorist.com/problems/Feedback_Edge_Vertex_Set.html

https://www.slideshare.net/AlexandreLewkowicz/slides-46398494

https://en.wikipedia.org/wiki/Feedback_arc_set

<h4>6-11.</h4> 

Use a min heap to keep the weight of edges. Extract one, mark the visited vertex, and add new edges...

<h3>Union-Find</h3>

<h4>6-12.</h4> 

<h4>6-13.</h4> 

<h3>Shortest Paths</h3>

<h4>6-14.</h4> 

http://mathcenter.oxford.emory.edu/site/cs171/dijkstrasShortestPathAlgorithm/

https://en.wikipedia.org/wiki/Shortest_path_problem

<h4>6-15.</h4> 

No. For example, in the graph, "A—(1)—B—(1)—C—(3)—A,C—(1)—D,B—(4)—D", the shortest path from A to D has a total weight of 3 with edges {A,B},{B,C},{C,D}. If the weights are increased by a constant number 9, like "A—(10)—B—(10)—C—(12)—A,C—(10)—D,B—(13)—D". The shortest path will be {A,C},{C,D} woth the total weight, 22.

<h4>6-16.</h4>

(a) "A—(1)—B, B—(1)—C, C—(3)—A, C—(1)—D, B—(4)—D"

(b) "A→(11)→B, B→(11)→C, C←(13)←A, C→(11)→D, B→(14)→D"

(c) Two paths are edge-disjoint if they have no edge in common.

<h4>6-17.</h4> 

<h4>6-18.</h4> 

<h4>6-19.</h4> 

<h4>6-20.</h4> 

<h4>6-21.</h4> 

<h4>6-22.</h4> 

<h4>6-23.</h4> 

<h3>Network Flow and Matching</h3>

<h4>6-24.</h4> 

<h4>6-25.</h4> 
