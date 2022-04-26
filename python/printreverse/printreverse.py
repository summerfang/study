from sqlalchemy import null


def print_reserse(str):
    if len(str) == 0:
        return
    else:
        print_reserse(str[1:])
        print(str[0], end='')

if __name__ == '__main__':
    s = "Hello World!"
    print_reserse(s)
    print('\n')