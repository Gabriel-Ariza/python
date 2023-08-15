import json
import os
data = {}
data['vendedores'] = []


with open('ventas.txt', 'r') as archivo_txt:
    lines = archivo_txt.readlines()

for linea_list in lines[1:]:
    linea = linea_list.split(",")
    lista = []
    apel = linea[0]
    iden = linea[1]
    ven = linea[2:9]
    lista.extend(ven)

    data['vendedores'].append({
        'Apellido': apel,
        'Id': iden,
        'Ventas': lista
    })
with open('vendedores.json', 'w') as file:
    json.dump(data, file, indent=3)

os.system('clear')
print("\n Archivo creado exitosamente... \n\n")