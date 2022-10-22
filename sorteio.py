def mergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k] = listaDaEsquerda[i]
                i += 1
            else:
                lista[k] = listaDaDireita[j]
                j += 1
            k += 1
        while i < len(listaDaEsquerda):

            lista[k] = listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k] = listaDaDireita[j]
            j += 1
            k += 1
        return lista

if __name__ == '__main__':
    print('Ordenar lista')
    
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista inserida: ", lista)
    print("Lista ordenada: ", mergeSort(lista))
