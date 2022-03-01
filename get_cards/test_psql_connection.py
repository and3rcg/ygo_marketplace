import psycopg2

db_connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres',
    port=5432)

print('Connected successfully!')

db_cursor = db_connection.cursor()

print('Cursor created successfully!')

db_cursor.close()
db_connection.close()

print('Connection closed successfully!')
