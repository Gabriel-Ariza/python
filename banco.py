import json
i= 0
with open('ahorradores.json', 'r') as lectura:
    archivo = json.load(lectura)

    for cliente, valores in archivo.items():
        for key in valores:
            i+= 1
            id = key["Id"]
            nombre = key["Nombre"]
            cuenta = key["NumCuenta"]
            saldo = key["Saldo"]

            print(f"Nombre: {nombre}")
            print(f"Id: {id}")
            print(f"NumCuenta: {cuenta}")
            print(f"Saldo: {saldo}")
            print("="*30)

            if saldo > 35_000_000:
                data = {}
                data['cliente'] = []
                data['cliente'].append({

                    #'Nombre': nombre,
                    'consecutivo': i,
                    'Id': id,
                    #'NumCuenta': cuenta,
                    'Saldo': saldo
                })

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)