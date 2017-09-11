from Dominio.Fornecedor import Fornecedor
from DAO.FornecedorDAO import FornecedorDAO
from controle.Fachada import Fachada
f= Fornecedor()
f.setID(0)
f.setNome("Luiz")
f.setCNPJ("09876543213210")
fd= Fachada()
bloc=fd.Excluir(f)
print( bloc)
#f=bloc[2]print("Nome : "+f.getNome()+ " CNPJ: "+f.getCNPJ())