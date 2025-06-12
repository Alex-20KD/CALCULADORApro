import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        dbname="Calculadorapro",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

def guardar_operacion_log(operacion, resultado):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            sql.SQL("INSERT INTO calculos (operacion, resultado) VALUES (%s, %s)"),
            (operacion, resultado)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
