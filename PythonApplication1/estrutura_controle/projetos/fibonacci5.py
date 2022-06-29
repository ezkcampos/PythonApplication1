def fibonacci(limite):
    resultado = [0, 1]
    #usando lista no lugar de variaveis
    while resultado[-1] < limite:
        #usando função soma para somar os dois ultimos valores da lista
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    #o laço for, para fazer uma repetição a partir de cada numero da lista
    for fib in fibonacci(1000):
        print(fib)
