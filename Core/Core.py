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
while True :
    print('selecione uma opção')
    print("1 cadastrar")
    print("2 alterar")
    print("3 excluir")
    print("4 consultar")
    n =input("")
    if n == "1":
        f.setNome(input("digite o nome"))
        f.setCNPJ(input("digite o cnpj"))
        fd.Cadastrar(f)
        print("inserido com sucesso!")
    elif n == "2":
        f.setID(int("digite o código"))
        f.setNome(input("digite o nome"))
        f.setCNPJ(input("digite o cnpj"))
        fd.Alterar(f)
        print("alterado com sucesso!")
    elif n == "3":
        f.setID(int("digite o código"))
        fd.Excluir(f)
        print("excluido com sucesso!")
    elif n == "4":
        print("")
        le=fd.Consultar(f)
        for a in le:
            print(str(a.getID())+ " "+a.getNome()+ " "+a.getCNPJ())
        print("")

