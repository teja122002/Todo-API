import mysql.connector
import Config
conn=mysql.connector.connect(
    host=Config.HOST,
    user=Config.USER,
    password=Config.PASSWORD,
    database=Config.DATABASE
)
cursor=conn.cursor()
cursor.execute("""Create table  if not exists groceries_users(
               id int auto_increment primary key,
                        user_name varchar(50) unique,
                        password varchar(60))""")

cursor.execute("""CREATE TABLE if not exists Todo(
               id int auto_increment primary key,
               user_id int,
                title varchar(50),
                is_done BOOLEAN DEFAULT FALSE,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               FOREIGN KEY(user_id) REFERENCES groceries_users(id))""")
conn.commit()
cursor.close()
conn.close()