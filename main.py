#Programa para gestion de productos
#En una lista de mercado
nombreUsuario=None

#Declarando las variables
productos=[]
producto={}

#crear un menu de opciones
print("*** MerqueoAPP ***")
print("1. Agregar Producto a tu lista de mercado")
print("2. Mostrar tu lista de mercado")
print("3. Modificar tu lista de mercado")
print("4. Retirar producto de tu lista de mercado")
print(" Presiona 5 para SALIR")

opcion=100
while opcion != 5:
    opcion=int(input("Digita una opcion del menu: "))

    if opcion == 1:
        print("Creando la lista")
        #Poblando listas y diccionarios en python 

        #Asignando claves a un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["presentacion"]=input(" Digita la presentacion del producto: ")
        producto["cantidad"]=int(input("Digita la cantidad: "))
        producto["precio"]=int(input("Digita el precio del producto: "))

        #Asignando a una lista un diccionario
        productos.append(producto)
        print(productos)


    elif opcion == 2:
        print("Mostrando la lista")
    elif opcion == 3:
        print("Modificando la lista")
    elif opcion == 4:
        print("Retirando un producto")
    else:
        print("Opcion invalida")
    
    
