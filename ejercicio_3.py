print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#3- Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por fruta, 
#un número de kilos mostrar el precio de ese número de kilos de fruta

# Diccionario con precios de frutas por kilo
precios_frutas = {
    'manzana': 2.80,
    'banana': 1.2,
    'naranja': 2.45,
    'uva': 4.75
}

# Solicitar al usuario la fruta y la cantidad de kilos
fruta = input("Introduce el nombre de la fruta (manzana, banana, naranja, uva): ").lower()#convierte la entrada a minúsculas
kilos = float(input("Introduce el número de kilos: "))                                    # para que sea más fácil de comparar con las claves del diccionario

# Calcular y mostrar el precio
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: ${precio_total:.2f}")
else:
    print("La fruta no está en el diccionario.")

print (" ")

