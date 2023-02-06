def funciondelista(funcion, lista):
    list = []
    for i in lista:
        list.append(funcion(i))
    return list


def suma(i):
    return i + 1