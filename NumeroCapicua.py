def NumeroCapicua(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    if type(numero) != int:
        return None
    numero_s = str(numero)
    numero_digitos = len(numero_s)
    aux = int(numero_digitos) // 2
    resultado = True
    for n in range(numero_digitos):
        while n <= aux-1:
            if numero_s[n] == numero_s[numero_digitos-n-1]:
                resultado = True
            else:
                return False
            n += 1
    return resultado


print(NumeroCapicua(101))



