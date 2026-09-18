alunos = []


def menu():
    print("\n===== SISTEMA DE CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Consultar alunos")
    print("3 - Atualizar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")


def cadastrar():
    print("\n===== CADASTRO DE ALUNO =====")

    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")


def consultar():
    print("\n===== ALUNOS CADASTRADOS =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"\nAluno {i}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")


def atualizar():
    print("\n===== ATUALIZAR ALUNO =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    consultar()

    try:
        numero = int(input("\nDigite o número do aluno que deseja atualizar: "))
        indice = numero - 1

        if indice < 0 or indice >= len(alunos):
            print("Aluno não encontrado.")
            return

        novo_nome = input("Novo nome: ")
        nova_idade = input("Nova idade: ")
        novo_curso = input("Novo curso: ")

        alunos[indice]["nome"] = novo_nome
        alunos[indice]["idade"] = nova_idade
        alunos[indice]["curso"] = novo_curso

        print("\nAluno atualizado com sucesso!")

    except ValueError:
        print("Digite um número válido.")


def excluir():
    print("\n===== EXCLUIR ALUNO =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    consultar()

    try:
        numero = int(input("\nDigite o número do aluno que deseja excluir: "))
        indice = numero - 1

        if indice < 0 or indice >= len(alunos):
            print("Aluno não encontrado.")
            return

        aluno_removido = alunos.pop(indice)

        print(f"\nAluno {aluno_removido['nome']} excluído com sucesso!")

    except ValueError:
        print("Digite um número válido.")


while True:
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        consultar()

    elif opcao == "3":
        atualizar()

    elif opcao == "4":
        excluir()

    elif opcao == "5":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")