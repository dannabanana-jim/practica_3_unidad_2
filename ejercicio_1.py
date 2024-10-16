print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
#1- Guardar en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
#El usuario debe meter una divisa y debe mostrar el símbolo o un mensaje de que la divisa no está en el diccionario.

# Diccionario de divisas
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Solicitar al usuario que ingrese una divisa
divisa_input = input("Introduce una divisa (Euro, Dollar, Yen): ")

# Mostrar el símbolo o un mensaje de error
if divisa_input in divisas:
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")
else:
    print("La divisa no está en el diccionario.")
print (" ")