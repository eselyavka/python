import re

class ProcessConfig():
    dfile = None
    replacements = list()
    def __init__(self, dfile):
        self.dfile = dfile

    def replacementsPush(self, replace):
        self.replacements.append(replace)
    
    def replace(self, template, sfile, replacement):
        with open(self.dfile, 'r+') as fh:
            lines = fh.readlines()
            fh.seek(0)
            fh.truncate()
            for line in lines:
                if (re.search(template, line)):
                    fh.write(re.sub(template, replacement, line))
                else:
                    fh.write(line)
