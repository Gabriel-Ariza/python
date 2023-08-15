import json

data = {}
data['clientes'] = []
data['clientes'].append({

    'first_name': 'Theodoric',
    'last_name': 'rivers',
    'age': 21,
    'amount': 1.11
})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

lectura = open('data.json', 'r')
archivo = json.load(lectura)

texto = archivo['clientes'][0]
texto = '\n'.join(str(elem) for elem in texto)

print(texto)
lectura.close()