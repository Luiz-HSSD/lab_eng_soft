"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
#from flask 
from Fornecedor import Fornecedor
from FornecedorDAO import FornecedorDAO
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
f= Fornecedor()
fd  =FornecedorDAO()
@app.route('/',methods=['GET','POST'])
def index():
    """Renders a sample page."""
    f.setID(1);
    rs=fd.Consultar(f)
    ss=""
    for s in rs:
        ss+="\n".join(str(s))
    return ss

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
