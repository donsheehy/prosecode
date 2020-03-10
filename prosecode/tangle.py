import markdown
from prosecode.chunk_extension import CodeChunkExtension

def tangle(srcdir, mdfilename):
    mdfile = open(mdfilename, 'r')
    md = mdfile.read()
    codechunks = CodeChunkExtension()
    html = markdown.markdown(md, extensions=[codechunks])

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
    MD_FILE = './examples/tangle.md'

    html = tangle(SRC_DIR, MD_FILE)
    with open('./examples/small_tangle.html', 'w') as htmlfile:
        htmlfile.write(html)
