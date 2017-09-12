from Core.IStrategy import IStrategy
from EntidadeDominio import EntidadeDominio
class teste(IStrategy):
    """description of class"""
    def Processar(self,EntidadeDominio):
        if EntidadeDominio.getNome() == 'Luiz':
            return "Luizinho é foda"


