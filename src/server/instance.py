from flask import Flask
from flask_restplus import Api


class Server ():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api (self.api,
                        version='1.0',
                        title='Carros',
                        description='Carros list',
                        doc= '/docs')
    def run (self,):
        self.app.run(
            port=9990, 
            host='localhost',
            debug=True
        ) 

server = Server()