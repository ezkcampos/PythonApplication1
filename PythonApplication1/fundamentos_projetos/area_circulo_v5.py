import math
import sys

def circulo(r):
    return('area:', math.pi  * float(r) ** 2)

def help():
    print("É necessario informar corretamente o raio do circulo.") 
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        help()
        print('o raio deve ser um valor numerico')
    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Area do circulo:', area) 