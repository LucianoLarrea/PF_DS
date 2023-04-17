# Este código está leyendo un archivo CSV llamado 'NombreArchivo.csv' utilizando la función pd.read_csv() de pandas 
# y guardando los datos en un DataFrame llamado 'data'. Luego, está conectando a una base de datos MySQL utilizando 
# la librería pymysql y creando un cursor para realizar operaciones en la base de datos.

import pymysql
from pandas.io import sql
import sqlalchemy as db
import pandas as pd
## seleccionar datos

data = pd.read_csv('/Users/lucianolarrea/Desktop/M3/CP M3/Tablas Sucursales/Comisiones Córdoba Quiróz.csv', delimiter=';')


##conectar con mysql

conexion = pymysql.connect(
   host = 'localhost',
   user = 'root',
   passwd = 'Henry2022',
   db = 'henry_checkpoint_m3'
)

cursor  = conexion.cursor()

# Después, está usando el método fillna() de pandas para reemplazar los valores faltantes en el DataFrame 
# con una cadena vacía y luego imprime el DataFrame para verificar los datos.
##Checar datos faltantes y visualizar datos 
data.fillna('',inplace=True)
print (data)

# Este código está tomando el DataFrame 'data' y convirtiéndolo en una lista de tuplas utilizando 
# el método to_records() de pandas y la función tuple(). 
# Esto es necesario para insertar los datos en la tabla de la base de datos utilizando el método executemany() del cursor.
##convertir csv a lista de tuplas y creación de query con columnas hacia donde van los datos importados
data_imp=  [tuple(x) for x in data.to_records(index=False)]   ##Se necesita convertir a lista de tuplas

#La variable 'query' contiene una cadena de consulta SQL que inserta datos en la tabla 'cliente' y especifica los nombres 
# de las columnas en las que se insertarán los datos. Los valores a insertar son marcados con signos de porcentaje '%s' 
# y se corresponden con los valores en las tuplas de la lista 'data_imp'.
query = 'INSERT INTO Quiroz2 (CodigoEmpleado, IdSucursal, Apellido_y_Nombre, Sucursal, Anio, Mes, Porcentaje) VALUES (%s,%s,%s,%s,%s,%s,%s)'
#El método executemany() ejecuta la consulta SQL con todas las tuplas en la lista 'data_imp', 
# insertando varios registros en la tabla a la vez.
cursor.executemany(query,data_imp)
# Utiliza el método commit() de la conexión para confirmar los cambios en la base de datos.
## necesario para enviar datos a mysql
conexion.commit()
# Cierra el cursor y la conexión para liberar recursos y evitar problemas al modificar otras cosas en la base de datos.
## una vez terminado poner en otra celda para cerrar conexión y no tener problemas al modificar cosas en mysql
cursor.close()
conexion.close()