#CRUD: sigla para Create, Read, Update e Delete.


#Importa uma biblioteca dentro do seu código
import sqlite3

#criação da conexão com o banco de dados e definição um objeto de representação =>
def criar_tabela():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXIXTTS usuarios (
                         id INTEGER PRIMARY KEY,
                         nome TEXT NOT NUL,
                         idade INTEGER)''')
    
    conexao.commit()
    conexao.close()

#Criação das funções =>
def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (?, ?)''', (nome, idade))
    conexao.commit()
    conexao.close()

#Leitura dos dados da tabela =>
def listar_usuarios():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

#Atualizar os dados da tabela =>
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?''',(nome, idade, id))
    conexao.commit()
    conexao.close()

#Função Deletar =>
def deletar_usuario(id):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FORM usuarios WHERE id = ?''',(id,))
    conexao.commit()
    conexao.close()

#Menu de Interface gráfica =>
def menu():
    print("\n1. Adicionar Usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")


#lógica de Interação com o Usuário =>
criar_tabela()

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        adicionar_usuario(nome, idade)
        print("Usuário adicionado com sucesso!")
    elif escolha == '2':
        print("\nTodos os usuários:")
        listar_usuarios()
    elif escolha == '3':
        id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        atualizar_usuario(id, nome, idade)
        print("Usuário atualizado com sucesso!")
    elif escolha == '4':
        id = int(input("Digite o ID do usuário a ser deletado: "))
        deletar_usuario(id)
        print("Usuário deletado com sucesso!")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


