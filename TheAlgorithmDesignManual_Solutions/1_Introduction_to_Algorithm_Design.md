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

<h4>1-2.  Show that $ a \times b $ can be less than $ \min(a,b) $.</h4>

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

<h4>1-4. Design/draw a road network with two points $ a $ and $ b $ such that the shortest route between $ a $ and $ b $ is not the route with the fewest turns.</h4>

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

<h4>1-8. Prove the correctness of the following algorithm for evaluating a polynomial. P(x) = $ a_nx^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0 $</h4>
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

<h4>1-10. Prove that $ \sum_{i=1}^n i $=$ n(n+1)/2 $ for $ n \geq 0 $, by induction.</h4>

 S = (n) + (n-1) + (n-2) + ... + 3 + 2 + 1
 
+S = 1 + 2 + 3 +  ...  + (n-2) + (n-1) + n

---------------------------------------------------

 2S = (n+1) + (n+1) + ... + (n+1) 
 
     |←　 　       n 　     　　→|
     
  S = n*(n+1)/2 

<h4>1-11.</h4>

n = n+1

(n+1)**2 + n(n + 1)(2n + 1)/6 = (n+1)((n+1) + 1)(2(n+1) + 1)/6

<h4>1-12. Prove that $ \sum_{i=1}^n i^3 $=$ n^2(n+1)^2/4 $ for $ n \geq 0 $, by induction.</h4>

n = n+1

(n+1)**3 + n**2(n + 1)**2/4 = (n+1)**2((n+1) + 1)**2/4

<h4>1-13.</h4>

(n+1)((n+1) + 1)((n+1) + 2) + n(n + 1)(n + 2)(n + 3)/4 = (n + 1)((n + 1) + 1)((n + 1) + 2)((n + 1) + 3)/4

<h4>1-14. Prove by induction on $ n \geq 1 $ that for every $ a \neq 1 $, $ \sum_{i=0}^n a^i =\frac{a^{n+1}-1}{a-1} $ }</h4>

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

<h4>1-19. Do all the books you own total at least one million pages? How many total pages are stored in your school library? Schaffer, chapter 2 problem 2.21</h4>

My books: 100 books * 500 pages = 50000 pages = 0.5 million pages

School library: 1000000 books * 500 pages = 500 million pages

<h4>1-20. How many words are there in this textbook?</h4>

~50*40 (per page) * 700 pages

<h4>1-21. </h4>

1 hour = 3600 seconds

1000/3.6 => (1000/3 + 1000/4)/2 => (333+250)/2 ~290 hours

24hours/day => 240*10 + 24*2 => 12 days

<h4>1-22. Estimate how many cities and towns there are in the United States.</h4>

50*400 = 20000...? Sorry...really no idea!

<h4>1-23. </h4>

Depth: 0.02 mile

Width: 1 mile

Flow velocity: 10 miles/hour

0.02 * 1 * 10 * 24 = 4.8 cubic miles of water/day

<h4>1-24. Is disk drive access time normally measured in milliseconds (thousandths of a second) or microseconds (millionths of a second)? Does your RAM memory access a word in more or less than a microsecond? How many instructions can your CPU execute in one year if the machine is left running all the time?</h4>

Disk drive access time is normally measured in milliseconds: http://db.cs.duke.edu/courses/cps104/fall98/lectures/week14-l1/tsld012.htm

The RAM memory accesses a word in less than a microsecond: "Fast RAM chips have an access time of 10 nanoseconds (ns) or less"

=>A microsecond is equal to 1000 nanoseconds. So the anser is less.

Instructions that a CPU can execute in one year: 
 
For example: i7 3 GHz (3,000,000,000 cycles/sec)


    1,000,000,000 billion
    
1,000,000,000,000 trillion

300 trillion * 3.65 * 24 *3.6 ~ 67500 trillion... 

<h4>1-25.</h4>

(a) a = (1000) ** 2 = 1000000 ; b = (10000) ** 2 = 100000000 ; b/a = 100 seconds

(b) a = 1000*log2(1000) ; b = 10000*log2(10000) ; b/a ~ 10*(13.2877/9.96578) ~13.33 seconds

