from os import system
from msvcrt import getch

productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1]
}



def stock_marca(marca):
    stock_marca(productos,stock)
    clave= int(input("Ingrese Clave: ").title)
    for clave in productos:
            if clave==productos[0]:
                for clave in stock:
                    if clave== stock[1]:
                        stock_marca
            
            



def búsqueda_precio(p_min, p_max):
    for clave in stock:
            if clave== stock[0]:
                if p_min>0:
                    clave[0]= búsqueda_precio
                



def actualizar_precio(modelo, p):
    for modelo, p in productos:
        if modelo[0]==productos:
            if modelo[0]>=1:
                print("La cantidad de Stock de la Marca son: {modelo}")
                if p[0]>0 in productos:
                    PrecioNuevo= int("Ingrese precio nuevo: ")
                    if PrecioNuevo>0:
                        stock[0].pop
                        stock[0].append(PrecioNuevo)
                        
            else:
                print("❌Modelo No valida")  
