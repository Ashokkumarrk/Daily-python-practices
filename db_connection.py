import mysql.connector as db
conn=db.connect(
    host="localhost",
    user="root",
    password="ashok45",
    database="MYSQL"
)
cursor=conn.cursor()
cursor.execute("select * from employees;")
rows=cursor.fetchall()
for r in rows:
    print(r)
    
conn.close()