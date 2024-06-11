# BODH
# BinarioOctalDecimalHexadecimal

def TFN(numero, base_inicial):
    return int(numero, base_inicial)

def division_sucesiva(decimal, base_final):
    resultado = ""
    while decimal > 0:
        resultado = str(decimal % base_final) + resultado
        decimal = decimal // base_final
    return resultado

def pasaje_por_tablas(decimal, base_final):
    tabla = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    while decimal > 0:
        resultado = tabla[decimal % base_final] + resultado
        decimal = decimal // base_final
    return resultado

def obtener_numero_base():
    bases = {'bin': 2, 'oct': 8, 'dec': 10, 'hex': 16}
    while True:
        base_str = input("Ingrese la base (bin, oct, dec, hex): ").lower()
        if base_str in bases:
            numero = input("Ingrese el número en la base {}: ".format(base_str))
            try:
                int(numero, bases[base_str])  # Intenta convertir el número a decimal
                return numero, bases[base_str]
            except ValueError:
                print("El número ingresado no es válido para la base indicada.")
        else:
            print("Base no válida.")

def convertir_a_decimal(numero, base):
    if base == 2:
        return int(numero, 2)
    elif base == 8:
        return int(numero, 8)
    elif base == 10:
        return int(numero)
    elif base == 16:
        return int(numero, 16)
    else:
        return None

def convertir_a_base(numero_decimal, base):
    if base == 2:
        return bin(numero_decimal)[2:]
    elif base == 8:
        return oct(numero_decimal)[2:]
    elif base == 10:
        return str(numero_decimal)
    elif base == 16:
        return hex(numero_decimal)[2:]
    else:
        return None

def suma():
    print("Ingrese la primera base (2, 8, 10, 16):")
    base1 = int(input())
    print("Ingrese el primer número:")
    numero1 = input()

    print("Ingrese la segunda base (2, 8, 10, 16):")
    base2 = int(input())
    print("Ingrese el segundo número:")
    numero2 = input()

    num1_decimal = convertir_a_decimal(numero1, base1)
    num2_decimal = convertir_a_decimal(numero2, base2)

    if num1_decimal is None or num2_decimal is None:
        print("Base no válida.")
        return

    suma_decimal = num1_decimal + num2_decimal

    print("Suma en base binaria:", convertir_a_base(suma_decimal, 2))
    print("Suma en base octal:", convertir_a_base(suma_decimal, 8))
    print("Suma en base decimal:", convertir_a_base(suma_decimal, 10))
    print("Suma en base hexadecimal:", convertir_a_base(suma_decimal, 16))

def resta():
    print("Ingrese la primera base (2, 8, 10, 16):")
    base1 = int(input())
    print("Ingrese el primer número:")
    numero1 = input()

    print("Ingrese la segunda base (2, 8, 10, 16):")
    base2 = int(input())
    print("Ingrese el segundo número:")
    numero2 = input()

    num1_decimal = convertir_a_decimal(numero1, base1)
    num2_decimal = convertir_a_decimal(numero2, base2)

    if num1_decimal is None or num2_decimal is None:
        print("Base no válida.")
        return

    resta_decimal = num1_decimal - num2_decimal

    print("Resta en base binaria:", convertir_a_base(resta_decimal, 2))
    print("Resta en base octal:", convertir_a_base(resta_decimal, 8))
    print("Resta en base decimal:", convertir_a_base(resta_decimal, 10))
    print("Resta en base hexadecimal:", convertir_a_base(resta_decimal, 16))

def multiplicacion():
    print("Ingrese la primera base (2, 8, 10, 16):")
    base1 = int(input())
    print("Ingrese el primer número:")
    numero1 = input()

    print("Ingrese la segunda base (2, 8, 10, 16):")
    base2 = int(input())
    print("Ingrese el segundo número:")
    numero2 = input()

    num1_decimal = convertir_a_decimal(numero1, base1)
    num2_decimal = convertir_a_decimal(numero2, base2)

    if num1_decimal is None or num2_decimal is None:
        print("Base no válida.")
        return

    producto_decimal = num1_decimal * num2_decimal

    print("Producto en base binaria:", convertir_a_base(producto_decimal, 2))
    print("Producto en base octal:", convertir_a_base(producto_decimal, 8))
    print("Producto en base decimal:", convertir_a_base(producto_decimal, 10))
    print("Producto en base hexadecimal:", convertir_a_base(producto_decimal, 16))

def division():
    print("Ingrese la primera base (2, 8, 10, 16):")
    base1 = int(input())
    print("Ingrese el primer número:")
    numero1 = input()

    print("Ingrese la segunda base (2, 8, 10, 16):")
    base2 = int(input())
    print("Ingrese el segundo número:")
    numero2 = input()

    num1_decimal = convertir_a_decimal(numero1, base1)
    num2_decimal = convertir_a_decimal(numero2, base2)

    if num1_decimal is None or num2_decimal is None:
        print("Base no válida.")
        return

    if num2_decimal == 0:
        print("No se puede dividir por cero.")
        return

    division_decimal = num1_decimal / num2_decimal

    print("División en base binaria:", convertir_a_base(int(division_decimal), 2))
    print("División en base octal:", convertir_a_base(int(division_decimal), 8))
    print("División en base decimal:", convertir_a_base(int(division_decimal), 10))
    print("División en base hexadecimal:", convertir_a_base(int(division_decimal), 16))

if __name__ == "__main__":
    print("1. Pasaje entre bases")
    print("2. Suma")
    print("3. Resta")
    print("4. Multiplicación")
    print("5. División")

    opcion = int(input("Seleccione una operación (1-5): "))

    if opcion == 1:
        numero, base_inicial = obtener_numero_base()
        decimal = TFN(numero, base_inicial)
        print(f'Binario: \033[31m{division_sucesiva(decimal, 2)}\033[0m)²\nOctal: \033[31m{division_sucesiva(decimal, 8)}\033[0m)⁸\nDecimal: \033[31m{decimal}\033[0m)¹⁰\nHexadecimal \033[31m{pasaje_por_tablas(decimal, 16)}\033[0m)¹⁶\n\n\n')
    elif opcion == 2:
        suma()
    elif opcion == 3:
        resta()
    elif opcion == 4:
        multiplicacion()
    elif opcion == 5:
        division()
    else:
        print("Opción no válida.")