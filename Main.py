
from Funciones import*
from os import system
from msvcrt import getch


print("""
****Menu Principal***
1) Stock por Marca
2) Búsqueda por Precio
3) Actualizar Precio
4) Salir          
      """)




while True:
    Opcion= int(input("Seleccione una opción: "))

    if Opcion==1:
        stock_marca(productos,stock)
        clave= int(input("Ingrese Clave: ").title)
        for clave in productos:
            if clave==productos[0]:
                for clave in stock:
                    if clave== stock[1]:
                        stock_marca(stock[1])
    if Opcion==2:
        búsqueda_precio(p_max,p_min,clave)
        p_min = int("Ingrese Precio Minimo: ")
        p_max = int("Ingrese Precio Maximo: ")
        for clave in stock:
            if clave== stock[0]:
                if p_min>0:
                    clave[0]= búsqueda_precio
    if Opcion==3:
        actualizar_precio(clave, búsqueda_precio, productos, stock )
        clave= int(input("Ingrese Clave: "))
        if clave in productos or stock:
            if clave== stock[0]:
                 clave=int(input("Ingrese Precio Nuevo: "))
                 if clave<=0:
                  print("El precio debe ser mayor a 0")
                  if clave>0:
                    print("EL Precio Nuevo es: {clave}")
                    actualizar_precio[
                        
                        'modelo':[clave,stock]
                    ]
                    actualizar_precio(stock[0])
        else:
            print("El modelo no existe")
            False
    if Opcion==4:
        print("Programa finalizado✅")
    else:
        print("Opción NO Valida❌")

















"""
Opcion= int(input("Seleccione una opción: "))

while True:
    
    if Opcion==1:    
            clave = input(int("Ingrese la marca: "))
            if clave[0] in stock_marca:
                stock_marca(clave[0]) 
    if Opcion==2:
             
             PrecioMin = int("Ingrese Precio Minimo:")
             PrecioMax = int("Ingrese Precio Maximo")
             if PrecioMin>0:
                   print(stock[PrecioMin] and [PrecioMax])
                  
                  
            
    if Opcion==3:
        Clave = int(input("Ingrese Clave: "))
        if Clave in stock:
              print("La Clave si existe ")
              Clave= input("Desea Modificarlo S/N:").upper()
              if Clave=="S":
                    PrecioNuevo = int("Ingrese Precio Nuevo: ")
                    stock[
                    'Clave':''["PrecioNuevo":PrecioNuevo[0], "Stock":[1] ]   
                    ]
                    
    if Opcion==4:
        print("Programa Finalizado")
        break
    else:

        print("Debe seleccionar una opción válida!!❌")

"""
