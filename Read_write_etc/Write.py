import sys
def Write_file(write,file):
    with open(file, 'r') as Opened:
        Readfile = Opened.read()
        Writefile = Readfile.split(',')
        print(Writefile)
    with open(file, 'w') as g:
        Writefile.append(write)
        g.write(','.join(Writefile))
    return Writefile

