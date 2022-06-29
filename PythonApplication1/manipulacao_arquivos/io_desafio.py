import csv
import urllib.request

def read(url):
    with urllib.request.urlopen(url) as entrada:
        print('baixando o csv')
        dados = entrada.read().decode('latin1')
        print('csv baixado')
        for cidade in csv.reader(dados.splitlines()):
            #imprimir a 9ª coluna e a 4ª coluna(comeca em 0)
            print(f'{cidade[8]}:{cidade[3]}')



if __name__ == '__main__':
    #string raw para não ter erro na hora de ler o link do csv
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')