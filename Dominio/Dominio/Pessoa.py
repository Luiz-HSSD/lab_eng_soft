from EntidadeDominio import EntidadeDominio
class Pessoa(EntidadeDominio):
    """description of class"""
    __Nome="empty"
    def setNome(self,str):
        self.__Nome=str
    def getNome(self):
        return self.__Nome

