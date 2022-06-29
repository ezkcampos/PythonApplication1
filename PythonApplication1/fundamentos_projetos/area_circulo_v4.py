import math
import sys

def circulo(r):
    return('area:', math.pi  * float(r) ** 2)


if __name__ == '__main__':
    r = sys.argv[1]
    area = circulo(r)
    print('Area do circulo:', area)