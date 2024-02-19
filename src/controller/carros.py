from flask import Flash

from flask_restplus import Api,Resource

from src.server.instance import server
app,api = server.app, server.api

carros = [
    {
        'id' : 1,
        'nome': "Siena",
        'modelo': 'Sedam',
        'marca': 'Fiat',
        'ano': 2018
    },
    {
        'id' : 2,
        'nome': 'Corolla',
        'modelo': 'Sedam',
        'marca': 'Toyota',
        'ano': 2023
    },
    {
        'id' : 3,
        'nome': 'hondafit',
        'modelo': 'hat',
        'marca': 'honda',
        'ano': 2012
    },
    {
        'id' : 4,
        'nome': 'Cronos',
        'modelo': 'Sedam',
        'marca': 'Fit',
        'ano': 2024
    },
    {
        'id' : 5,
        'nome': 'Touro',
        'modelo': 'Picape',
        'marca': 'Fit'
    },

] 




class carrlist (Resource):
    def get(self,):

        return carros