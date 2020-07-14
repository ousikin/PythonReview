lista = [4, 2, 78, 12, 34, 68]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            print(lista)
