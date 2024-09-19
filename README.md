# CRUD-Python

## Criando um CRUD simples com python
CRUD (sigla para Create, Read, Update e Delete, que são as operações básicas de um sistema de gerenciamento de banco de dados)


Primeiramente é necessário fazer as importações do sqlite pra criar a base de dados que vamos adicionar os dados.

```bash
import sqlite3
```
Depois, é necessário criar uma conexão com o banco de dados e definir um objeto que represente suas tabelas. Segue
o exemplo:

```bash
def criar_tabela():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        idade INTEGER)''')
    conexao.commit()
    conexao.close()
```

Agora você pode criar as funções que vão adicionar o usuario na base de dados:

```bash
def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (?, ?)''', (nome, idade))
    conexao.commit()
    conexao.close()
```

Para ler os dados da tabela, você pode utilizar a seguinte função:

```bash
def listar_usuarios():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()
```

Para atualizar os dados da tabela, você pode utilizar a seguinte função:

```bash
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?''', (nome, idade, id))
    conexao.commit()
    conexao.close()
```

Em seguida vamos fazer a função para deletar os usuarios na base de dados:

```bash
def deletar_usuario(id):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()
```

Vamos criar um menu para gerar uma interface grafica para interagir com o usuario no terminal:

```bash
def menu():
    print("\n1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")
```

No final do código foi criado uma logica para interação com o usuario:


```bash
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

```


                                                                                      😄   Lucas Cunha  😄
                                                                                        









