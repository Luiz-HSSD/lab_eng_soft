from Core.IStrategy import IStrategy
from Dominio.EntidadeDominio import EntidadeDominio
class Parametro_Excluir(IStrategy):
    """description of class"""
    def Processar(self,EntidadeDominio):
        if EntidadeDominio.getID() == 0:
            return "parametro de exclusão não pode ser 0"


