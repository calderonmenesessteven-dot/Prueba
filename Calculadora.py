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
        