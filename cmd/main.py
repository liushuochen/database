from flask import Flask
from cmd import init

app = Flask("database service")


if __name__ == '__main__':
    host, port = init()
    app.run(host=host, port=port)
