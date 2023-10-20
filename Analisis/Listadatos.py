import random

# Lista de municipios 
municipiosFicticios = ["Medellin", "Bello", "Envigado", "Itagui", "Sabaneta", "Rionegro", "LaCeja", "Caldas", "Guarne", "Copacabana"]

# Lista de tipos de árboles 
tiposArbolesFicticios = ["Pino", "Eucalipto", "Roble", "Cedro", "Nogal", "Palmira", "Mango", "Aguacate", "Naranjo", "Papaya"]

# Creación de 2000 registros 
registrosFicticios = []
for _ in range(2000):
    municipio = random.choice(municipiosFicticios)
    tipoArbol = random.choice(tiposArbolesFicticios)
    cantidad = random.randint(1, 100)
    registrosFicticios.append({"Municipio": municipio, "TipoArbol": tipoArbol, "Cantidad": cantidad})


for registro in registrosFicticios[:2000]:
    print(registro)