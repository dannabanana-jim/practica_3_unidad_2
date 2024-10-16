print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
#2- Preguntar al usuario nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje 

# Solicitar datos al usuario
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu direccion: ")
telefono = input("Introduce tu numero de telefono: ")

# Guardar los datos en un diccionario
datos_usuario = {
    'Nombre': nombre,
    'Edad': edad,
    'Dirección': direccion,
    'Teléfono': telefono
}

# Mostrar el mensaje con los datos
print("\nDatos ingresados:")
print(f"Nombre: {datos_usuario['Nombre']}")
print(f"Edad: {datos_usuario['Edad']}")
print(f"Dirección: {datos_usuario['Dirección']}")
print(f"Teléfono: {datos_usuario['Teléfono']}")

print (" ")

