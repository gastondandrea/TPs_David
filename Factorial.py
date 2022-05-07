def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    if type(numero) != int or numero < 1:
        return None
    aux = numero
    while aux > 1:
        numero = numero * (aux-1)
        aux=aux-1
    return numero

print(Factorial(4))