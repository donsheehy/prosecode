import re
import random
import string
import subprocess

def random_id():
    alphabet = 'abcdefghijklmnopqrstuvwxyz123456789'
    return ''.join(random.choice(alphabet) for i in range(10))

def keyvalue(string, key):
    pattern = (r'\{.*?(?P<key>(?<=\{|\s)' +
                key +
                r'(?=\}|\s|=))((\s*=\s*)\"?(?P<value>(\w|_|\.)*)\"?)?.*?\}')

    m = re.compile(pattern).search(string)
    if m:
        value = m.group('value')
        if value:
            if value in ['true', 'True']:
                return True
            if value in ['false', 'False']:
                return False
            else:
                return value
        else:
            return True
    return False

class Chunk:
    def __init__(self, lang, options, code):
        self.lang = lang
        self.code = code
        self.cont = None

        if options is None:
            self.cmd = False
            self.hide = False
            self.output = 'text'
            self.id = False
            self.tagclass = None
            self.cont_id = None
            self.error_expected = False
        else:
            self.cmd = keyvalue(options, 'cmd')
            self.hide = keyvalue(options, 'hide')
            self.output = keyvalue(options, 'output')
            self.id = keyvalue(options, 'id')
            self.tagclass = keyvalue(options, 'class')
            self.cont_id = keyvalue(options, 'continue')
            self.error_expected = keyvalue(options, 'error_expected')
            # TODO: implement element, stdin, args

        if self.id == False:
            self.id = random_id()
        namestart = 1 if self.id[0] == '_' else 0

        nameend = -3if self.id[-3] == '_' else None
        self.name = self.id[namestart : nameend]

    def setcontinue(self, chunk):
        if chunk:
            if chunk == self:
                # print("Continue id: ", chunk.cont_id)
                raise RuntimeError("Continue cannot point to self.")
            self.cont = chunk

    def keep(self):
        return self.id[0] == '_'

    def fullstr(self):
        if self.cont is self:
            raise RuntimeError("The continue cannot point to self.")
        if self.cont is None:
            return str(self)
        else:
            return "\n".join([self.cont.fullstr(), str(self)])

    def execute(self):
        filename = self.id
        with open(filename, 'w') as outfile:
            outfile.write(self.fullstr())
        # TODO: possibly change the lang to cmd
        process = subprocess.run([self.lang, filename],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        subprocess.run(['rm', filename],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
        return process.stdout.decode(), process.stderr.decode()

    def __str__(self):
        return self.code
