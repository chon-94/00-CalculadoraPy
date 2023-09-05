import math

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
        5.- Elevación
        6.- Raíz
        7.- Porcentaje
        Seleccione una operación (1/2/3/4/5/6/7): """)

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
        
        elif operacion == '5':
            print("\nELEVACIÓN\n")
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            resultado = base ** exponente
            print(f"Resultado de {base} ^ {exponente}: {resultado}\n")

        elif operacion == '6':
            print("\nRAÍZ\n")
            indice = int(input("Ingresa el índice de la raíz: "))
            numero = int(input("Ingresa el número para calcular su raíz: "))
            
            resultado = numero**(1/indice)

            
            print(f"Raíz {indice} de {numero}: {resultado}\n")

        elif operacion == '7':
            print("\nPORCENTAJE\n")
            numero = int(input("ingrese el numero al que le quieres sacar el porcentaje : "))
            porcen = int(input ("ingrese el porcentaje : "))
            taje =  (porcen/100)
            print (numero*taje)
        
        else:
            print("\nOperación inválida... solo ingresa numeros enteros del 1 al 7")

    calculadora()

    # while True :    
        # continuar = input("Deseas Continuar? - SI/NO: ")
        # if continuar.upper() != "SI" and continuar.upper() != "si" and continuar.upper() != "yes" :
        #     print("\n¡Hasta luego!\n")
        #     break

    # continuar = input("Deseas Continuar? - SI/NO: ")
    # if continuar == "SI" and continuar == "si" and continuar == "yes" :
    #     continue
    # elif continuar == "NO" and continuar == "no" and continuar == "not" :
    #     print("\n¡Hasta luego!\n")
    #     break
    # else :
    #     print("\n¡ingresaste mal algo jejeje!\n")
    #     continue
    while True:
        continuar = input("Deseas Continuar? - SI/NO: ")
        if continuar.upper() in ["SI", "YES"]:
            break
        elif continuar.upper() in ["NO", "NOT"]:
            print("\n¡Hasta luego!\n")
            exit()  
        else:
            print("\n¡Ingresaste algo no válido!\n")
