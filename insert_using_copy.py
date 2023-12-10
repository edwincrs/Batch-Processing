import psycopg2
from sqlalchemy import column

host = "pg-dev-dev-101.a.aivencloud.com"
port = "16506"
dbname = "defaultdb"
user = "avnadmin"
password = "AVNS_WKCKGD4JC5s0lel9zKD"

conn =  psycopg2.connect(("host={host} dbname={dbname} user={user} password={password} port={port}").format(host=host,dbname=dbname,user=user,password=password,port=port))

cur=conn.cursor()

# create table
cur.execute("""
            CREATE TABLE IF NOT EXISTS edwin_users_using_copy(
                id serial primary key
                ,email text
                ,name text
                ,phone text
                ,postal_code text
                )
            """)

with open ("C:/Users/Edwin Cris/Desktop/Course/Digital Skola/Docker/users_w_postal_code.csv","r") as f:
    next(f)
    cur.copy_from(f, "edwin_users_using_copy", sep=",", columns=("email","name","phone","postal_code"))
    
conn.commit()