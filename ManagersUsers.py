# usuarios = {}
#
# opcao = input("O que deseja realizar? "
#               +  "<I> - Para Inserir um usário "
#               +  "<P> - Para Pesquisar um usuário "
#               +  "<E> - Para Excluir um usuário "
#               +  "<L> _ Para Listar um usuário: ").upper()
#
# while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
#     if opcao == "I":
#         # chave = input("Digite o login: ").upper()
#         # nome = input("Digite o nome: ").upper()
#         # data = input("Digite a última data de acesso: ")
#         # estacao = input("Qual a última estação acessada: ").upper()
#         # usuarios[chave] = [nome,data,estacao]
#
#         # chave = input("Digite o login: ").upper()
#         # usuarios[chave] = [input("Digite o nome:").upper(),
#         #                    input("Digite a útilma data de acesso: "),
#         #                    input("Qual a últma estação acessada: ").upper()]
#
#         usuarios[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
#                                                        input("Digite a útima data de acesso: "),
#                                                        input("Qual a última estação acessada:  ").upper()]
#
#
#     opcao = input("O que desja realizar? "+
#                   "<I> - Para Inserir um usuário " +
#                   "<P> - Para Pesquisar um usuário " +
#                   "<E> -Para Excluir um usuário " +
#                   "<L> - Para listar um usuário: ").upper()

from Funcoes.FuncoesDicionario import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao =="L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Qual o login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios, input("Qual o login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()


