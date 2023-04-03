import sys

def Read_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        print(Readfile)
    return Readfile
def Joinlist_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        Splitfile = Readfile.split('\n')
    return Splitfile
def Line_Count(file):
    Linecount = 0
    with open(file,'r') as Opened:
        Readfile = Opened.read()
        for Line in Readfile:
            if Line == '\n':
                Linecount = Linecount + 1
    return Linecount
def Readline_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.readline(1)
        print(Readfile)
    return Readfile
