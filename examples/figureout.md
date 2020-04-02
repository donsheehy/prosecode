Goals:
A python script that generates a figure should
1. save a pdf
2. save an svg
3. print the svg as html output in Atom
4. add image tag for the svg in html
5. add the includegraphics for the pdf in latex

For steps 1, 2, and 3, this is managed by a context manager.

Step 4 is handled by the code chunk processor.
It looks for the figure option in the code chunk header.
If it finds it, it suppresses the output and writes the html img tag using the id for the filename.
No extension should be used in the id.

Step 5 is handled by the html to latex parser.
It finds the html image tag and builds a corresponding `includegraphics` command, changing the filename from an `.svg` extension to `.pdf`.

**Note: This requires pip installing dsviz**

```python {cmd figure id="figures.testfigure" output="html"}
from dsviz.canvas import svg_plus_pdf

with svg_plus_pdf(600, 480, 'figures/testfigure') as c:
    c.point((30,30), 'ps')
    c.point((50,30), 'doublepoint')
    c.circle((100,100), 40, 'stark')
    c.rectangle((250,20), 100, 200)
    c.line((100,200), (300, 150))
    c.text('hello', (140, 300))

```

```python {cmd figure id="figures.list01" output="html"}
from dsviz.canvas import svg_plus_pdf
from dsviz.datastructures import VizList

with svg_plus_pdf(600, 480, 'figures/list01') as canvas:
    VizList([1,2,3, 'a string', '0']).draw(canvas)

```
