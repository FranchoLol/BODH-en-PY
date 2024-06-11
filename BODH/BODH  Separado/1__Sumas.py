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


def main():
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

if __name__ == "__main__":
    main()
