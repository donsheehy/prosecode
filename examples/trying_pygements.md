# Some basic Pygments examples

```python {cmd id="imports"}
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter
```

```python {cmd continue="imports" output="html"}
style_defs = LatexFormatter().get_style_defs()
style_file ='./pygments_macros.tex'

with open(style_file, 'w') as outfile:
    outfile.write(style_defs)
```

```python {cmd continue="imports"}
code = 'print "Hello World")'
print(highlight(code, PythonLexer(), LatexFormatter()))
