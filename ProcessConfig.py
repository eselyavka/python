import re

class ProcessConfig():
    def __init__(self):
        pass

        def replace(self, template, sfile, replace):
        with open(sfile, 'r+') as fh:
            lines = fh.readlines()
            fh.seek(0)
            fh.truncate()
            for line in lines:
                if (re.search(template, line)):
                    fh.write(re.sub(template, replace, line))
                else:
                    fh.write(line)
