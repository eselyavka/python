import re

class ProcessConfig():
    dfile = None

    def __init__(self, dfile):
        self.dfile = dfile

    def replace(self, template, replacement):
        with open(self.dfile, 'r+') as fh:
            lines = fh.readlines()
            fh.seek(0)
            fh.truncate()
            for line in lines:
                if (re.search(template, line)):
                    fh.write(re.sub(template, replacement, line))
                else:
                    fh.write(line)
