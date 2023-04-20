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
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        Text = Readfile.split('\n')
        Linecount= len(Text)

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
    with open(file,'r') as Opened:

        Readfile = Opened.read()
        Text = Readfile.split('\n')
        print(Text)
        Text[linenum-1] = edit
    with open(file,'w') as Writing:
        for line in Text:
            Writing.write(f'{line}\n')
    return


