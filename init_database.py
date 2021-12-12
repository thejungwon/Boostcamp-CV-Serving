import toml
import mysql.connector

secrets = toml.load(".streamlit/secrets.toml")

conn =  mysql.connector.connect(
    host=secrets['mysql']['host'],
    user=secrets['mysql']['user'],
    passwd=secrets['mysql']['password'],
)

with conn.cursor() as cur:
    try:
        cur.execute("DROP DATABASE streamlit")    
    except:
        pass
    cur.execute("CREATE DATABASE streamlit")

conn.close()

conn =  mysql.connector.connect(
    host=secrets['mysql']['host'],
    user=secrets['mysql']['user'],
    passwd=secrets['mysql']['password'],
    database=secrets['mysql']['database'],
)



with conn.cursor() as cur:
    try:
        sql = "DROP TABLE pictures"
        cur.execute(sql)
    except:
        pass
    cur.execute("""
    CREATE TABLE pictures 
    (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        username VARCHAR(50),
        image_url VARCHAR(255),
        label VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """)

conn.close()
    