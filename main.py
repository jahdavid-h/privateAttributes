# total.py
from classVenta import Producto, Carrito


def main():
    carrito = Carrito()

    for i in range(1, 4):
        producto = Producto()  # Crea el objeto Producto

        print(f'Producto {i}')

        cantidad = int(input(f"Ingrese la cantidad del Producto {i}: "))
        producto.set_cantidad(cantidad)

        precio = float(input(f"Ingrese el precio del Producto {i}: "))
        producto.set_precio(precio)

        print("")

        carrito.agregar_producto(producto)

    carrito.mostrar_detalles()


if __name__ == "__main__":
    main()
