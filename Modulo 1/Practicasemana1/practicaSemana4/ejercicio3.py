meses={
    "1": "enero",
    "2": "febrero",
    "3": "marzo",
    "4": "abril",
    "5": "mayo",
    "6": "junio",
    "7": "julio",
    "8": "agosto",
    "9": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}


fecha=input("Ingrese la fecha en formato dd/mm/aaaa:")
fecha_lista=fecha.split("/")
mes=fecha_lista[1]

print(f'{fecha_lista[0]} de {meses[mes]} de {fecha_lista[2]}')