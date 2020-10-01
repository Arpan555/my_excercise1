from math import sqrt
C=50
H=30
def square(D):
    D=int(D)
    return str(int(sqrt((2*C*D)/H)))
D = input('enter value of D').split(',')
D = list(map(square,D))  
print(",".join(D))
