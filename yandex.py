import re

#Task1
inKey = ('key1','key2','key3','key4')
inValues = ('value1','value2')

def toDict(inKey, inValues):
    outDict = dict()
    i=0
    for k in inKey:
        try:
            outDict[k] = inValues[i]
        except IndexError:
            outDict[k] = None
        i+=1
    return outDict

#Task2
def checkLoginRE(login):
    if login is not None:
        if len(login) == 1:
            ver = re.compile(r'^[a-z]', re.I|re.M)
            if ver.match(login) is not None:
                return login
        elif len(login) > 1 and len(login) <= 20:
            ver = re.compile(r'''^[a-z]{1} #first symbol only letter
                             [a-z0-9\.\-]{0,18} #then any 18 symbols
                             [a-z0-9]{1}$ #last symbol only letter or digit
                        ''', re.I|re.M|re.X)
            if ver.match(login) is not None:
                return login
    return None

def checkLoginArr(login):
    if login is not None:
        if len(login) == 1:
            if login.isalpha():
                return login
        elif len(login) > 1 and len(login) <= 20:
            if login[0].isalpha() and (login[-1].isalpha() or login[-1].isdigit()):
                incorrectSymbol = False
                for l in login[1:-1]:
                    if not (l.isalpha() and l.isnumeric() and l == '.' and l == '-'):
                        incorrectSymbol = True
                if not incorrectSymbol:
                    return login
    return None

#Task3
def sqlQuery():
    return '''select Name,count(*)
              from users u join messages m
              on u.uid=m.uid group by
              Name'''

#Task4
def shellExample():
    return '''awk '{print $1}' < access.log | sort | uniq -c -d  | sort -rnk1 | head -10'''

def shellExample2():
    return '''awk '{freq[$1]++} END {for (i in freq) {printf "%d\t%s\n", freq[i], i}}' < access.log | sort -rnk1 | head -10'''

def pythonExample():
    freq = dict()
    with(open('access.log', 'r')) as lines:
        for l in lines:
            if freq.has_key(l.split(' ')[0]):
                freq[l.split(' ')[0]]+=1
            else:
                freq[l.split(' ')[0]]=1

    i=0
    for ip in sorted(freq, key=freq.__getitem__, reverse=True):
        print ip + ' ' + str(freq[ip])
        if i == 9: break
        i+=1
