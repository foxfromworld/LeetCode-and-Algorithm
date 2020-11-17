<h3>Finding Counterexamples</h3>

<h4>1-1. </h4>
 
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

<h4>1-2. </h4>

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

<h4>1-3. </h4>

a-c-b: shorter but with a lot of traffic lights

a-d-b: longer but with no traffic lights so you can drive faster

a--x--c--x--x--b                        
a---------D---------b

<h4>1-4. </h4>

a-c-b: shorter but with a lot of traffic
a-d-e-f-b: with a lot of turns but with super light traffic

a----c----b

└d      f┘

  └--e--┘

<h4>1-5. </h4>

S = {1, 2, 5, 9, 10}, T = 22
(a) {1,2,5,9,10} => 1+2+5+9+19 > 22

(b) {1,2,5,9,10} => 1+2+5+9+19 > 22

(c) {10,9,5} => 10+9+5 > 22

<h4>1-6. </h4>

U = {1,2,3,4,5,6}
S1 = {1, 2, 3, 6}, S2 = {2, 4 ,6},  and S3 = {1, 3, 5}

Select the largest: S1 + S2 + S3 (X)

Smallest subset: S2 + S3 (O)

<h3> Proofs of Correctness </h3>

<h4>1-7.</h4> 
y*z = y * ⌊z/c⌋ * c + y * (z mod c)

z = ⌊z/c⌋ *c + (z mod c)

⌊z/c⌋ *c = z - (z mod c)

y*z = y * (z - (z mod c)) + y * (z mod c) = y*c - y (z mod c) + y * (z mod c) = yz

<h4>1-8. </h4>
[Correctness of Horner’s Rule](https://atekihcan.github.io/CLRS/P02-03/ "link") 
[HighFive](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/LeetCode_Solutions/1086HighFive.py "link")
