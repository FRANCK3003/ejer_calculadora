def validar_entero(numero:str)->int:
    while True:
        entrada = input(numero)
        try:
            entero = int(entrada)
            return entero
        except ValueError:
            print("Error, se esperaba un entero")

def v_entero(a:int, b:int)->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Se esperaban enteros")

def sumar (a:int, b:int)->int:
    """suma 2 operadores 

    Args:
        a (int): primer operador de la sumatoria 
        b (int): segundo operador de la sumatoria 

    Returns:
        int: la suma de los numeros enteros
    """
    v_entero(a,b)
    resultado = a + b
    return resultado

def restar (a:int, b:int)->int:
    """resta 2 operadores

    Args:
        a (int): primer operador de la resta
        b (int): segundo operador de la resta

    Returns:
        int: la resta de los operadores
    """
    v_entero(a,b)
    resultado = a - b
    return resultado

def divicion (a:int, b:int)->int:
    """divide 2 operadores 

    Args:
        a (int): Primer operador a dividir
        b (int): Segundo operador a dividir

    Returns:
        int: resultado de la divicion
    """
    v_entero(a,b)
    try:
        div = a / b
    except ZeroDivisionError:
        print("----------¡No puedes dividir por cero!----------")
        div = None
    return div

def multiplicar (a:int, b:int)->int:
    """Multiplica 2 operadores

    Args:
        a (int): Primer operador a multiplicar
        b (int): Segundo operador a multiplicar 

    Returns:
        int: Resultado de la multiplicacion
    """
    v_entero(a,b)
    resultado = a * b
    return resultado

def limpiar_pantalla():
    """Limpia la pantalla de datos
    """
    from os import system
    system("cls")

def pausar():
    """pausa para ver resultados
    """
    from os import system
    system("pause")

def menu_calculadora(a,b)->str:
    """Calculadora basica tipo menu de opciones

    Args:
        a (_type_): primer operador a mostrar durante el uso de la calculadora
        b (_type_): segundo operador a mostrar durante el uso de la calculadora

    Returns:
        str: Opcion elegida por el usuario
    """
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

def confirmar_salida(confirmacion:str)->bool:
    """confirmacion de salida del programa

    Args:
        confirmacion (str): input del usuario con la opcion

    Returns:
        bool: retorna true o false dependiendo la eleccion del usuario
    """
    while confirmacion != "si" and confirmacion != "no":
        confirmacion = input("Error, Elija solamente [si] o [no]: ").lower()
    
    if confirmacion == "si":
        return True
    return False

def factorial (n:int)->int:
    """Muestra el factorial del numero ingresado

    Args:
        n (int): operador a factorizar

    Raises:
        ValueError: tira error si no es tipo int
        ValueError: tira error si el numero es negativo

    Returns:
        int: resultado del factoreo
    """
    if not isinstance (n,int):
        raise ValueError("Error, se esperaba un entero")
    if n < 0:
        raise ValueError("El número no debe ser un negativo.")
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n -1)
    return fact
