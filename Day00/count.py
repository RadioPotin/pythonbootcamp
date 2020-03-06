import sys, string

def text_analyzer(s):
    try:
        dico = {'low': 0, 'upper': 0, 'punctuation': 0, 'space': 0}
        for c in s:
            if c.islower():
                dico['low'] += 1
            elif c.isupper():
                dico['upper'] += 1
            elif c.isspace():
                dico['space'] += 1
            elif c in string.punctuation:
                dico['punctuation'] += 1
        for key,value in dico.items():
            print("- ", value, key, "letters")
    except ValueError:
        print('- 0 upper case letter\n- 0 lower letters\n- 0 punctuation letters\n- 0 spaces')


def main():
    if len(sys.argv) is not 2:
        s = input("Oops, looks like you forgot to provide a text to analyze ! Please do:")
        text_analyzer(s)
    else:
        text_analyzer(sys.argv[1])

if __name__ == "__main__":
    main()
