def fibonacci(quantidade):
    resultado = [0, 1]
    #usando lista no lugar de variaveis
    while True:
        #usando função soma para somar os dois ultimos valores da lista
        resultado.append(sum(resultado[-2:]))
        #o que vai determinar a parada vai ser a quantidade de valores da lista
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    #o laço for, para fazer uma repetição a partir de cada numero da lista
    for fib in fibonacci(20):
        print(fib)
