import random
import pandas as pd

def generarRegistrosAleatorios(numRegistros=2000):
    municipios = ["Medellin", "Bello", "Envigado", "Itagui", "Sabaneta", "Rionegro", "LaCeja", "Caldas", "Guarne", "Copacabana"]
    tiposArboles = ["Pino", "Eucalipto", "Roble", "Cedro", "Nogal", "Palmira", "Mango", "Aguacate", "Naranjo", "Papaya"]

    registros = []

    for _ in range(numRegistros):
        municipio = random.choice(municipios)
        tipoArbol = random.choice(tiposArboles)
        cantidad = random.randint(1, 100)
        registros.append({"Municipio": municipio, "TipoArbol": tipoArbol, "Cantidad": cantidad})

    return registros


registros = generarRegistrosAleatorios(100)


df = pd.DataFrame(registros)


print(df.head(10))
