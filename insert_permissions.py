import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import urlparse, quote_plus
import requests
import pyodbc
import os


# set credentials, server and database name

username = 'your_username'
password = 'your_password'
server   = 'hostname_or_ip'
port     = '5432'
database = 'target_database_for_pg_permissions'


# create connection string using the credentials

conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(username,password,server, port, database)
db = create_engine(conn_string)
conn = db.connect() 


# provide query to get list of databeses 

query = 'SELECT datname FROM pg_database WHERE datistemplate = false;'

db_list = pd.read_sql(query, conn)



# create new list containing database names  

dblist = db_list['datname'].to_list()




# loop through each database in the list, connect and get permission details on database objects  

for db in dblist:
    
    loop_string = 'postgresql://{}:{}@{}/{}'.format(username,password,server,db)
    loop_db = create_engine(loop_string)
    loop_conn = loop_db.connect() 
    
    
    loop_query = """
    SELECT  current_database() as db_name,
            grantee as user_name, 
            privilege_type as permission, 
            table_schema as schema_name, 
            table_name 
    FROM information_schema.role_table_grants
    where table_schema not in ('pg_catalog','information_schema');
    """
    
    
    
    dbloop_list = pd.read_sql(loop_query, loop_conn)
    
    # insert into "pg_permissions" table
    
    dbloop_list.to_sql(name="pg_permissions", con=conn, if_exists="append", index=False)
    
    # close connections
    
    loop_conn.close()
    
conn.close()