from flask import Flask
from routes.auth import auth
from routes.todo import todo
app=Flask(__name__)
app.register_blueprint(todo)
app.register_blueprint(auth)
if __name__=="__main__":
    app.run(debug=True)