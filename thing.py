import gc
class B():
    def __init__(self,yes):
        self.yes = yes
    def __str__(self):
        return f'{self.yes}'
person = B('no')
a = B('s')
c= B('a')
print(isinstance(a,B))