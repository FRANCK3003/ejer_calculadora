def validar_entero(numero):
    """_summary_

    Args:
        numero (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        entrada = input(numero)
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Error, se esperaba un entero")

def sumar (a:int, b:int)->int:
    try:
        resultado = a + b
        return resultado
    except TypeError:
        raise TypeError("Se esperaban enteros")

def restar (a:int, b:int)->int:
    try:
        resultado = a - b
        return resultado
    except TypeError:
        raise TypeError("Se esperaban enteros")

def divicion (a:int, b:int)->int:
    try:
        div = a / b
    except ZeroDivisionError:
        print("----------¡No puedes dividir por cero!----------")
        div = None
    return div

def multiplicar (a:int, b:int)->int:
    try:
        resultado = a * b
        return resultado
    except TypeError:
        raise TypeError("Se esperaban enteros")

def limpiar_pantalla():
    from os import system
    system("cls")

def pausar():
    from os import system
    system("pause")

def menu_calculadora(a,b)->str:
    limpiar_pantalla()
    print("   -------Calculadora-------")
    print(f"A = {a}")
    print(f"B = {b}")
    print("1- Sumar")
    print("2- Restar")
    print("3- Dividir")
    print("4- Multiplicar")
    print("5- Factorial")
    print("6- Salir")
    return input("Ingrese opcion: ")

def confirmar_salir(confirmacion:str)->bool:
    while confirmacion != "si" and confirmacion != "no":
        print("Error, Elija solamente 'si' o 'no'")
    if confirmacion == "si":
        return True
    return False

def factorial (n:int)->int:
    if not isinstance (n,int):
        raise ValueError("Error, se esperaba un entero")
    if n < 0:
        raise ValueError("El número no debe ser un negativo.")
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n -1)
    return fact
