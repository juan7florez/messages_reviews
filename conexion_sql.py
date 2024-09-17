import os 
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

def connect_and_query():
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host='db-capitalpocket.cumig8edpvmh.us-east-1.rds.amazonaws.com',  # Cambia si es necesario
            database='cpocketbot',  # Cambia el nombre de tu DB
            user='Cp0ck3t4dm1n',  # Cambia por tu usuario
            password='+nY^6fgNbTg+F*qTgqkv&IwER7drYdPZaxHzq#ck3'  # Cambia por tu contraseña
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            # Crear un cursor para ejecutar la consulta
            cursor = connection.cursor()
            
            query1 = os.getenv('QUERY')
            # Ejecutar la consulta SQL para obtener los primeros 100 registros
            # query_1 = "SELECT idauditTrail, phone, LOWER(message), creationdate, modificationdate \
            #         FROM cpocketbot.auditTrail\
            #         WHERE \
	        #         phone NOT IN ('573113172984', '573506217627',	'573045239673',	'573215086949',\
            #         '573043361388',	'573108758159',	'573008598735',	'13054679681',\
            #         '573004489677',	'573127949986',	'573117051810', '573024483131',\
            #         '573194214452')\
	        #         AND type LIKE (1)\
            #         AND typeMessage LIKE ('text');"
            cursor.execute(query1)
            # Obtener los resultados
            records = cursor.fetchall()
            
            print('Otro resultados')
            
            return records 
            
            # query2 = "SELECT COUNT(*) AS Total FROM auditTrail"
            # cursor.execute(query2)
            
            # records2 = cursor.fetchall()
            # Mostrar los resultados
            
            # print(f"Total de registros: {records2[0][0]}")
                
            
    except Error as e:
        print(f"Error al conectar o consultar en MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")
            

connect_and_query()

