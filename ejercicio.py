import json
import os
import time
jugadores = {}

def agregar_json(nombre, edad, peso):
    jugadores[nombre] = []
    jugadores[nombre].append({
        'edad': edad,
        'peso': peso
    })

    with open('jugadores.json', 'w') as archivo:
        json.dump(jugadores, archivo, indent=3)

def msg(mensaje, duracion):
    print(mensaje, end='', flush=True)
    time.sleep(duracion)
    print("\r" + " " * len(mensaje), end='', flush=True)

def validacion(numero):
    while True:
        try:
            convertir = int(numero)
            if convertir >= 0:
                break
        except ValueError:
            msg(" ===  Introduzca Un Valor Válido  === ", 3)
            numero = input("\n\nIngresa El Dato Nuevamente:  ").strip() 
    return convertir

ciclo = True
while ciclo:
    nombre = input("Ingrese Nombre Del Jugador:  ")
    edad = validacion(input("Ingrese La Edad Del Jugador:  "))
    peso = validacion(input("Ingrese Peso Del Jugador:  "))
    agregar_json(nombre, edad, peso)

    respuesta = input("¿Desea agregar otro jugador? (si/no): ")
    if respuesta.lower() == "no":
        ciclo = False
        print("Fin Del Progama ...")
        time.sleep(2)
        os.system('clear')
        lectura = "jugadores.json"
        abriendo = open(lectura, "r").read()
        data = json.loads(abriendo)
        for jugador, detalles in data.items():
            for detalle in detalles:
                edad = detalle["edad"]
                peso = detalle["peso"]
                print(f"Jugador: {jugador}, Edad: {edad}, Peso: {peso}")