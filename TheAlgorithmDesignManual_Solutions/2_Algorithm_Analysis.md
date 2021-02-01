
<h3>Program Analysis</h3>

<h4>2-1.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercise%202-1.jpg)

<h4>2-2.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercise%202-2.jpg)

<h4>2-3.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercise%202-3.jpg)

<h4>2-4.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercise%202-4.jpg)

<h4>2-5.</h4> 

xpower := x ∗ xpower (i)

p := p + ai ∗ xpower (ii)

(a) n*(i)+n*(ii) => 2n multiplications; n*(ii) => n additions

(b) 2n multiplications

(c) https://en.wikipedia.org/wiki/Horner%27s_method

```python
result = 0   

for i in range(n,-1,-1):

  result = result*x + poly[i]
```
    
<h4>2-6.</h4> 

It compares every two value in the array from the first value to the last value and keeps the bigger value in each loop. So there won't be any problems. It's correct...

<h4>2-7.</h4> 

(a) True. 2^(n+1) = 2*(2^n) we can consider the 2 as a constant so the Big Oh notation is O(2^n)

(b) False 2^(2n) = 2^n^2 ==> O(2^2n)
  
<h4>2-8.</h4> 

• f(n) = O(g(n)) means c · g(n) is an upper bound on f(n). Thus there exists
some constant c such that f(n) is always ≤ c · g(n), for large enough n (i.e. ,
n ≥ n0 for some constant n0).

• f(n) = Ω(g(n)) means c · g(n) is a lower bound on f(n). Thus there exists
some constant c such that f(n) is always ≥ c · g(n), for all n ≥ n0.

• f(n) = Θ(g(n)) means c1 · g(n) is an upper bound on f(n) and c2 · g(n) is
a lower bound on f(n), for all n ≥ n0. Thus there exist constants c1 and c2
such that f(n) ≤ c1 ·g(n) and f(n) ≥ c2 ·g(n). This means that g(n) provides
a nice, tight bound on f(n).

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercises%202-8.jpg)

<h4>2-9.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercises%202-9.jpg)


<h4>2-10. 2-11. 2-13. 2-14.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercises%202-10_11_13_14.jpg)

<h4>2-12.</h4> 

(a) c = 1 (b) c = 2 (c) c = 2

<h4>2-15. 2-16. 2-17. 2-18. 2-19. 2-20.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercises%202-15_16_17_18_19_20.jpg)

<h4>2-21.</h4> 

(a) True

(b) False (c) True (Because square root of n dominates logn)

(d) False (logn = 2 log (square root of n) and the square root of n dominates logn)

(e) True

(f) True (logn = 2 log (square root of n))

(g) False (the other way round is correct)

<h4>2-22.</h4> 

(a) f(n) = Ω(g(n))

(b) f(n) = O(g(n))

(c) f(n) = Ω(g(n))

<h4>2-23.</h4> 

(a) Yes. The worst case is just the upper bound. So it's possible.

(b) Yes. The worst case is just the upper bound. So it's possible.

(c) Yes. 

(d) No. (I don't quite know why...)

(e) Yes. Both are Θ(n^2)

<h4>2-24. 2-25. 2-26. 2-27. 2-29. 2-30.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Exercises%202-24_25_26_27_29_30.jpg)
