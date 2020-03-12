import markdown
from prosecode.chunk_extension import CodeChunkExtension

def tangle(md):
    """
    Return a dictionary of code blocks.  The keys are filenames and the values
    are the code.
    """
    # The CodeChunkExtension will find the code without executing it.
    codechunks = CodeChunkExtension(execute = False)

    # Parse it to find the code chunks.
    markdown.markdown(md, extensions=[codechunks])

    # Filter teh chunks to keep and sort them by id.
    chunks = sorted(c for c in codechunks.chunks.values() if c.keep())

    # The returned dictionary maps names to the lexicographically last chunk
    # with that name.  This works because chunks is sorted by id.
    return {chunk.name : chunk for chunk in chunks}
