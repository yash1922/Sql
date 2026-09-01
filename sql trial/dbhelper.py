import mysql.connector


class DBHelper:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="trial"
        )
        self.cursor = self.connection.cursor()

    def add_user(self, name, email, password):
        try:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, email, password))
            self.connection.commit()
            return True
        except mysql.connector.Error:
            return False

    def check_user(self, email, password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        self.cursor.execute(query, (email, password))
        user = self.cursor.fetchone()

        if user:
            return True
        return False
