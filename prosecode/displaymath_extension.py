from markdown import Extension
from markdown.preprocessors import Preprocessor
import re

class DisplayMathExtension(Extension):

    def extendMarkdown(self, md):
        """ Add DisplayMathPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.register(DisplayMathPreprocessor(md), 'display_math', 27)

class DisplayMathPreprocessor(Preprocessor):
    DISPLAY_MATH_RE = re.compile(r'''
(?P<math>^\\\[        # opening \[
.*?                   # the contents
\\\])                  # closing \]
''', re.MULTILINE | re.DOTALL | re.VERBOSE)

    def run(self, lines):
        """ Match and store Display Math Blocks in the HtmlStash. """
        text = "\n".join(lines)
        while True:
            m = self.DISPLAY_MATH_RE.search(text)
            if not m:
                break
            math = self._escape(m.group('math'))
            placeholder = self.md.htmlStash.store(math)
            text = '{}\n{}\n{}'.format(text[:m.start()],
                                   placeholder,
                                   text[m.end():])

        return text.split("\n")

    def _escape(self, txt):
        """ basic string escaping """
        # txt = txt.replace('\\', '\\\\')
        return txt


def makeExtension(**kwargs):  # pragma: no cover
    return DisplayMathExtension(**kwargs)
