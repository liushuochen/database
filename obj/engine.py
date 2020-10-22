import mysql.connector


class Engine(object):
    def __init__(
            self,
            username,
            password,
            name="DEFAULT",
            database=None,
            host="localhost"
    ):
        self.username = username
        self.password = password
        self.name = name
        self.database = database
        self.host = host

    def connection(self):
        kwargs = {
            "host": self.host,
            "user": self.username,
            "password": self.password,
            "auth_plugin": "mysql_native_password",
        }
        if self.database:
            kwargs["database"] = self.database

        return mysql.connector.connect(**kwargs)
