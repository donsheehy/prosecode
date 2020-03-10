from prosecode.tangle import tangle

SRC_DIR = './examples/src/'
MD_FILE = './examples/tangle.md'

html = tangle(SRC_DIR, MD_FILE)
with open('small_tangle_.html', 'w') as htmlfile:
    htmlfile.write(html)