<h3>Implementation Projects</h3>

<h4>1-26. Implement the two TSP heuristics of tsp-robot. Which of them gives better-quality solutions in practice? Can you devise a heuristic that works better than both of them?</h4>

Nearest Neighbor

https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/NearestNeighbor.py

Closest Pair (Not exactly finished)

https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/ClosestPair.py

Both are not true in all examples

Can you devise a heuristic that works better than both of them?

Obviously, this is why I need to learn! Of course I cannot come up with the answer right now...(I'll come back to this later)

Some interesting examples: https://jupyter.brynmawr.edu/services/public/dblank/jupyter.cs/FLAIRS-2015/TSPv3.ipynb

<h4>1-27. Describe how to test whether a given set of tickets establishes sufficient coverage in the Lotto problem of lotto. Write a program to find good ticket sets.</h4>

https://blog.wakatta.jp/blog/2012/02/10/psychic-modeling/

https://mikkqu.com/notes/psychic-modeling/

<h3>Interview Problems</h3>

<h4>1-28.</h4>

https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/PerformIntegerDivisionWithoutUsingOperators.py

<h4>1-29.</h4>

            5 races
     ┌  A1 A2 A3 A4 A5 - Assume A1 is the fastest (discard A4 and A5) 
     
     │  B1 B2 B3 B4 B5 - Assume B1 is the fastest (discard B4 and B5)          +1 race
     
25   │  C1 C2 C3 C4 C5 - Assume C1 is the fastest (discard C4 and C5)  —　A1 B1 C1 D1 E1 － Assume A1 is the fastest (discard C3, D group, and E group)

     │  D1 D2 D3 D4 D5 - Assume D2 is the fastest (discard D4 and D5) 
     
     └  E1 E2 E3 E4 E5 - Assume E1 is the fastest (discard E4 and E5) 

       +1 race
 
=> A2, A3, B1, B2, C1 => Totally 7 races

<h4>1-30. How many piano tuners are there in the entire world?</h4>

World population ~7,800,000,000 (7.8 billion = 7800 million)

Guess: 1 piano/100 people => 78 million pianos

<h4>1-31.</h4>

168000

https://www.fueleconomy.gov/feg/quizzes/answerquiz16.shtml

Population in U.S. : 3.3/10 billion

Assume the half of citizens own a car ~ 0.1 billion people

Assume that a gas station opens 12 hours a day and serves 50 customers in one hour

Cars need to refuel once in a week.

100000000/7*12*10 = 10000000/7*12 ~ 10000000/85 ~ 2000000/17 ~ (2000000/15 + 2000000/20)/2 ~ (400000/3 + 100000)/2 ~ (133333 + 100000)/2 ~ (233333)/2 ~ 120000

<h4>1-32. How much does the ice in a hockey rink weigh?</h4>

Size of the rink

The density of ice ~ 0.9 g/cm3

60 m (length) * 30 m (width) * 0.75*2.5*1/100 m (thickness) => 33000 kg

<h4>1-33</h4>

https://www.artba.org/about/faq/

1 km ~ 0.621 miles

Area of US: 9,834,000 km2 ~ 10,000,000 km2 ~ 5000km *2000km 

=> 3 road /1 km => 1700 roads (horizontal) and 600 roads (vertical)

(1700*2000km+600*5000)*0.621 => 3960000 miles

<h4>1-34. On average, how many times would you have to flip open the Manhattan phone book at random in order to find a specific name?</h4>

https://math.stackexchange.com/questions/1780476/manhattan-phone-book

Assume the phone book has 1,000 pages. => 500 openins. Set the probability as 5%

Suppose you will not revisit the same page: 

pn= (500−n)/500=1−n/500. Now Setting pn≤0.05 yields n≥475.

<h3>Programming Challenges</h3>

<h4>1-1. “The 3n + 1 Problem” – Programming Challenges 110101, UVA Judge 100.</h4>


<h4>1-2. “The Trip” – Programming Challenges 110103, UVA Judge 10137.</h4>


<h4>1-3. “Australian Voting” – Programming Challenges 110108, UVA Judge 10142.</h4>


