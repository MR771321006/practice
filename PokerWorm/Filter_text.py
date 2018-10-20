import re


def Filter_text():
    b = re.compile(r'^例子.*?/>')
    a = str(b)
    a = a.replace(a, '')
