def maior_elemento(lista):
    num_max = lista[0]
    for i in lista:
        if i > num_max:
            num_max = i
    
    return num_max


def menor_elemento(lista):
    num_min = lista[0]
    for i in lista:
        if i < num_min:
            num_min = i
    
    return num_min

def num_pares(lista):
    lista_pares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

def primeiro_elemento(lista):
    contador = 0
    for i in range(0, len(lista)):
        if lista[i] == lista[0]:
            contador += 1
    return contador

def media_elementos(lista):
    soma = 0
    for i in lista:
        soma += i

    media = soma/len(lista)
    return media

def soma_negativos(lista):
    soma_negativos = 0
    for i in lista:
        if i < 0:
            soma_negativos += i

    return soma_negativos


numeros = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

def switch_case(valor):
    if valor == 1:
        print("===== Maior Elemento =====")
        print(maior_elemento(numeros))

    if valor == 2:
        print("===== Menor Elemento =====")
        print(menor_elemento(numeros))

    if valor == 3:
        print("===== Numeros Pares =====")
        print(num_pares(numeros))

    if valor == 4:
        print("===== Ocorrencias do Primeiro Elemento da Lista =====")
        print(primeiro_elemento(numeros))

    if valor == 5:
        print("===== Media dos Elementos =====")
        print(media_elementos(numeros))

    if valor == 6:
        print("===== Soma dos Valores Negativos =====")
        print(soma_negativos(numeros))


print(switch_case(2))


