import random

def generarRegistrosAleatorios(numRegistros=2000):
    municipiosFicticios = ["Medellin", "Bello", "Envigado", "Itagui", "Sabaneta", "Rionegro", "LaCeja", "Caldas", "Guarne", "Copacabana"]
    tiposArbolesFicticios = ["Pino", "Eucalipto", "Roble", "Cedro", "Nogal", "Palmira", "Mango", "Aguacate", "Naranjo", "Papaya"]

    registrosFicticios = []

    for _ in range(numRegistros):
        municipio = random.choice(municipiosFicticios)
        tipoArbol = random.choice(tiposArbolesFicticios)
        cantidad = random.randint(1, 100)
        registrosFicticios.append({"Municipio": municipio, "TipoArbol": tipoArbol, "Cantidad": cantidad})

    return registrosFicticios


registros = generarRegistrosAleatorios(100)


for registro in registros[:10]:
    print(registro)