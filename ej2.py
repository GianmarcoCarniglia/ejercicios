def funciondelista(funcion, lista):
    list = []
    for i in lista:
        if funcion(i)== True:
            list.append(i)
    return list

def mayor10(i):
    return i>10


print(funciondelista(mayor10, [1, 5, 10, 15, 20, 25]))