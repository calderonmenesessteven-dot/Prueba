def calculadora():
    print ("Bienvenido a la calculadora")
    print ("Operaciones disponibles:")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicación")
    print ("4. División")

    continuar = "si"

    while continuar.lower() == "si":
        #Pedir datos al usuario
        Num1 = float(input("Ingrese el primer número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")
        Num2 = float(input("Ingrese el segundo número: "))

        #Realizar la operación
    if operacion == "+":
                    resultado = Num1 + Num2
                    print(f"El resultado de la suma es: {resultado}")
    elif operacion == "-":
                    resultado = Num1 - Num2
                    print(f"El resultado de la resta es: {resultado}")
    elif operacion == "*":
                    resultado = Num1 * Num2
                    print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == "/":
                    if Num2 != 0:
                        resultado = Num1 / Num2
                        print(f"El resultado de la división es: {resultado}")
                    else:
                        print("Error: No se puede dividir entre cero.")
    else:
                    print("Operación no válida. Por favor, ingrese una operación correcta.")

        