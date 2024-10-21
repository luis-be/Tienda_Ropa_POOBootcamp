class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Precio: ${self.__precio}")


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio)
        self.__cantidad = cantidad
        self.__talla = talla

    def get_cantidad(self):
        return self.__cantidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cantidad: {self.__cantidad}, Talla: {self.__talla}")

    def comprar(self, cantidad_a_comprar):
        if cantidad_a_comprar > self.__cantidad:
            print("No hay suficiente cantidad disponible.")
        else:
            self.__cantidad -= cantidad_a_comprar
            print(f"Has comprado {cantidad_a_comprar} unidades de {self.get_nombre()}.")


class RopaHombre(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

    def mostrar_info(self):
        super().mostrar_info()


class RopaMujer(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

    def mostrar_info(self):
        super().mostrar_info()


class Inventario:
    def __init__(self):
        self.__prendas = [] 

    def agregar_prenda(self, prenda):
        self.__prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario de Prendas:")
        for prenda in self.__prendas:
            prenda.mostrar_info()

    def buscar_prenda(self, nombre):
        for prenda in self.__prendas:
            if prenda.get_nombre() == nombre:
                return prenda
        return None


class Carrito:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_resumen(self):
        total = 0
        print("\nResumen de la compra:")
        for producto in self.__productos:
            producto.mostrar_info()
            total += producto.get_precio()
        print(f"Total a pagar: ${total}")


def menu():
    inventario = Inventario()
    carrito = Carrito()

    inventario.agregar_prenda(RopaHombre("Camisa de Hombre", 25.0, 10, "M"))
    inventario.agregar_prenda(RopaMujer("Blusa de Mujer", 30.0, 5, "S"))

    while True:
        print("\nMenu:")
        print("1. Añadir prenda")
        print("2. Ver inventario")
        print("3. Comprar prenda")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            while True:
                print("\nMenu:")
                print("1. Añadir prenda de Hombre")
                print("2. Añadir prenda de Mujer")
                print("3. Volver al menu principal")

                opcion = input("Selecciona una opción: ")

                if opcion == '1':
                    nombre = input("Nombre de la prenda: ")
                    precio = float(input("Precio: "))
                    cantidad = int(input("Cantidad: "))
                    talla = input("Talla: ")
                    ropa_hombre = RopaHombre(nombre, precio, cantidad, talla)
                    inventario.agregar_prenda(ropa_hombre)

                elif opcion == '2':
                    nombre = input("Nombre de la prenda: ")
                    precio = float(input("Precio: "))
                    cantidad = int(input("Cantidad: "))
                    talla = input("Talla: ")
                    ropa_mujer = RopaMujer(nombre, precio, cantidad, talla)
                    inventario.agregar_prenda(ropa_mujer)

                elif opcion == '3':
                    break
                else:
                    print("Introduce una opción válida")

        elif opcion == '2':
            inventario.mostrar_inventario()

        elif opcion == '3':
            inventario.mostrar_inventario()
            nombre = input("Introduce el nombre de la prenda que deseas comprar: ")
            cantidad = int(input("¿Cuántas unidades deseas comprar?: "))
            prenda = inventario.buscar_prenda(nombre)
            if prenda:
                prenda.comprar(cantidad)
                if cantidad <= prenda.get_cantidad():
                    carrito.agregar_producto(prenda)
            else:
                print("Prenda no encontrada.")

        elif opcion == '4':
            carrito.mostrar_resumen() 
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida, por favor selecciona otra.")


menu()
