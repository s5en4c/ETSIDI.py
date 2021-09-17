# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:43:02 2021

@author: s5en4
"""
#este programa es un organizador de tiempo. 
#Al principio te pregunta cuantas tareas quieres hacer
#despues indicas la tarea y su tiempo en cada una
#A continuacion se inicia el contador de tiempo
#Para pasar de actividad tienes que pulsar enter
#cuando acabas puedes empezar una nueva rutina

#Se necesitan 3 archivos
# lista de tareas 
# programa de numeros para mostrar el temporizador en consola
# txt con el registro de las rutinas para posteriormente poder analizarlo


# librerias*********************************************************
import pandas as pd # manejar base de datos
import tkinter as Tkinter  
#from datetime import datetime 
import sys, time
import sevseg  # Imports our sevseg.py program.


handle = open("registro.txt", "a")
otra= 1

while otra>0:
    
    #listas guardadas****************************************************************
    mis_datos = pd.read_csv("tareas.txt")

    print(mis_datos)

    # Creamos las listas (vacías al comienzo)
    nombres = []
    tiempos = []

    # Definimos un tamaño para las listas
    # Lo puedes cambiar si quieres

    print("Ingrese el numero de actividades: ")
    tamaño = int(input())

    # Leemos los datos y los agregamos a la lista
    for i in range(tamaño):
        print("Ingrese los datos de la actividad", i + 1)
        print("\n Numero:")
        a=int(input())
        if a>4:
            print("ERROR:no existe esa actividad!! \n repite el numero:")
            a=int(input())
        act=mis_datos.iloc[a]
        nombre = str(act[0])
        tiempo = input("Tiempo: ")

        nombres.append(nombre)
        tiempos.append(tiempo)
        
        
        handle.write(nombres[i])
        handle.write(tiempos[i])
        handle.write("\n")
        
        

    # Ahora mostremos las listas
    for i in range(tamaño):
        print("\n Mostrando los datos de la actividad", i + 1)

        print("Nombre:", nombres[i])
        print("Tiempo:", tiempos[i])
        
        
    print ("\n\n\n START")

    # **********************************contadores***********************************

    for j in range(tamaño):
        # (!) Change this to any number of seconds:
        secondsLeft = int(tiempos[j])
        
        

        try:
            while True:  # Main program loop.
                # Clear the screen by printing several newlines:  
                print('\n' * 60)

                # Get the hours/minutes/seconds from secondsLeft:
                # For example: 7265 is 2 hours, 1 minute, 5 seconds.
                # So 7265 // 3600 is 2 hours:
                hours = str(secondsLeft // 3600)
                # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
                minutes = str((secondsLeft % 3600) // 60)
                # And 7265 % 60 is 5 seconds:
                seconds = str(secondsLeft % 60)

                # Get the digit strings from the sevseg module:
                hDigits = sevseg.getSevSegStr(hours, 2)
                hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

                mDigits = sevseg.getSevSegStr(minutes, 2)
                mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

                sDigits = sevseg.getSevSegStr(seconds, 2)
                sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
                
                print("Actividad:", nombres[j])

                # Display the digits:
                print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
                print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
                print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

                if secondsLeft == 0:
                    print()
                    print('    * * * * FIN * * * *')
                    print(' Pulsa enter para continuar')
                    input()
                    break

                print()
                print('Press Ctrl-C to quit.')
               
                

                time.sleep(1)  # Insert a one-second pause.
                secondsLeft -= 1
        except KeyboardInterrupt:
            print('Countdown, by Al Sweigart al@inventwithpython.com')
            sys.exit()  # When Ctrl-C is pressed, end the program.)
         
            

    print("¿OTRO? \n(pulsa 0 para acabar, otro numero para repetir):")
    otra=int(input())


    
print("HAS ACABADO!!!!!!!!!!!!!!")
handler.close()
