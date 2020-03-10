import markdown
from prosecode.chunk_extension import CodeChunkExtension
from prosecode.displaymath_extension import DisplayMathExtension

def tangle(srcdir, mdfilename):
    mdfile = open(mdfilename, 'r')
    md = mdfile.read()
    codechunks = CodeChunkExtension(execute = False)
    # Parse it once to tangle out the codechunks
    markdown.markdown(md, extensions=[codechunks])


    displaymath = DisplayMathExtension()
    codechunks = CodeChunkExtension(execute = True)
    html = markdown.markdown(md, extensions=[codechunks,
                                             displaymath,
                                             'tables',
                                             ])

    chunks = [c for c in codechunks.chunks.values() if c.keep()]

    chunks.sort(key = lambda c: c.id)
    tangled = {}
    for chunk in chunks:
        tangled[chunk.name] = chunk

    for name, chunk in tangled.items():
        name = name.replace('.', '/')
        with open(srcdir + name + '.py', 'w') as outfile:
            outfile.write(chunk.fullstr())

    return html

if __name__ == '__main__':
    SRC_DIR = './examples/src/'
    MD_FILE = './examples/tables.md'
    OUT_FILE = MD_FILE.replace('md', 'html')

    html = tangle(SRC_DIR, MD_FILE)
    with open(OUT_FILE, 'w') as htmlfile:
        htmlfile.write(html)
