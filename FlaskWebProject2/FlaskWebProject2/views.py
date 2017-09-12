"""
Routes and views for the flask application.
"""
from flask import Flask
from datetime import datetime
from flask import Flask, redirect, render_template, url_for, request
from FlaskWebProject2 import app
from FlaskWebProject2.Controllers import Controllers
@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return Controllers.search()

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/read/<client_id>')
def read(client_id):
    client = Controllers.search(client_id)
    return render_template('read.html', client=client)

@app.route('/search')
def search():
    return Controllers.search()

@app.route('/save', methods=['GET', 'POST'])
def client_save():
    kwargs = {
        'nome': request.form['nome'],
        'cnpj': request.form['cnpj']
    }
    return Controllers.save(**kwargs)

@app.route('/update', methods=['GET', 'POST'])
def update():
    print(request.form)
    kwargs = {
        'id': request.form.get('id'),
        'nome': request.form.get('nome'),
        'cnpj': request.form.get('cnpj')
    }
    return Controllers.update(**kwargs)

@app.route('/delete/<client_id>')
def delete_client(client_id):
    return Controllers.delete(client_id)
