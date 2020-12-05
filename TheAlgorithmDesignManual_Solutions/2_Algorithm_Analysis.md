
<h3>Program Analysis</h3>

<h4>2-1.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Excercises%202-1.jpg)

<h4>2-2.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Excercises%202-2.jpg)

<h4>2-3.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Excercises%202-3.jpg)

<h4>2-4.</h4> 

![image](https://github.com/foxfromworld/Coding-Interview-Preparation-with-LeetCode-and-An-Algorithm-Book/blob/main/TheAlgorithmDesignManual_Solutions/Excercises%202-4.jpg)

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

    
<h4>2-5.</h4> 
  
