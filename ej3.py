from math import sin, cos, tan, exp, log

def funcionmath (num):
    for i in range(1, int(num+1)):
        seno=sin(i)
        coseno=cos(i)
        tangente=tan(i)
        exponencial=exp(i)
        logaritmo=log(i)

        print(f'Seno: {seno}, coseno: {coseno}, tangente: {tangente}\nexponencial: {exponencial}, logaritmo: {logaritmo}\n')

def solicitud():
    num=int(input('Ingrese un numero: '))
    return num



funcionmath(solicitud())