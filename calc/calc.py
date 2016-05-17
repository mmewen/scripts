from math import *
from sys import argv

exp = "".join(argv[1:])

print exp, " = "
print eval(exp)
