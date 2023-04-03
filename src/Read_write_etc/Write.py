import sys
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
