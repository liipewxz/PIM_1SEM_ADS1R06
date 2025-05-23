
import json
import os

ARQUIVO = "usuarios_com_cursos.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    else:
        return []

def salvar_dados(lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

cursos_disponiveis = ['Lógica', 'Segurança Digital', 'Introdução à Programação', 'Redes de Computadores', 'Banco de Dados', 'Empreendedorismo Digital']

def registrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    print("Cursos disponíveis:")
    for i, curso in enumerate(cursos_disponiveis, 1):
        print(f"{i}. {curso}")
    opcao_curso = int(input("Escolha o número do curso: "))
    curso = cursos_disponiveis[opcao_curso - 1]
    
    nota = float(input("Nota final (0 a 10): "))
    senha = input("Crie uma senha (mínimo 6 caracteres): ")

    if len(senha) < 6:
        print("⚠️ Senha fraca. Tente novamente com mais de 6 caracteres.")
        return

    status = "Aprovado" if nota >= 7 else "Reprovado"
    
    usuario = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota,
        "status": status
    }

    dados = carregar_dados()
    dados.append(usuario)
    salvar_dados(dados)

    print("✅ Usuário cadastrado com sucesso!")

def mostrar_usuarios():
    print("\n--- Lista de Usuários ---")
    dados = carregar_dados()
    for usuario in dados:
        print(f"Nome: {usuario['nome']} | Curso: {usuario['curso']} | Nota: {usuario['nota']} | Status: {usuario['status']}")

def calcular_media():
    dados = carregar_dados()
    if not dados:
        print("Nenhum dado para calcular.")
        return
    soma = sum(usuario['nota'] for usuario in dados)
    media = soma / len(dados)
    print(f"\n📊 Média das notas dos alunos: {media:.2f}")

def menu():
    while True:
        print("\n--- Plataforma Digital ONG ---")
        print("1. Cadastrar novo usuário")
        print("2. Mostrar usuários cadastrados")
        print("3. Calcular média das notas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            mostrar_usuarios()
        elif opcao == "3":
            calcular_media()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
