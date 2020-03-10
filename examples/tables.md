# Here is a nice little table

| Operation Name            | Code      | Cost |
|---------------------------|-----------|:------:|
| Add a new item            | `A.add(newitem)` | $1$ |
| Delete an item            | `A.delete(item)` | $1$ |
| Union                     | `A | B`   | $n_A + n_B$ |
| Intersection              | `A & B`   | $\min\{n_A, n_B\}$ |
| Set differences           | `A - B`   | $n_A$ |
| Symmetric Difference      | `A ^ B`   | $n_A + n_B$ |





```python {cmd output="text"}
import markdown

def escape(txt):
    """ basic html escaping """
    txt = txt.replace('&', '&amp;')
    txt = txt.replace('<', '&lt;')
    txt = txt.replace('>', '&gt;')
    txt = txt.replace('"', '&quot;')
    return txt

tbl = """
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
"""

html = markdown.markdown(tbl, extensions=['tables'])
print(escape(html))
```

The goal is to transform this into the following.

```
\begin{tabular}{c c}
\hline
First Header & Second Header \\
\hline
Content Cell & Content Cell \\
Content Cell & Content Cell \\
\hline
\end{tabular}
```
