# Consulta de Stock de Materiales en base a archivos csv
## Proyecto Final Python Inicial

![ControlDeStock](/Imagenes/ControlDeStock.jpg)


En este proyecto estaremos trabajando con 5 planillas csv donde se podran realizar las consultass de los materiales que tenemos en stock y ademas ir creando una planilla de compras. En esta plnailla de compras el programa nos brindara a que proveedor le tendriamos que comprar dicho producto por tener  el preco mas bajo. Una breve de scripcion de la splnillas que utiliza el programa:

![Planillas](/Imagenes/Planillas.jpg)

Planilla **stock.csv**: en esta planilla tenemos la informacion de los materiales que contamos en stock y el dato de las cantidades que hay en stock de cada material. Esta planilla contiene una columna que se llama **Codigo Interno** que tambien se repite en las plniallas de los **proveedres.csv**, y este es el dato que vincula todas las planillas.

![stock.csv](/Imagenes/stock.csv.jpg)

Planillas **Proveedre.csv**: en estas plniallas encontraremos todos los productos con el mismo **codigo Interno** que se enceuntra dentro de la planilla **stock.csv**, ademas el **precio** y el nombre del **proveedor**.

![Proveedor.csv](/Imagenes/Proveedor.csv.jpg)

Planilla **Compras.csv**: en esta planilla se van guardando los productos que nosotros queremos comprar, ademas se iran guardando a que proveedor se lo devemos comprar junto con su precio. Tambien se guardara el dato de **Codigo Interno**.

![compras.csv](/Imagenes/compras.csv.jpg)

Consulta de stock y consulta de mejor precio de materiales a comprar para una ferretería, la idea seria poder trabajar con una planilla csv la cual contiene el listado de los materiales con un código interno propio de la ferretería, la descripción del material y la cantidad que quedaría en stock. También trabajar con  planillas csv de proveedores, las cuales contendrán la descripción del producto junto con el código interno de la ferretería y el costo del mismo.  
