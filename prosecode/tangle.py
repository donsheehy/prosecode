import markdown
from prosecode.chunk_extension import CodeChunkExtension
from prosecode.displaymath_extension import DisplayMathExtension
import os

def tangle(mdfile, srcdir):
    # md = open(mdfile, 'r').read()
    # The CodeChunkExtension will find the code without executing it.
    # codechunks = CodeChunkExtension(execute = False)
    # Parse it once to tangle out the codechunks
    # markdown.markdown(md, extensions=[codechunks])

    allchunks = _allchunks(mdfile)
    chunks = [c for c in allchunks.values() if c.keep()]
    chunks.sort(key = lambda c: c.id)
    # The `tangled` dictionary maps names to the lexicographically last chunk
    # with that name.
    tangled = {}
    for chunk in chunks:
        tangled[chunk.name] = chunk

    for name, chunk in tangled.items():
        name = name.replace('.', '/')
        with open(srcdir + name + '.py', 'w') as outfile:
            outfile.write(chunk.fullstr())

def _allchunks(mdfile):
    md = open(mdfile, 'r').read()
    # The CodeChunkExtension will find the code without executing it.
    codechunks = CodeChunkExtension(execute = False)
    # Parse it once to tangle out the codechunks
    markdown.markdown(md, extensions=[codechunks])
    return codechunks.chunks

def cleanup(mdfile, srcdir):
    # allchunks
    filenames = {c.name for c in _allchunks(mdfile).values() if c.keep()}
    # filenames = {chunk.name for chunk in allchunks.values()}
    for name in filenames:
        name = name.replace('.', '/')
        os.remove(srcdir + name + '.py')


if __name__ == '__main__':
    SRC_DIR = './examples/src/'
    MD_FILE = './examples/tangle.md'

    # tangle(MD_FILE, SRC_DIR)
    cleanup(MD_FILE, SRC_DIR)
