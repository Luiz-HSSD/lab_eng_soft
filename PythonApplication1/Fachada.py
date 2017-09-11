from EntidadeDominio import EntidadeDominio
from FornecedorDAO import FornecedorDAO
from Fornecedor import Fornecedor
from IDAO import IDAO
from IFachada import IFachada
class Fachada(IFachada):
    """description of class"""
    c='cadastrar'
    r='consultar'
    u='alterar'
    d='excuir'
    def _init_(self):
        self.rnscadastrafornecedor=[]
        self.rnsconsultarfornecedor=[]
        self.rnsalterarfornecedor=[]
        self.rnsexcluirfornecedor=[]
        self.rnsfornecedor={c:rnscadastrafornecedor , r:rnscosultarfornecedor, u:rnsalterarfornecedor,d:rnsexcluirfornecedor}
        self.rns={'Fornecedor' : rnsfornecedor}
        self.IDAOS={Fornecedor.__class__.__name__ : rnsfornecedor}
        return
    def executar_regras(self,EntidadeDominio,str): 
        nmClasse= EntidadeDominio.__class__.__name__
        msg=[]
        dict=self.rns().get(nmClasse)
        if dict is not None:
            regras=dict.get(str)
            if regras is not None:
                for val in regras:
                    erro=val.processar(EntidadeDominio)
                    if erro is not None:
                        msg.append(erro+'\n')
                    continue
        if  msg.count() > 0 :
            erro=''.join(msg)
            return str(erro)
        else: 
            return None

    def Cadastrar(self,EntidadeDominio):
        msg=self.executar_regras(EntidadeDominio,self.c)
        if msg is not None:
            IDAO(exe=IDAOS[EntidadeDominio.__class__.__name__]).Cadastrar(EntidadeDominio)

    def Consultar(EntidadeDominio):
	    executar_regras(EntidadeDominio,r)

    def Alterar(EntidadeDominio):
	    executar_regras(EntidadeDominio,u)
    def excluir(EntidadeDominio):
	    executar_regras(EntidadeDominio,d)
    def Visualizar():
	    executar_regras(EntidadeDominio,r)
