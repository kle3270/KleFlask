import sys
def Write_file(write,file):
    with open(file, 'a') as g:
        g.write(f'{write}\n')
    return
