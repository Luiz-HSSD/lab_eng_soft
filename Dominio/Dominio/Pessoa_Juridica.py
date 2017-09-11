from Dominio.Pessoa import Pessoa
class Pessoa_Juridica(Pessoa):
    """description of class"""
    __CNPJ="12345678901234"
    def setCNPJ(self,str):
        self.__CNPJ=str
    def getCNPJ(self):
        return self.__CNPJ