import json
from flask import request, jsonify, Response
from database import Database
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity
from config import Config
from datetime import timedelta

bcrypt = Bcrypt()

class Auth:
    def __init__(self):
        self.db = Database()

    def login(self, username, password):
        connection = self.db.get_connection()
        cursor = connection.cursor(buffered=True)
        cursor.execute("select user_id, password from precise.users where user_id = %s", (username,))
        status = "error"
        access_token = ""
        if cursor.rowcount > 0:
            data_user = cursor.fetchone()
            if bcrypt.check_password_hash(data_user[1],password) is True:
                access_token = create_access_token(identity=username,  expires_delta=timedelta(seconds=float(Config.JWT_ACCESS_TOKEN_EXPIRED)))
                message = "You are logged in"
                status = "ok"
            else:
                message = "Password not matched"
        else:
            message = "Not match for any user"
        msg = {'status':status, 'message':message, "access_token":access_token}
        cursor.close()
        return jsonify(msg), 200
    
    def me(self):
        data = get_jwt()
        connection = self.db.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select * from dbhrd.newdatakar where NIP=%s", [data["sub"]])
        myData = cursor.fetchone()
        cursor.close()
        return jsonify(myData), 200

