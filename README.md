# Consulta de Stock de Materiales con archivos csv
## Proyecto Final Python Inicial

![ControlDeStock](/Imagenes/ControlDeStock.jpg)


En este proyecto estaremos trabajando con 5 planillas csv donde se podran realizar las consultass de los materiales que tenemos en stock y ademas ir creando una planilla de compras. En esta plnailla de compras el programa nos brindara a que proveedor le tendriamos que comprar dicho producto por tener  el preco mas bajo. Abajo hay una breve descripcion de las plnillas que utiliza el programa:

![Planillas](/Imagenes/Planillas.jpg)

### Planilla **stock.csv**: 
En esta planilla tenemos la informacion de los materiales que contamos en stock y el dato de las cantidades que hay en stock de cada material. Esta planilla contiene una columna que se llama **Codigo Interno** que tambien se repite en las plniallas de los **proveedres.csv**, y este es el dato que vincula todas las planillas.

![stock.csv](/Imagenes/stock.csv.jpg)

### Planillas **Proveedre.csv**: 
En estas plniallas encontraremos todos los productos con el mismo **codigo Interno** que se enceuntra dentro de la planilla **stock.csv**, ademas el **precio** y el nombre del **proveedor**.

![Proveedor.csv](/Imagenes/Proveedor.csv.jpg)

### Planilla **Compras.csv**: 
En esta planilla se van guardando los productos que nosotros queremos comprar, ademas se iran guardando a que proveedor se lo devemos comprar junto con su precio. Tambien se guardara el dato de **Codigo Interno**.

![compras.csv](/Imagenes/compras.csv.jpg)

## Breve descripcion del funcionamiento

En la pagina principal el usuario podra seleccion las sigueintes 2 opcines:
  
![Opcines](/Imagenes/Opcines.jpg)

En la primera opción **"consulta de stock"**  vamos a tener 3 cónsulas:

  - poder consultar la planilla completa con el stock de cada material
  - poder realizar una consulta de un material especifico
  - poder consultar los materiales a comprar, se generaría un archivo compra.csv de compra sin ela gregado de los proveedores aun

