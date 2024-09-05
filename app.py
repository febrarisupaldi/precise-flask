from flask import Flask, request
from resources.master.user import User
from resources.auth import Auth
from flask_jwt_extended import JWTManager, jwt_required
from config import Config
app = Flask(__name__)

user = User()
auth = Auth()
JWTManager(app)
app.config.from_object(Config)

@app.route("/login", methods=['POST'])
def login():
    data = request.form
    username = data['user_id']
    password = data['password']
    return auth.login(username, password)

@app.route("/", methods=['GET'])
@jwt_required()
def index():
    return user.get_users()

@app.route("/me", methods=['POST'])
@jwt_required()
def me():
    return auth.me()


if __name__ == '__main__':
    app.run(debug=True)