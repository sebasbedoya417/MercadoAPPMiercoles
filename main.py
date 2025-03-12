#Programa para gestion de productos
#En una lista de mercado
nombreUsuario=None

#Declarando las variables
productos=[]
contador=0

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

    if opcion == 1:        #Poblando listas y diccionarios en python 

        #Asignando claves a un diccionario
        producto={}
        contador=contador+1
        producto["id"]=contador
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["presentacion"]=input(" Digita la presentacion del producto: ")
        producto["cantidad"]=int(input("Digita la cantidad: "))
        producto["precio"]=int(input("Digita el precio del producto: "))

        #Asignando a una lista un diccionario
        productos.append(producto)


    elif opcion == 2:

        #Recorriendo una lista de diccionarios
        for productoiterador in productos:
            print(f"id Producto:{productoiterador['id']}")
            print(f"Nombre Producto:{productoiterador['nombre']}")
            print(f"Nombre Precio:{productoiterador['precio']}")

    elif opcion == 3:
        #preguntar al usuario que producto desea modificar
        idProductoAbuscar=int(input("Digita el id del producto a modificar: "))
         #recorrer la lista de productos
        for productoBuscado in productos:
            if idProductoAbuscar == productoBuscado["id"]:
                print("Producto encontrado")
                break
            else:
                print("Producto no encontrado")
        #modificar la o las propiedades del producto

            
    elif opcion == 4:
        print("Retirando un producto")
    else:
        print("Opcion invalida")
    
    
