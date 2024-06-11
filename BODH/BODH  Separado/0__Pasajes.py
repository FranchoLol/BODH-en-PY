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

# Ejemplos de uso
numero, base_inicial = obtener_numero_base()

decimal = TFN(numero, base_inicial)
print(f'Binario: \033[31m{division_sucesiva(decimal, 2)}\033[0m)²\nOctal: \033[31m{division_sucesiva(decimal, 8)}\033[0m)⁸\nDecimal: \033[31m{decimal}\033[0m)¹⁰\nHexadecimal \033[31m{pasaje_por_tablas(decimal, 16)}\033[0m)¹⁶\n\n\n')