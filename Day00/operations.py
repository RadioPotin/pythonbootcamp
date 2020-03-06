import sys

def do_op(x, y):
    dico = {'Sum:': "0", 'Difference:': "0", 'Product:': "0", 'Quotient:': "0", 'Remainder:': "0"}
    dico['Sum:'] = str(x + y)
    dico['Difference:'] = str(x - y)
    dico['Product:'] = str(x * y)
    dico['Quotient:'] = str(x / y) if y is not 0 else "ERROR (Div by zero)"
    dico['Remainder:'] = str(x % y) if y is not 0 else "ERROR (Mod by zero)"
    for key, value in dico.items():
        print(key, value)
    return

def main():
    if len(sys.argv) < 3:
        print("Usage: python operations.py <int1> <int2>\nExample:\n\tpython operations.py 42 0.")
        return
    elif len(sys.argv) > 3:
        print("InputError: Too many arguments.")
    elif int(sys.argv[1]) == None or int(sys.argv[2]) == None:
        print("InputError: Only integers !!")
    else:
        do_op(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == "__main__":
    main()
