import math
import sys


nota = float(input('Informe a nota: '))

if __name__ == '__main__':
    if nota >= 9.1 and  nota <=10:
        print("nota A")
    elif nota >= 8.1:
        print('nota A-')
    elif nota >= 7.1:
        print('nota B')
    elif nota >= 6.1:
        print('nota B-')
    elif nota >= 5.1:
        print('nota C')
    elif nota >= 4.1:
        print('nota C-')
    elif nota >= 3.1:
        print('nota D')
    elif nota >= 2.1:
        print('nota D-')
    elif nota >= 1.1:
        print('nota E')
    elif nota >= 0:
        print('nota E-')
    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Area do circulo:', area) 