from flask import Blueprint,request,jsonify
import bcrypt 
import mysql.connector
import Config
import jwt
import datetime

auth=Blueprint('auth',__name__)
@auth.route('/register',methods=['POST'])
def get_user():
    conn=mysql.connector.connect(
    host=Config.HOST,
    user=Config.USER,
    password=Config.PASSWORD,
    database=Config.DATABASE
    )
    data=request.get_json() 
    user_name=data['name']
    password=data['password']
    hashed=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    cursor=conn.cursor()
    cursor.execute("INSERT INTO groceries_users (user_name,password) values(%s,%s)",
    (user_name,hashed))
    cursor.close()
    conn.commit()
    conn.close()
    return jsonify({"Message":"User has added"}),201
@auth.route('/login',methods=['POST'])
def login_user():
    conn=mysql.connector.connect(
    host=Config.HOST,
    user=Config.USER,
    password=Config.PASSWORD,
    database=Config.DATABASE
    )
    data=request.get_json()
    user_name=data["name"]
    password=data['password']
    cursor=conn.cursor()
    cursor.execute("select * from groceries_users Where user_name=%s",(user_name,))
    user=cursor.fetchone()
    if not user:
        return jsonify({"Message":"user not found"}),404
    check=bcrypt.checkpw(password.encode('utf-8'),user[2].encode('utf-8'))   
    if check==False:
        return jsonify({"Message":"Incorrect password try again"}), 401
    token = jwt.encode(
    {"user_id": user[0], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
    Config.SECRET_KEY,
    algorithm="HS256")
    return jsonify({"token":token}),200

    
    
    