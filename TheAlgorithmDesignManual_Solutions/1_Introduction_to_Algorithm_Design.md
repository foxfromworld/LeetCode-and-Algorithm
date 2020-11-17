<h3>Finding Counterexamples</h3>

<h4>1-1. Show that a + b can be less than min(a, b). </h4>
 
a + b < a  
=>  b < 0  
=>  a < 0

a + b < b  
=>  a < 0  
=>  b < 0

So when a < 0 and b < 0, a + b < min(a,b)

For example:

-3 + -5 = -8
min(-3,-5) = -5

=> -8 < -5

<h4>1-2. Show that a × b can be less than min(a, b).</h4>

a x b < a

=> a x b - a < 0

=> a x (b-1) < 0

=> a < 0 and b-1 > 0　(b > 1)

=> b > 1 and a < 0

=> a > 0 and b-1 < 0　(b < 1)

=> 0<a<b<1

a x b < b

=> a x b - b < 0

=> b x (a-1) < 0

=> b < 0 and a-1 > 0

=> b > 0 and a-1 < 0

=> ...

<h4>1-3. Design/draw a road network with two points a and b such that the fastest route between a and b is not the shortest route.</h4>

a-c-b: shorter but with a lot of traffic lights

a-d-b: longer but with no traffic lights so you can drive faster

a--x--c--x--x--b                        
a---------D---------b

<h4>1-4. Design/draw a road network with two points a and b such that the shortest route between a and b is not the route with the fewest turns.</h4>

a-c-b: shorter but with a lot of traffic
a-d-e-f-b: with a lot of turns but with super light traffic

a----c----b

└d      f┘

  └--e--┘

<h4>1-5. The knapsack problem is as follows: given a set of integers S = {s1, s2,...,sn}, and a target number T, find a subset of S which adds up exactly to T. For example, there exists a subset within S = {1, 2, 5, 9, 10} that adds up to T = 22 but not
T = 23. Find counterexamples to each of the following algorithms for the knapsack problem. That is, giving an S and T such that the subset is selected using the algorithm does not leave the knapsack completely full, even though such a solution exists.</h4>
　　　<h4>(a) Put the elements of S in the knapsack in left to right order if they fit, i.e. the first-fit algorithm.</h4>
　　　<h4>(b) Put the elements of S in the knapsack from smallest to largest, i.e. the best-fit algorithm.</h4>
　　　<h4>(c) Put the elements of S in the knapsack from largest to smallest.</h4>

S = {1, 2, 5, 9, 10}, T = 22
(a) {1,2,5,9,10} => 1+2+5+9+19 > 22

(b) {1,2,5,9,10} => 1+2+5+9+19 > 22

(c) {10,9,5} => 10+9+5 > 22

<h4>1-6. The set cover problem is as follows: given a set of subsets S1, ..., Sm of the universal set U = {1, ..., n}, find the smallest subset of subsets T ⊂ S such that
∪ti∈T ti = U. For example, there are the following subsets, S1 = {1, 3, 5}, S2 = {2, 4}, S3 = {1, 4}, and S4 = {2, 5} The set cover would then be S1 and S2. Find a counterexample for the following algorithm: Select the largest subset for the cover, and then delete all its elements from the universal set. Repeat by adding the subset containing the largest number of uncovered elements until all are covered.</h4>

U = {1,2,3,4,5,6}
S1 = {1, 2, 3, 6}, S2 = {2, 4 ,6},  and S3 = {1, 3, 5}

Select the largest: S1 + S2 + S3 (X)
Smallest subset: S2 + S3 (O)

<h3> Proofs of Correctness </h3>
<img src="http://chart.googleapis.com/chart?cht=tx&chl=\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" style="border:none;">
