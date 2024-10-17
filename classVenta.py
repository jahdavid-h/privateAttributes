# productos.py

class Producto:

    __cantidad = None
    __precio = None

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

class Carrito:
    __productos = None  # Lista de productos

    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def calcular_precif(self):
        total = 0
        for producto in self.__productos:
            total = producto.get_cantidad() * producto.get_precio()
        return total

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_cantidad() * producto.get_precio()
        return total

    def mostrar_detalles(self):
        print("")
        print("Detalles del carrito:")

        for producto in self.__productos:
            print(f"Producto, Cantidad: {producto.get_cantidad()}, Precio x Productos: ${producto.get_precio()}, Precio: {self.calcular_precif()}")
        total = self.calcular_total()
        print(f"Total a pagar: ${total:.2f}")
