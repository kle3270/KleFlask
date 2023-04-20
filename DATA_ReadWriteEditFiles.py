##Create

def Create_file(Username):
    open(f"{Username}Notes.txt",'x')


## Read
def Read_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        print(Readfile)
    return Readfile

def Joinlist_file(file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        Splitfile = Readfile.split('\n')
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


##Write
def Write_file(write,file):
    with open(file, 'a') as g:
        g.write(f'{write}\n')
    return
def Edit_line(file,linenum,edit):
    Linecount = 0
    with open(file,'r') as Opened:
        Readfile = Opened.read()

    Readfile.replace(f'Line {linenum}')

    return Linecount


