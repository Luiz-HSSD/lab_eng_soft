from EntidadeDominio import EntidadeDominio
from DAO.FornecedorDAO import FornecedorDAO
from Fornecedor import Fornecedor
from Core.IDAO import IDAO
from Core.IFachada import IFachada
from Core.IStrategy import IStrategy
from Negocio.Parametro_Excluir import Parametro_Excluir
from Negocio.teste import teste
class Fachada(IFachada):
    """description of class"""
    c='cadastrar'
    r='consultar'
    u='alterar'
    d='excluir'
    pa_ex = Parametro_Excluir()
    tes=teste()
    f= FornecedorDAO()
    rnscadastrafornecedor=[]
    rnsconsultarfornecedor=[]
    rnsalterarfornecedor=[]
    rnsexcluirfornecedor=[pa_ex,tes]
    rnsfornecedor={c:rnscadastrafornecedor , r:rnsconsultarfornecedor, u:rnsalterarfornecedor,d:rnsexcluirfornecedor}
    rns={'Fornecedor' : rnsfornecedor}
    IDAOS={'Fornecedor' : f}
    per =IDAO()
    def _init_(self):
        return

    def executar_regras(self,EntidadeDominio,str): 
        nmClasse= EntidadeDominio.__class__.__name__
        msg=[]
        dict=self.rns.get(nmClasse)
        if dict is not None:
            regras=dict.get(str)
            if regras is not None:
                for val in regras:
                    erro=val.Processar(EntidadeDominio)
                    if erro is not None:
                        msg.append(erro+'\n')
                    continue
        if  len(msg) > 0 :
            erro=''.join(msg)
            return erro
        else: 
            return None
       
    def Cadastrar(self,EntidadeDominio):
        msg=self.executar_regras(EntidadeDominio,self.c)
        if msg is None:
            per=  self.IDAOS[EntidadeDominio.__class__.__name__]
            return per.Cadastrar(EntidadeDominio)
    def Consultar(self,EntidadeDominio):
        msg=self.executar_regras(EntidadeDominio,self.r)
        if msg is None:
            per=  self.IDAOS[EntidadeDominio.__class__.__name__]
            return per.Consultar(EntidadeDominio)
    def Alterar(self,EntidadeDominio):
        msg=self.executar_regras(EntidadeDominio,self.u)
        if msg is None:
            per=  self.IDAOS[EntidadeDominio.__class__.__name__]
            return per.Alterar(EntidadeDominio)
    def Excluir(self,EntidadeDominio):
        msg=self.executar_regras(EntidadeDominio,self.d)
        if msg is None:
            per=  self.IDAOS[EntidadeDominio.__class__.__name__]
            return per.Excluir(EntidadeDominio)
        return msg
#    def Visualizar():	    executar_regras(EntidadeDominio,r)
