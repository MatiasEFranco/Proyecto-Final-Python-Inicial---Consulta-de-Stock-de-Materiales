from ast import Try
from asyncore import write
import csv
from re import I

'''///////////////////////////////////////////////////////////////////////////////////'''
def abrir_archivo(dato1,dato2):

    archivo = dato1
    formato = dato2
    with open (archivo,formato) as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
        planilla_info = list(csv.DictReader(planilla_csv))
        return planilla_info

    


def mostrar_lista(dato):
    lista = dato

    for i in lista:

        print(i)
        

def consultar_materiales(dato):
    
    archivo = abrir_archivo(dato,'r')

    ##with open (archivo,'r') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
      ##  planilla_info = list(csv.DictReader(planilla_csv))

    while True:
        indice = None
        print("Por favor ingrese el codigo interno del material a consultar")

        try:    
            codigo_material = int(input())

            for i in range(len(archivo)):
                if codigo_material == int(archivo[i].get('ï»¿Codigo Interno')):
                    indice = i
        
            if indice != None:
                print(archivo[indice])
                if archivo[indice].get('Cantidad de stock') == '' or int(archivo[indice].get('Cantidad de stock')) == 0 :
                    print("El material",archivo[indice].get('ï»¿Codigo Interno'), "no cuenta con stock" )
                    print("Agregar a la lista de Compras? SI/N0")
                    material_agregar  = input()
                    if material_agregar.lower() == 'si':
                        compra_material(indice,archivo)
                    elif material_agregar.lower() == 'no':
                        print("No se agrego el material a la compra")
                    else:
                        print("Se introdujo un valor erroneo")


            else:
                print("El valor ingrresado no esta dentro del stock") 
            
            print("Desea Realizar otra Consulta? SI/NO")

            consulta = volver_inicio(input())
   
            if consulta.lower() == 'no':
                print("Volvera al Inicio")
                break
            elif consulta.lower() == 'si':
                continue

        except:
            print("Se ingreso un valor erroneo, intentelo de nuevo")
            continue


def volver_inicio(info):
    dato = info

    while dato.lower() != "si":
        if dato.lower() == "si":
            return dato
        elif dato.lower() == "no":
            return dato
        else:
            print("Se introdujo un dato erroneo, intentelo de nuevo")
            dato = input()
    return dato


def compra_material(indice,archivo):
    codigo_interno = archivo[indice].get('ï»¿Codigo Interno')
    print("Indicar cantidad a comprar")
    cantidad = int(input())
    header = ['Codigo Interno','Cantidad a comrpar','Proveedor','Precio Unitario','Precio Total']
    material = {'Codigo Interno': codigo_interno, 'Cantidad a comrpar':cantidad,'Proveedor':'no definido','Precio Unitario':0,'Precio Total':0}
    with open ('compras.csv', 'a', newline='') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            write = csv.DictWriter(planilla_csv, fieldnames=header)
            write.writerow(material)
            
    
