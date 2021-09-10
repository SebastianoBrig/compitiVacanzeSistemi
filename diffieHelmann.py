import random

p=5
g=11
a = random.randint(2,p-1)
b = random.randint(2,p-1)
A = pow(g,a,p)
B = pow(g,b,p)
As = pow(B,a,p)
Bs = pow(A,b,p)
print(f"alice secret:{As}, bob secret: {Bs}")