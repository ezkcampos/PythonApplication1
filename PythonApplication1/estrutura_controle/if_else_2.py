import math
import sys

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'menor de idade'
    elif idade in range (18, 64):
        return 'Adulto'
    elif idade in range (65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'idade inválida'


if __name__ == '__main__':
    for idade in (17, 35, 86, 113, -2):
        print (f'{idade}: {faixa_etaria(idade)}')