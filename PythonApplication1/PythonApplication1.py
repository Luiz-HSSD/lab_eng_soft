from Fornecedor import Fornecedor
from FornecedorDAO import FornecedorDAO
from Fachada import Fachada
f=Fornecedor()
f.setNome("Luizinho")
f.setCNPJ("98765432103210")
fd=FornecedorDAO()
while(True):
    print("selecione a opção")
    print("1 - cadastrar")
    print("2 - ler")
    print("3 - alterar")
    print("4 - excluir") 
    a =input()
    if a=="1":
        f.setNome(input("digite o nome: "))
        f.setCNPJ(input("digite o cnpj: "))
        fd.Cadastrar(f);
    elif a=="2":
        f.setID(int(input("chave: ")));
        fd.Consultar(f);
    elif a=="3":
        f.setID(int(input("chave: ")));
        f.setNome(input("digite o nome: "))
        f.setCNPJ(input("digite o cnpj: "))
        fd.Alterar(f);
    elif a=="4":
        f.setID(int(input("chave: ")));
        fd.excluir(f);