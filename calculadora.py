from def_funciones import *

a = validar_entero("Ingrese el operador A: ")

b = validar_entero("Ingrese el operador B: ")

while True:
    match menu_calculadora(a,b):
        case "1":
            print("Selecciono [Sumar]")
            print(f"El resultado de {a} + {b} es: {sumar(a,b)}")
        
        case "2":
            print("Selecciono[Restar]")
            print(f"El resultado de {a} - {b} es: {restar(a,b)}")
        
        case "3":
            print("Selecciono [Dividir]")
            print(f"El resultado de {a} / {b} es: {divicion(a,b)}")
        
        case "4":
            print("Selecciono [Multiplicar]")
            print(f"El resultado de {a} * {b} es: {multiplicar(a,b)}")
    
        case "5":
            print("Selecciono [Factorial]")
            print(f"El Factorial de {a} es: {factorial(a)} y el factorial de {b} es: {factorial(b)}")
    
        case "6":
            opcion = input("Confirmas que quiere salir? elija 'si' o 'no': ").lower()
            resultado = confirmar_salida(opcion)
            if resultado:
                break
    
    
    
    
    pausar()



