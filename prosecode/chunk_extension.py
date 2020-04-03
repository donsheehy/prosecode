from markdown import Extension
from markdown.preprocessors import Preprocessor
from prosecode.chunk import Chunk
import re

class CodeChunkExtension(Extension):

    def __init__(self, execute = False, executepath = ''):
        super().__init__()
        self.execute = execute
        self.executepath = executepath
        self.chunks = {}

    def extendMarkdown(self, md):
        """ Add CodeChunkPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        preprocessor = CodeChunkPreprocessor(md, self.chunks, self.execute,
                                             self.executepath)
        md.preprocessors.register(preprocessor, 'code_chunk', 26)

class CodeChunkPreprocessor(Preprocessor):
    CODE_CHUNK_RE = re.compile(r'''
(?P<fence>^(?:`{3,}))[ ]*                # opening ```
(?P<lang>[\w#.+-]*)[ ]*                  # language
(?P<chunkoptions>\{.*?\})?[ ]*\n         # code chunk options
(?P<code>.*?)
(?<=\n)(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)
    CODE_WRAP = '<pre class="prettyprint"><code%s>%s</code></pre>'
    LANG_TAG = ' class="lang-%s"'
    OUTPUT_CLASS = ' class="verbatim"'

    def __init__(self, md, chunks, execute, executepath = ''):
        super().__init__(md)
        self.chunks = chunks
        self.execute = execute
        self.executepath = executepath

    def run(self, lines):
        """ Match code chunks and store them in the HtmlStash. """
        text = "\n".join(lines)
        while True:
            m = self.CODE_CHUNK_RE.search(text)
            if not m: break # Break if there is no match.

            # Extract lang, code, and chunkoptions from the match.
            lang = m.group('lang')
            if lang is None:
                lang = 'verbatim'
            code = m.group('code')
            chunkoptions = m.group('chunkoptions')

            # Create the chunk, register is predecessor and store it.
            chunk = Chunk(lang, chunkoptions, code)
            chunk.setcontinue(self.chunks.get(chunk.cont_id))
            self.chunks[chunk.id] = chunk

            # If it's a chunk we want to see, stash it.
            if chunk.hide:
                placeholder = ''
            else:
                codehtml = self._codehtml(lang, code)
                placeholder = self.md.htmlStash.store(codehtml)

            output = ''
            if self.execute and chunk.cmd:
                stdout, stderr = chunk.execute(self.executepath)
                if len(stdout) + len(stderr) > 0:
                    if chunk.error_expected:
                        rawoutput = self._escape(stdout + '\n' + stderr)
                    else:
                        if stderr:
                            pass
                            # This is where we would log any errors.
                        rawoutput = self._escape(stdout)
                    if chunk.figure:
                        imgfilename = chunk.id.replace('.', '/') + '.svg'
                        chunkoutput = '<img src=\"{}\"></img>'.format(imgfilename)
                        output = self.md.htmlStash.store(chunkoutput)
                    elif chunk.output != 'none':
                        chunkoutput = self._codehtml('verbatim', rawoutput)
                        output = self.md.htmlStash.store(chunkoutput)

            text = '{}\n{}\n{}\n{}'.format(text[:m.start()],
                                       placeholder,
                                       output,
                                       text[m.end():])

        return text.split("\n")

    def _codehtml(self, lang, code):
        langhtml = self.LANG_TAG % lang if lang else ''

        codehtml = self.CODE_WRAP % (langhtml,
                                    self._escape(code))
        return codehtml

    def _escape(self, txt):
        """ basic html escaping """
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('<', '&lt;')
        txt = txt.replace('>', '&gt;')
        txt = txt.replace('"', '&quot;')
        return txt


def makeExtension(**kwargs):  # pragma: no cover
    return CodeChunkExtension(**kwargs)
