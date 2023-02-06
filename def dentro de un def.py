def funciondelista(funcion, lista):
    list = []
    for i in lista:
        list.append(funcion(i))
    return list


def suma(i):
    return i + 1

print(funciondelista(suma, [1,2,3,4,5,6]))