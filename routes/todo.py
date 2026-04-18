from flask import Blueprint,request,jsonify
import Config
import jwt
import mysql.connector
conn=mysql.connector.connect(
    host=Config.HOST,
    user=Config.USER,
    password=Config.PASSWORD,
    database=Config.DATABASE
    )
todo=Blueprint('todo',__name__)
def verify_token():
    token=request.headers.get('Authorization')
    if not token:
        return None
    try:
        decoded=jwt.decode(token,Config.SECRET_KEY,algorithms=["HS256"])
        return decoded['user_id']
    except:
        return None
#Verify token
@todo.route('/todo',methods=['GET'])
def get_todo():
    user_id=verify_token()
    if not user_id:
        return jsonify({"Message":"Token not found"}),401
    cursor=conn.cursor()
    cursor.execute("select * from todo where user_id=%s",(user_id,))
    todos = cursor.fetchall()
    cursor.close()
    return jsonify({"todo":todos})
#Add todo
@todo.route('/add',methods=['POST'])
def add_todo():
    user_id=verify_token()
    data=request.get_json()
    title=data.get('title')
    if not user_id:
        return jsonify({'Message':'Token not found'}) 
    cursor=conn.cursor()
    cursor.execute("INSERT INTO todo (user_id,title) values(%s,%s)",(user_id,title))
    conn.commit()
    cursor.close()
    return jsonify({"Message":"Title has added"})
#update todo
@todo.route('/put/todo/<id>',methods=['PUT'])
def update(id):
    user_id=verify_token()
    if not user_id:
        return jsonify({"Message":"User not found"})
    data=request.get_json()
    cursor=conn.cursor()
    cursor.execute("UPDATE todo set title=%s where id=%s and user_id=%s",(data['title'],id,user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"Message":"title has updated"})
@todo.route('/delete/todo/<id>',methods=['DELETE'])
def delete(id):
    user_id=verify_token()
    if not user_id:
        return jsonify({'Message':"User not found"})
    cursor=conn.cursor()
    cursor.execute("DELETE from todo where id=%s and user_id=%s",(id,user_id))
    cursor.close()
    conn.commit()
    conn.close()
    return jsonify({"Message":"Deleted"})
    



        



