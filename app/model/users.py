"""users file"""
import datetime
from flask import jsonify
from flask_jwt_extended import create_access_token
from app.database import Database


class User(Database):
    """class for implementing user functions"""

    def __init__(self):
        """user class constructor"""
        Database.__init__(self)

    def sign_up(self, username, password, address,
                email, admin):
        """method for creating a user"""
        try:
            """method for checking whether user is avialable"""
            response = ""
            cur = self.con.cursor()
            cur.execute("""SELECT username FROM Users where
                        username =%s """, (username, ))
            self.con.commit()
            result = cur.rowcount
            if result > 0:
                response = jsonify({"message": "Username is already existing"}), 409
            else:
                cur.execute("""INSERT INTO users(username, password, address,
                            email, admin)VALUES (%s, %s, %s, %s, False)""",
                            (username, password, address,
                            email))
                self.con.commit()
                response = jsonify({"message": "User registeration successfuly"}), 201
            return response
        except Exception as err:
            return jsonify({"Message": "The {} is problem".format(str(err))}), 400


    def login(self, username, password):
        """method for loging in a user"""
        try:
            response = ""
            cur = self.con.cursor()
            cur.execute("""SELECT * FROM  Users where username = %s AND
                        password = %s""", (username, password))
            self.con.commit()
            count = cur.rowcount
            data = cur.fetchone()
            if count > 0:
                '''Lets user create access token 
                for a user login to acces resources
                '''

                expires = datetime.timedelta(days=1)
                user = dict(user_id=data[0], username=data[1],
                                    password=data[2], address=data[3],
                                    email=data[4],admin=data[5])
                access_token = create_access_token(identity=user,
                                                   expires_delta=expires)
                response = jsonify({"Message": "Login successful",
                                    "Token": access_token})
                response.status_code = 200
            else:
                response = jsonify({"Message": "Username or password is not valid"}), 404
            return response
        except:
            return jsonify({"message": "User login failed"})
