import psycopg2
from Utils.Conexao import Conexao 
from Core.IDAO import IDAO
from Dominio.Fornecedor import Fornecedor
from Dominio.EntidadeDominio import EntidadeDominio
class FornecedorDAO(IDAO):
    """description of class"""
    def _init_():
        pass
    def Cadastrar(self,EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        sql = "insert into fornecedor values (default, '"+f.getNome()+"' , '"+f.getCNPJ()+"' )"
        if con.manipular(sql):
            con.fechar()
            return
        else:
            con.fechar()
            raise ConnectionAbortedError
    def Alterar(self, EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        sql = "UPDATE fornecedor SET fornecedor_nome = '"+f.getNome()+"', cnpj ='"+ f.getCNPJ() +"' WHERE forne_id = "+str(f.getID())
        if con.manipular(sql):
            con.fechar()
            return
        else:
            con.fechar()
            raise ConnectionAbortedError
    def Excluir(self,EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        sql = "delete from fornecedor where FORNE_ID="+str(f.getID())
        if con.manipular(sql):
            con.fechar()
            return
        else:
            con.fechar()
            raise ConnectionAbortedError
    def Consultar(self, EntidadeDominio):
        f=EntidadeDominio
        f.__class__ = Fornecedor
        con=Conexao('localhost','lab','postgres','123')
        rs=con.consultar("select * from fornecedor")
        helicopter=[]
        for linha in rs:
            fa = Fornecedor()
            fa.setID(int(linha[0]))
            fa.setNome(str(linha[1]))
            fa.setCNPJ((linha[2]))
            helicopter.append(fa)
        con.fechar()
        return helicopter
