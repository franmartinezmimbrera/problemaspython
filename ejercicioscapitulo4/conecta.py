import sqlite3

def conectar_bd():
    # Crea una conexión a una base de datos local (o en memoria)
    conexion = sqlite3.connect("ejemplo.db")
    cursor = conexion.cursor()
    
    # Crear tabla
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER, nombre TEXT)")
    
    # Insertar datos
    cursor.execute("INSERT INTO usuarios VALUES (1, 'Ana')")
    conexion.commit()
    
    # Leer datos
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())
    
    # Cerrar conexión
    conexion.close()

if __name__ == "__main__":
    conectar_bd()