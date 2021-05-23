<h3>Simulating Graph Algorithms</h3>

<h4>5-1.</h4> 
```python
G1
      ┌ C ┐
  ┌ B   |   F┐
  │ |└ E ┘ │
  │ | ╱ | ╲  │
A ─ D   |   H┤
  │   ╲ | ╱  │
  │     G    │   
  └ I ─J──┘
```

```python
result = 0   

for i in range(n,-1,-1):

  result = result*x + poly[i]
```
