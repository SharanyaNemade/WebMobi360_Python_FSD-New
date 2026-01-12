# import os
# import mysql.connector

# def init_database():
#     conn = mysql.connector.connect(
#         host=os.getenv("DB_HOST"),
#         port=int(os.getenv("DB_PORT", 3306)),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME")
#     )

#     cursor = conn.cursor()

#     with open("db_init.sql", "r") as f:
#         sql_script = f.read()

#     for statement in sql_script.split(";"):
#         if statement.strip():
#             cursor.execute(statement)

#     conn.commit()
#     cursor.close()
#     conn.close()

#     print("✅ Database & tables ready")














import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()



def init_database():
    # connect WITHOUT database first
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_disabled=False
    )


        # host=os.getenv("DB_HOST"),
        # user=os.getenv("DB_USER"),
        # password=os.getenv("DB_PASSWORD")
    
    cursor = conn.cursor()

    with open("db_init.sql", "r") as f:
        sql_script = f.read()

    for statement in sql_script.split(";"):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Database & tables ready")
