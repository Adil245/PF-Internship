import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres',password='1412', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS image_embaddings")

#Creating table as per requirement
# sql ='''CREATE TABLE image_embaddings(
#    id SERIAL PRIMARY KEY ,
#    NAME CHAR(40) NOT NULL,
#    Embadings VARCHAR,
#    Path VARCHAR
# )'''

# cursor.execute(sql)
# print("Table created successfully........")
# conn.commit()
#Closing the connection
# conn.close()