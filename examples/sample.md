# This is a sample markdown file

It contains some inline math $X = \left\{(i,i+1) \mid i \in \{1,\ldots ,n\}\right\}$.
It also has some display math.

\[
  e^x  = \sum_{i=0}^\infty \frac{x^i}{i!}
\]

There is a bit of code.

```python {cmd id="startingpoint"}
x = 100
y = 200
```

```
Here's a block that should just be output.

```

That code is continued one way.

```python {cmd continue="startingpoint"}
print('The value of x' , x, '.')
x = 1000
```

Then, that code is continued a different way.

```python {cmd continue="startingpoint"}
print('The value of x is still' , x, '.')
```
