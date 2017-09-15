from flask import Flask, redirect, render_template, url_for, request
from EntidadeDominio import EntidadeDominio
from Fornecedor import Fornecedor
from Command.AlterarCommand import AlterarCommand
from Command.ConsultarCommand import ConsultarCommand
from Command.ExcluirCommand import ExcluirCommand
from Command.SalvarCommand import SalvarCommand
from os import environ
from FlaskWebProject2 import app
class Controllers(object):
    """description of class"""
    def __init__(self):
        pass

    @staticmethod
    def save(**kwargs):
        forne = Fornecedor()
        forne.setNome(kwargs['nome'])
        forne.setCNPJ(kwargs['cnpj'])

        save_command = SaveCommand()
        result = save_command.execute(client)

        return render_template('insert.html', message=result.result)

    @staticmethod
    def update(**kwargs):
        forne = Fornecedor()
        forne.setID(int(kwargs['id']))
        forne.setNome(kwargs['nome'])
        forne.setCNPJ(kwargs['cnpj'])
        delete_command = ExcluirCommand()
        result = delete_command.execute(forne)
        return render_template('index.html', message=result.result)

    @staticmethod
    def delete(client_id):
        forne = Fornecedor()
        forne.setID(int(client_id))
        delete_command = ExcluirCommand()
        result = delete_command.execute(forne)
        return render_template('index.html', message=result.result)


    @staticmethod
    def search(client_id=None):
        forne = Fornecedor()
 #       forne.setID(0)
        search_command = ConsultarCommand()
        result = search_command.execute(forne)
        if not client_id:
            return render_template('index.html', clients=result)
        return result.result


