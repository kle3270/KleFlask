import sys

def Read_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
    return Readfile
def Joinlist_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        Splitfile = Readfile.split(',')
    return Splitfile
