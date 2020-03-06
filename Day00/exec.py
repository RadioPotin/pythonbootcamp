import sys

def revarg(x):
    return x[::-1]

conc = ' '.join(sys.argv[1::])
print (revarg(conc).swapcase())
