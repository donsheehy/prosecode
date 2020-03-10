## Tangle This!

```python {cmd id="_afinetangle_00"}
"""
This is the first part of the file.
"""

A_STRING = 'Hello, World!'
```

### How about some headers to break it up!

```python {cmd}
print("Executed, but not tangled.")
```

```python {cmd id="_subfolder.onepiece"}
"""
This should go in the subfolder
"""

def foo():
    pass

```

### More stuff

The following is more stuff.

```python {cmd id="_afinetangle_01" continue="_afinetangle_00"}
"""
This is the second part.
"""

print(A_STRING)
```
