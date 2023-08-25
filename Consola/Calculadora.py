while True:

    def Suma(valores):
        return sum(valores)

    def Resta(valores):
        result = valores[0]
        for valor in valores[1:]:
            result -= valor
        return result

    def Division(a,b):
        if b != 0:
            return a / b
        else:
            return "No se puede dividir por cero"

    def Multiplicacion(valores):
        result = 1
        for valor in valores:
            result *= valor
        return result

    def calculadora():
        operacion = input("""
        Bienvenido a la calculadora
        1.- Suma 
        2.- Resta 
        3.- Division 
        4.- Multiplicacion 
        Seleccione una operación (1/2/3/4): """)

        if operacion == '1':
            print("\nSUMA\n")
            cantidad = int(input("Ingresa la cantidad de números que deseas operar: "))
            valores = []

            for i in range(cantidad):
                valor = float(input(f"Ingrese el valor {i + 1}: "))
                valores.append(valor)

            print("Resultado:", Suma(valores),"\n")
        
        elif operacion == '2':
            print("\nRESTA\n")
            cantidad = int(input("Ingresa la cantidad de números que deseas operar: "))
            valores = []
            
            for i in range(cantidad):
                valor = float(input(f"Ingrese el valor {i + 1}: "))
                valores.append(valor)
            print("Resultado:", Resta(valores))
            
        elif operacion == '3':
            print("\nSUMA\n")
        
            n1 = float(input("Ingresa el numerador: "))
            n2 = float(input("Ingresa el denominador: "))
            print("Resultado:", Division(n1, n2))
            
        elif operacion == '4':

            cantidad = int(input("Ingresa la cantidad de números que deseas multiplicar: "))
            valores = []

            for i in range(cantidad):
                valor = float(input(f"Ingrese el valor {i + 1}: "))
                valores.append(valor)

            resultado = Multiplicacion(valores)
            print("Resultado de la multiplicación:", resultado)    
            
        else:
            print("\nOperación inválida... solo ingresa numeros enteros del 1 al 4")
            # continue        

    calculadora()

    continuar = input("Deseas Continuar? - SI/NO: ")
    if continuar.upper() != "SI":
        print("\n¡Hasta luego!\n")
        break