from ICommand.ICommand import ICommand
import Core
from controle.Fachada import Fachada
import Dominio
from EntidadeDominio import EntidadeDominio
from Fornecedor import Fornecedor
class AbstractCommand(ICommand):
    """description of class"""
    fa= Fachada()

