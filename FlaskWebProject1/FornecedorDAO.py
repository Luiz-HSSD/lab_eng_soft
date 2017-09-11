import psycopg2
from Conexao import Conexao 
from IDAO import IDAO
from Fornecedor import Fornecedor
from EntidadeDominio import EntidadeDominio
class FornecedorDAO(IDAO):
    """description of class"""
    def _init_():
        pass
    def Cadastrar(self,EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        sql = "insert into fornecedor values (default,"+"'"+f.getNome()+"','"+f.getCPNJ()+"')"
        if con.manipular(sql):
            print('inserido com sucesso!')
        rs=con.consultar("select * from fornecedor")
        for linha in rs:
            print(linha)
        con.fechar()
        return
    def Alterar(self, EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        sql = "UPDATE fornecedor SET fornecedor_nome = '"+f.getNome()+"', cnpj ='"+ f.getCNPJ() +"' WHERE forne_id = "+str(f.getID())
        if con.manipular(sql):
            print('alterado com sucesso!')
        rs=con.consultar("select * from fornecedor")
        for linha in rs:
            print(linha)
        con.fechar()
        return
    def excluir(self,EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        sql = "delete from fornecedor where FORNE_ID="+str(f.getID())
        if con.manipular(sql):
            print('excluido com sucesso!')
        rs=con.consultar("select * from fornecedor")
        for linha in rs:
            print(linha)
        con.fechar()
        return
    def Consultar(self, EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        #sql = "select * from fornecedor where FORNE_ID="+str(f.getID())    rs= con.consultar(sql)
        #for linha in rs:
         #   print(linha)  print("\n lista inteira \n")
        rs=con.consultar("select * from fornecedor")
        #for linha in rs:
          #  print(linha)
        con.fechar()
        return rs
