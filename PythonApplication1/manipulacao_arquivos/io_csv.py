import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        #o * esta como operador de argumentos e variaveis
        print('Nome: {}, Idade: {}'.format(*pessoa))