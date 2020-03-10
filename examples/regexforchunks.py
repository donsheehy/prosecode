import re

FENCED_BLOCK_RE = re.compile(r'''
(?P<fence>^(?:~{3,}|`{3,}))[ ]*         # Opening ``` or ~~~
(\{?\.?(?P<lang>[\w#.+-]*))?[ ]*        # Optional {, and lang
# Optional highlight lines, single- or double-quote-delimited
(hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot))?[ ]*
}?[ ]*\n                                # Optional closing }
(?P<code>.*?)(?<=\n)
(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)

CODE_CHUNK_RE = re.compile(r'''
(?P<fence>^(?:`{3,}))[ ]*                # opening ```
(?P<lang>[\w#.+-]*)[ ]*                  # language
(?P<chunkoptions>\{.*?\})?[ ]*\n         # code chunk options
(?P<code>.*?)
(?<=\n)(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)

md = """
# This is a sample markdown file

It contains some inline math $X = \left\{(i,i+1) \mid i \in \{1,\ldots ,n\}\right\}$.
It also has some display math.

\[
  e^x  = \sum_{i=0}^\infty \frac{x^i}{i!}
\]

There is a bit of code.

```python
{cmd id="startingpoint"}
x = 100
y = 200
```

That code is continued one way.

```python
{cmd continue="startingpoint"}
print('The value of x' , x, '.')
x = 1000
```

Then, that code is continued a different way.

```python
{cmd continue="startingpoint"}
print('The value of x is still' , x, '.')
```
"""

# for m in re.finditer(CODE_CHUNK_RE, md):
for m in re.finditer(FENCED_BLOCK_RE, md):
    print('-'*40)
    print('lang=', m.group('lang'))
    # print('chunkoptions=', m.group('chunkoptions'))
    print(m.group('code'))
    print(m.start(), m.end())
    print(md[m.start(): m.end()])
