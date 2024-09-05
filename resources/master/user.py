import json
from flask import Response, request, jsonify
from database import Database

class User:
    def __init__(self):
        self.db = Database()

    def get_users(self):
        connection = self.db.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select user_id from precise.users")
        users = cursor.fetchall()
        cursor.close()
        return Response(json.dumps(users), mimetype="application/json")