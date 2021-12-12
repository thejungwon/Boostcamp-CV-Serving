
import toml
import mysql.connector



def _execute(qry, val, is_select=False):
    secrets = toml.load(".streamlit/secrets.toml")
    conn =  mysql.connector.connect(
        host=secrets['mysql']['host'],
        user=secrets['mysql']['user'],
        passwd=secrets['mysql']['password'],
        database=secrets['mysql']['database']
        )
    print(qry, val)
    with conn.cursor(dictionary=True) as cur:
        cur.execute(qry, val)
        
        if is_select:
            result = cur.fetchall()
        else:
            conn.commit()
            result = cur.lastrowid
        print(result)

    conn.close()
    
    return result




def insert_data(username, image_url, label):
    qry = "INSERT INTO pictures (username, image_url, label) VALUES (%s, %s, %s)"
    val = (username, image_url, label)
    _ = _execute(qry, val, is_select=False)
    
    
    

def get_data(username):
    qry = "SELECT * FROM pictures WHERE username = %s ORDER BY id DESC"
    val = (username, )
    return _execute(qry, val, is_select=True)