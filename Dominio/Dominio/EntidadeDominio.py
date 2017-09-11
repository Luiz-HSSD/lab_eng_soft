from datetime import datetime
from Dominio.Entidade import Entidade
class EntidadeDominio(Entidade):
    """description of class"""
    __ID=0
    __DataCadastro=datetime.now()
    def setID(self,int):
        self.__ID=int
    def getID(self):
        return self.__ID
    def setDataCadastro(self,datetime):
        self.__DataCadastro=datetime
    def getDataCadastro(self):
        return self.__DataCadastro