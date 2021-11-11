import MySQLdb

DB_HOST = '34.151.234.8'
DB_USER = 'root'
DB_PASS = 'Soporte,f20'
DB_NAME = 'universidad'

criterio = "A001"
query = "SELECT a.CODALU, a.APEALU, a.NOMALU, c.CODCUR,c.NOMCUR, cru.nota, c.CREDITO FROM ALU_CUR as cru, CURSOS as c, ALUMNOS as a where cru.CODALU = a.CODALU and cru.CODCUR = c.CODCUR and cru.CODALU = '%s'" % criterio
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
conn = MySQLdb.connect(*datos)
cursor = conn.cursor()
cursor.execute(query)

if query.upper().startswith('SELECT'):
    data = cursor.fetchall()   # Traer los resultados de un select
else:
    conn.commit()              # Hacer efectiva la escritura de datos
    data = None
cursor.close()                 # Cerrar el cursor
conn.close()                   # Cerrar la conexión

print(data[0][0])
for cursos in data:
    print(cursos)