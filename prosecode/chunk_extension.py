from markdown import Extension
from markdown.preprocessors import Preprocessor
from prosecode.chunk import Chunk
import re

class CodeChunkExtension(Extension):

    def __init__(self, execute = False):
        super().__init__()
        self.execute = execute
        self.chunks = {}

    def extendMarkdown(self, md):
        """ Add CodeChunkPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        preprocessor = CodeChunkPreprocessor(md, self.chunks, self.execute)
        md.preprocessors.register(preprocessor, 'code_chunk', 26)

class CodeChunkPreprocessor(Preprocessor):
    CODE_CHUNK_RE = re.compile(r'''
(?P<fence>^(?:`{3,}))[ ]*                # opening ```
(?P<lang>[\w#.+-]*)[ ]*                  # language
(?P<chunkoptions>\{.*?\})?[ ]*\n         # code chunk options
(?P<code>.*?)
(?<=\n)(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)
    CODE_WRAP = '<pre><code%s>%s</code></pre>'
    LANG_TAG = ' class="%s"'
    OUTPUT_CLASS = ' class="verbatim"'

    def __init__(self, md, chunks, execute):
        super().__init__(md)
        self.chunks = chunks
        self.execute = execute

    def run(self, lines):
        """ Match and store Fenced Code Blocks in the HtmlStash. """
        text = "\n".join(lines)
        """
        This loop should be replaced this with `re.finditer`
        """
        while True:
            m = self.CODE_CHUNK_RE.search(text)
            if not m:
                break

            lang = m.group('lang')
            if lang is None:
                lang = 'verbatim'
            code = m.group('code')
            chunkoptions = m.group('chunkoptions')
            langhtml = self.LANG_TAG % lang if lang else ''

            codehtml = self.CODE_WRAP % (langhtml,
                                        self._escape(code))


            chunk = Chunk(lang, chunkoptions, code)
            chunk.setcontinue(self.chunks.get(chunk.cont_id))
            self.chunks[chunk.id] = chunk

            if chunk.hide:
                placeholder = ''
            else:
                placeholder = self.md.htmlStash.store(codehtml)

            output = None
            if self.execute and chunk.cmd:
                stdout, stderr = chunk.execute()
                if len(stdout) + len(stderr) > 0:
                    if chunk.error_expected:
                        rawoutput = self._escape(stdout + '\n' + stderr)
                    else:
                        rawoutput = self._escape(stdout)
                    chunkoutput = self.CODE_WRAP % (self.OUTPUT_CLASS,
                                                    rawoutput)
                    if chunk.output != 'none':
                        output = self.md.htmlStash.store(chunkoutput)

            if output:
                text = '{}\n{}\n{}\n{}'.format(text[:m.start()],
                                           placeholder,
                                           output,
                                           text[m.end():])
            else:
                text = '{}\n{}\n{}'.format(text[:m.start()],
                                       placeholder,
                                       text[m.end():])

        return text.split("\n")

    def _escape(self, txt):
        """ basic html escaping """
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('<', '&lt;')
        txt = txt.replace('>', '&gt;')
        txt = txt.replace('"', '&quot;')
        return txt


def makeExtension(**kwargs):  # pragma: no cover
    return CodeChunkExtension(**kwargs)
