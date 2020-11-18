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
Correctness of Horner’s Rule

https://atekihcan.github.io/CLRS/P02-03/

<h4>1-9. </h4>

nums = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]

[27, 28, 4, 2, 26, 13, 33, 8, 14, 35]

[27, 4, 2, 26, 13, 28, 8, 14, 33, 35]

[4, 2, 26, 13, 27, 8, 14, 28, 33, 35]

[2, 4, 13, 26, 8, 14, 27, 28, 33, 35]

[2, 4, 13, 8, 14, 26, 27, 28, 33, 35]

[2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

[2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

[2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

[2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

[2, 4, 8, 13, 14, 26, 27, 28, 33, 35]

<h4>1-10.</h4>

 S = (n) + (n-1) + (n-2) + ... + 3 + 2 + 1
 
+S = 1 + 2 + 3 +  ...  + (n-2) + (n-1) + n

---------------------------------------------------

 2S = (n+1) + (n+1) + ... + (n+1) 
 
     |←　 　       n 　     　　→|
     
  S = n*(n+1)/2 

<h4>1-11.</h4>

n = n+1

(n+1)**2 + n(n + 1)(2n + 1)/6 = (n+1)((n+1) + 1)(2(n+1) + 1)/6

<h4>1-12.</h4>

n = n+1

(n+1)**3 + n**2(n + 1)**2/4 = (n+1)**2((n+1) + 1)**2/4

<h4>1-13.</h4>

(n+1)((n+1) + 1)((n+1) + 2) + n(n + 1)(n + 2)(n + 3)/4 = (n + 1)((n + 1) + 1)((n + 1) + 2)((n + 1) + 3)/4

<h4>1-14.</h4>

a**(n+1) + (a**(n+1) - 1)/(a-1) = (a**((n+1)+1) - 1)/(a-1)

<h4>1-15.</h4>

1/(n+1)((n+1)+1) + n/(n+1) = (n+1)/((n+1)+1)

<h4>1-16.</h4>

(n**3 + 2n) = 3a

((n+1)**3 + 2(n+1)) = 3b

3b - 3a = 3(b-a) = n**2 + n + 1 (integer)

<h4>1-17.</h4>

E(n) = n-1

E(n+1) = n + 1 - 1 = E(n) + 1 = n - 1 + 1 = n

<h4>1-18. </h4>

https://en.wikipedia.org/wiki/Squared_triangular_number

<h4>1-19.</h4>

My books: 100 books * 500 pages = 50000 pages = 0.5 million pages

School library: 1000000 books * 500 pages = 500 million pages

<h4>1-20.</h4>

~50*40 (per page) * 700 pages

<h4>1-21. </h4>

1 hour = 3600 seconds

1000/3.6 => (1000/3 + 1000/4)/2 => (333+250)/2 ~290 hours

24hours/day => 240*10 + 24*2 => 12 days

<h4>1-22.</h4>

50*400 = 20000...? Sorry...really no idea!

<h4>1-23. </h4>

Depth: 0.02 mile

Width: 1 mile

Flow velocity: 10 miles/hour

0.02 * 1 * 10 * 24 = 4.8 cubic miles of water/day

<h4>1-24.</h4>

Disk drive access time is normally measured in milliseconds: http://db.cs.duke.edu/courses/cps104/fall98/lectures/week14-l1/tsld012.htm

The RAM memory accesses a word in less than a microsecond: "Fast RAM chips have an access time of 10 nanoseconds (ns) or less"

=>A microsecond is equal to 1000 nanoseconds. So the anser is less.

Instructions that a CPU can execute in one year: 
 
For example: i7 3 GHz (3,000,000,000 cycles/sec)


    1,000,000,000 billion
    
1,000,000,000,000 trillion

300 trillion * 3.65 * 24 *3.6 ~ 67500 trillion... 

<h4>1-25.</h4>

(a) a = 1000**2 = 1000000 ; b = 10000**2 = 100000000 ; b/a = 100 seconds

(b) a = 1000*log2(1000) ; b = 10000*log2(10000) ; b/a ~ 10*(13.2877/9.96578) ~13.33 seconds

<h3>Implementation Projects</h3>

<h4>1-26.</h4>

Nearest Neighbor

https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/NearestNeighbor.py

Closest Pair (Not exactly finished)

https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/ClosestPair.py

Both are not true in all examples

Can you devise a heuristic that works better than both of them?

Obviously, this is why I need to learn! Of course I cannot come up with the answer right now...(I'll come back to this later)

Some interesting examples: https://jupyter.brynmawr.edu/services/public/dblank/jupyter.cs/FLAIRS-2015/TSPv3.ipynb

<h4>1-27.</h4>

https://blog.wakatta.jp/blog/2012/02/10/psychic-modeling/

https://mikkqu.com/notes/psychic-modeling/

<h3>Interview Problems</h3>

<h4>1-28.</h4>

https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/PerformIntegerDivisionWithoutUsingOperators.py

<h4>1-29.</h4>

            5 races
     ┌  A1 A2 A3 A4 A5 - Assume A1 is the fastest (discard A4 and A5) 
     
     │  B1 B2 B3 B4 B5 - Assume B1 is the fastest (discard B4 and B5) 
     
25   │  C1 C2 C3 C4 C5 - Assume C1 is the fastest (discard C4 and C5)  —　A1 B1 C1 D1 E1 － Assume A1 is the fastest 

     │  D1 D2 D3 D4 D5 - Assume D2 is the fastest (discard D4 and D5) 
     
     └  E1 E2 E3 E4 E5 - Assume E1 is the fastest (discard E4 and E5) 

<h4>1-30.</h4>


<h4>1-31.</h4>


<h4>1-32.</h4>


<h4>1-33</h4>


<h4>1-34</h4>


<h3>Programming Challenges</h3>

<h4>1-1</h4>


<h4>1-2</h4>


<h4>1-3</h4>

