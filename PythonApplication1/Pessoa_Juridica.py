from Pessoa import Pessoa
class Pessoa_Juridica(Pessoa):
    """description of class"""
    __CNPJ=""
    def setCNPJ(self,str):
        self.__CPNJ=str
    def getCNPJ(self):
        return self.__CPNJ