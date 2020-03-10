import markdown
from prosecode.chunk_extension import CodeChunkExtension

mdfile = open('./examples/sample.md', 'r')
md = mdfile.read()
codechunks = CodeChunkExtension()
# print(codechunks.chunks)
html = markdown.markdown(md, extensions=[codechunks])
# print(html)
for lang, options, code in codechunks.chunks:
    print(lang, options, '\n')
    print(code)
    print('-'*40)

"""
A wrong output using the existing fenced code block extension.

<h1>This is a sample markdown file</h1>
<p>It contains some inline math $X = \left{(i,i+1) \mid i \in {1,\ldots ,n}\right}$.
It also has some display math.</p>
<p>[
  e^x  = \sum_{i=0}^\infty \frac{x^i}{i!}
]</p>
<p>There is a bit of code.</p>
<p>```python {cmd id="startingpoint"}
x = 100</p>
<pre><code>
That code is continued one way.
```python {cmd continue=&quot;startingpoint&quot;}
print('The value of x' , x, '.')
x = 1000
</code></pre>

<p>Then, that code is continued a different way.
<code>python {cmd continue="startingpoint"}
print('The value of x is still' , x, '.')</code></p>
"""
