class ejercicios_pares:

    def ejercicio_dos(self):
        mystr = ""
        total_suma = 0
        total_multiplicacion = 0
        limit = 30
        for x in range(limit):
            mystr = mystr + str(x * 3) + " "
            total_suma = total_suma + x
            total_multiplicacion = total_suma * x
        print("------------------------------------------------------------------------------------------------------")
        print("La secuencia es: ",mystr)
        print("Total de la suma es: ",total_suma)
        print("Total del producto es: ",total_multiplicacion)
        print("----------------------------------------------------------------------------------------------------")

    def ejercicio_cuatro(self, x, y):
        suma = 0
        for z in range(y):
            suma += x
        print(suma)

    def ejercicio_seis(self):
        usuario = None
        while usuario != "f" and usuario != "F":
            mystr = ""
            total_suma = 0
            total_multiplicacion = 0
            limit = 15
            for x in range(limit):
                mystr = mystr + str(x * 2) + " "
                total_suma = total_suma + x
                total_multiplicacion = total_suma * x

            print(mystr)
            print(total_multiplicacion)
            usuario = input("Ingresar F para salir: ")

    def ejercicio_ocho(self):
        numero = input("Ingrese un numero: ")
        print("Binario:",bin(int(numero)))


    def ejercicio_diez(self):
        usuario = None
        while usuario != "f" and usuario != "F":
            mystr = ""
            total_suma = 0
            total_media = 0
            limit = 10
            for x in range(limit):
                mystr = mystr + str(x * 2) + " "
                total_suma = total_suma + x
                total_multiplicacion = total_suma * x
                total_media = total_suma / limit

            print("-----------------------------------------")
            print("La secuencia es:", mystr)
            print("El total del producto es:",total_suma)
            print("La media es: ",total_media)
            print("-----------------------------------------")
            usuario = input("Ingresar F para salir: ")


    def ejercicio_doce(self):
        mayor = None
        menor = None
        lista = []

        for x in range(8):
            lista.append(x + 2 * 2 * 2.5)
        mayor = max(lista)
        menor = min(lista)
        print(lista)
        print("-----------------------------------")
        print("El mayor de la secuencia es:  "+str(mayor))
        print("El menor de la secuencia es:  "+str(menor))
        print("-----------------------------------")

    def ejercicio_catorce(self):
        mystr = ""
        total_suma = 0
        limit = 30
        pares = 0
        for x in range(limit):
            mystr = mystr + str(x * 1) + " "
            total_suma = total_suma + x

        print("------------------------------------------------------------------------------------------------")
        print("La secuencia es:", mystr)
        print("El total del producto es:", total_suma)
        print("pares: ")
        print("-------------------------------------------------------------------------------------------------")


prueba = ejercicios_pares()
prueba.ejercicio_cuatro()
