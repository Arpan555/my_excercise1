class Arpan():
    def __init__(self):
        self.str1=''
    def get(self):
        self.str1=input()
    def print(self):
        print(self.str1.upper())
obj=Arpan()
obj.get()
obj.print()