def comparar_precios(codigo_material, indice,cantidad):
    archivo_preveedor1 = abrir_archivo('Proveedor-1.csv','r')
    archivo_preveedor2 = abrir_archivo('Proveedor-2.csv','r')
    archivo_preveedor3 = abrir_archivo('Proveedor-3.csv','r')
    
    for i in range(len(archivo_preveedor1)):
        #print(archivo_preveedor1[i].get('ï»¿Codigo Interno '))
        #print(codigo_material)
        if archivo_preveedor1[i].get('ï»¿Codigo Interno ') == codigo_material:
            precio_proveedor1 = archivo_preveedor1[i].get('Precio')
            proveedor1 = archivo_preveedor1[i].get('Nombre del Proveedor')
            indice_proveedor1 = i
            #print(precio_proveedor1)
            #print(proveedor1)
            #print(indice_proveedor1)
    for i in range(len(archivo_preveedor2)):
        if archivo_preveedor2[i].get('ï»¿Codigo Interno ') == codigo_material:
            precio_proveedor2 = archivo_preveedor2[i].get('Precio')
            proveedor2 = archivo_preveedor2[i].get('Nombre del Proveedor')
            indice_proveedor2 = i
            #print(precio_proveedor2)
            #print(proveedor2)
            
    for i in range(len(archivo_preveedor3)):
        if archivo_preveedor3[i].get('ï»¿Codigo Interno ') == codigo_material:
            precio_proveedor3 = archivo_preveedor3[i].get('Precio')
            proveedor3 = archivo_preveedor3[i].get('Nombre del Proveedor')
            indice_proveedor3 = i
            #print(precio_proveedor3)
            #print(proveedor3)
    
    if precio_proveedor1 <= precio_proveedor2 and precio_proveedor1 <= precio_proveedor3:
        with open ('compras.csv') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            listado = list(csv.DictReader(planilla_csv))
            listado[indice]['Proveedor'] = proveedor1
            listado[indice]['Precio Unitario'] = precio_proveedor1
            listado[indice]['Precio Total'] = int(precio_proveedor1)*int(cantidad)
            #print(listado[indice]['Precio Total'])            

        with open ('compras.csv','w',newline='') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            header = ['Codigo Interno','Cantidad a comrpar','Proveedor','Precio Unitario','Precio Total']
            writer = csv.DictWriter(planilla_csv, fieldnames=header)
            writer.writeheader()
            writer.writerows(listado)
    if precio_proveedor2 < precio_proveedor1 and precio_proveedor2 < precio_proveedor3:
        with open ('compras.csv') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            listado = list(csv.DictReader(planilla_csv))
            listado[indice]['Proveedor'] = proveedor2
            listado[indice]['Precio Unitario'] = precio_proveedor2
            listado[indice]['Precio Total'] = int(precio_proveedor2)*int(cantidad)
                        

        with open ('compras.csv','w',newline='') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            header = ['Codigo Interno','Cantidad a comrpar','Proveedor','Precio Unitario','Precio Total']
            writer = csv.DictWriter(planilla_csv, fieldnames=header)
            writer.writeheader()
            writer.writerows(listado)
    if precio_proveedor3 < precio_proveedor2 and precio_proveedor3 < precio_proveedor2:
        with open ('compras.csv') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            listado = list(csv.DictReader(planilla_csv))
            listado[indice]['Proveedor'] = proveedor3
            listado[indice]['Precio Unitario'] = precio_proveedor3
            listado[indice]['Precio Total'] = int(precio_proveedor3)*int(cantidad)
                        

        with open ('compras.csv','w',newline='') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
            header = ['Codigo Interno','Cantidad a comrpar','Proveedor','Precio Unitario','Precio Total']
            writer = csv.DictWriter(planilla_csv, fieldnames=header)
            writer.writeheader()
            writer.writerows(listado)



'''///////////////////////////////////////////////////////////////////////////////////'''

'''///////////////////////////////////////////////////////////////////////////////////'''



if __name__ == '__main__':
    
    while True:
        print('''Que desea realizar:
                A- Realizar Consultas
                B- Compras''' )

        tarea = input()

        if tarea.lower() == "a":
            
            while True:
                print('''Que Opcion de Consulta desea realizar:
                1- Consulta el stock total
                2- Consultar materiales
                3- Consultar materiales a comprar
                4- Volver atras''')

                consulta = input()

                if consulta == "1":                
                    planilla_stock = abrir_archivo('stock.csv','r')
                    mostrar_lista(planilla_stock)
                    
                elif consulta == "2":
                    consultar_materiales('stock.csv')

                elif consulta == "3":
                    compra_materiales = abrir_archivo('compras.csv','r')
                    mostrar_lista(compra_material)

                elif consulta == "4":
                    break

                else:
                    print("Se ingreso un valor erroneo")     
   
        elif tarea.lower() == "b":
            codigo_material = 0
            archivo = abrir_archivo('compras.csv','r')
           
            if len(archivo) < 1:        
                print("El archivo de Compas esta Vacio")
            
            else:
                for i in range(len(archivo)):
                    codigo_material = archivo[i].get('Codigo Interno')
                    cantidad = archivo[i].get('Cantidad a comrpar')
                    indice = i
                    #print(codigo_material)
                    #print(indice)
                    #print(cantidad)
                    comparar_precios(codigo_material, indice, cantidad)
                    
                while True:
                    print("imprimir lista de compra? SI/NO")
                    imprimir = input()
                        
                    if imprimir.lower() == 'si':
                        archivo = abrir_archivo('compras.csv','r')
                        print(archivo)
                        print("Volviendo al Inicio")
                        break
                    elif imprimir.lower() == 'no':
                        print("Volviendo al Inicio")
                        break
                    else:
                        print("Se introdujo un comando erroneo")
        else: 
            print("Se ingreso un valor erroneo")
            continue