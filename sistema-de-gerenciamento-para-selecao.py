import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE candidatos (id_candidato integer,nome text,idade integer, email text, vaga text)")

    
def inserir():

    id_candidato = input("Informe seu ID: ")
    nome = input("Informe seu nome: ")
    idade = input("Informe a sua idade: ")
    email = input("Informe seu email: ")
    vaga = input("Informe a vaga de interesse: ")

    banco = sqlite3.connect('banco.db')

    cursor = banco.cursor()
    
    cursor.execute("INSERT INTO candidatos VALUES('"+id_candidato+"','"+nome+"','"+str(idade)+"','"+email+"','"+vaga+"')")

    banco.commit()

    print("\nCandidato cadastrado no sistema!\n")


def mostrar():
    print("\n| CANDIDATOS |\n")
    cursor.execute("SELECT * FROM candidatos")
    print(cursor.fetchall())


def atualizar(op):
    if op == 1:
        id_candidato = input("Informe o ID do candidato: ")
        nnome = input("Informe o nome a ser alterado: ")

        banco = sqlite3.connect('banco.db')

        cursor = banco.cursor()

        cursor.execute("UPDATE candidatos SET nome = '"+nnome+"' WHERE id_candidato = '"+id_candidato+"' ")

        banco.commit()

        print("\nNome alterado!\n")

    if op == 2:
        id_candidato = input("Informe o ID do candidato: ")
        nidade = input("Informe a idade a ser alterada: ")

        banco = sqlite3.connect('banco.db')

        cursor = banco.cursor()

        cursor.execute("UPDATE candidatos SET idade = '"+nidade+"' WHERE id_candidato = '"+id_candidato+"' ")

        banco.commit()

        print("\nIdade alterada!\n")

    if op == 3:
        id_candidato = input("Informe o ID do candidato: ")
        nemail = input("Informe o email a ser alterado: ")

        banco = sqlite3.connect('banco.db')

        cursor = banco.cursor()

        cursor.execute("UPDATE candidatos SET email = '"+nemail+"' WHERE id_candidato = '"+id_candidato+"' ")

        banco.commit()

        print("\nEmail alterado!\n")

    if op == 4:
        id_candidato = input("Informe o ID do candidato: ")
        nvaga = input("Informe a vaga a ser alterada: ")

        banco = sqlite3.connect('banco.db')

        cursor = banco.cursor()

        cursor.execute("UPDATE candidatos SET vaga = '"+nvaga+"' WHERE id_candidato = '"+id_candidato+"' ")

        banco.commit()

        print("\nVaga alterada!\n")

def delete():
    
    id_candidato = input("Informe o ID do candidato: ")

    try: 

        banco = sqlite3.connect('banco.db')

        cursor = banco.cursor()

        cursor.execute("DELETE FROM candidatos WHERE id_candidato = '"+id_candidato+"' ")

        banco.commit()

        banco.close()

        print("\nCandidato removido com sucesso!\n")

    except sqlite3.Error as erro:
        print("Solicitação apresentou ERRO ao exluir:", erro)


opcao = -1

while opcao != 0:
    
    print(39 * '-')
    print(" SISTEMA DE GERENCIAMENTO PARA SELEÇÃO")
    print(39 * '-')
    print('''
                | VAGAS |
        -------------------------
        * Estágiario
        * Analista de sistemas
        * Desenvolvedor Júnior
        * Desenvolvedor Pleno
        * Desenvolvedor Sênior  
        -------------------------''')
    print('''

    Escolha dentre as opções:

    [1] - Inserir candidato
    [2] - Mostrar candidatos
    [3] - Atualizar dados do candidato
    [4] - Excluir candidato
    [0] - Sair''')

    opcao = int(input("\nInforme a opção desejada: "))

    if opcao == 1:
        inserir()

    elif opcao == 2:
        mostrar()
    elif opcao == 3:
        print("\nEscolha:\n")
        print(" [1] - NOME")
        print(" [2] - IDADE")
        print(" [3] - EMAIL")
        print(" [4] - VAGA")
        op = int(input("\nInforme a operação desejada: "))
        atualizar(op)

    elif opcao == 4:
        delete()
    elif opcao == 0:
        banco.close()
        print("\nDesconectando do sistema...\n")
