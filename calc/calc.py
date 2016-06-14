from math import *
from sys import argv

exp = "".join(argv[1:]).replace("x","*")

print exp, " = "
print eval(exp)
