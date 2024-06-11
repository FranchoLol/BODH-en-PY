def convertir_base(numero, base_inicial):
    try:
        numero_decimal = int(numero, base_inicial)
        resultados = {}
        for base_final in [2, 8, 10, 16]:
            if base_final == 2:
                resultados["Binario"] = bin(numero_decimal)[2:]
            elif base_final == 8:
                resultados["Octal"] = oct(numero_decimal)[2:]
            elif base_final == 10:
                resultados["Decimal"] = str(numero_decimal)
            elif base_final == 16:
                resultados["Hexadecimal"] = hex(numero_decimal)[2:]
        return resultados
    except ValueError:
        return {"Error": "Número no válido."}

def operacion_aritmetica(operacion):
    try:
        print("Ingrese la primera base (2, 8, 10, 16):")
        base1 = int(input())
        print("Ingrese el primer número:")
        numero1 = input()

        print("Ingrese la segunda base (2, 8, 10, 16):")
        base2 = int(input())
        print("Ingrese el segundo número:")
        numero2 = input()

        num1_decimal = int(numero1, base1)
        num2_decimal = int(numero2, base2)

        if operacion == "+":
            resultado_decimal = num1_decimal + num2_decimal
        elif operacion == "-":
            resultado_decimal = num1_decimal - num2_decimal
        elif operacion == "*":
            resultado_decimal = num1_decimal * num2_decimal
        elif operacion == "/":
            if num2_decimal == 0:
                return {"Error": "No se puede dividir por cero."}
            resultado_decimal = num1_decimal / num2_decimal
        else:
            return {"Error": "Operación no válida."}

        return convertir_base(str(int(resultado_decimal)), 10)

    except ValueError:
        return {"Error": "Base no válida."}

if __name__ == "__main__":
    print("1. Pasaje entre bases\n2. Suma\n3. Resta\n4. Multiplicación\n5. División")

    opcion = int(input("Seleccione una operación (1-5): "))

    if opcion == 1:
        print("Ingrese la base (2, 8, 10, 16):")
        base_inicial = int(input())
        numero = input("Ingrese el número: ")
        print("Resultados:")
        resultados = convertir_base(numero, base_inicial)
        for base, resultado in resultados.items():
            print(f"{base}: {resultado}")
    elif opcion in [2, 3, 4, 5]:
        resultados_operacion = operacion_aritmetica("+-*/"[opcion - 2])
        if "Error" in resultados_operacion:
            print(resultados_operacion["Error"])
        else:
            print("Resultado en todas las bases:")
            for base, resultado in resultados_operacion.items():
                print(f"{base}: {resultado}")
    else:
        print("Opción no válida.")