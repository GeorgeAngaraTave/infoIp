import pymysql
import socket

# db = sqlalchemy.create_engine(
#     sqlalchemy.engine.url.URL(
#         drivername='mysql+pymysql',
#         username=DB_USER,
#         password=DB_PASSWORD,
#         database=DB_NAME,
#         query={
#             'unix_socket': '/cloudsql/{}'.format(INSTANCE_CONNECTION_NAME)
#         }
#     ),
#     # ... Specify additional properties here.
#     # ...
# )

def connection():
    DB_NAME = 'api_amazongear'
    DB_USER = 'saving_155216'
    DB_PASSWORD = 'GbUG*u2ccK-n'
    INSTANCE_CONNECTION_NAME = 'saving-the-amazon-155216:us-central1:mysql-saving-the-amazon'

    try:
        db = pymysql.connect(
        unix_socket='/cloudsql/' + INSTANCE_CONNECTION_NAME,
        host='130.211.113.54',
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        autocommit=True
    )
    except:
        exit("Error: Unable to connect to the database")

    return db

# prepare a cursor object using cursor() method
# cursor = db.cursor()

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)

# disconnect from server
# db.close()