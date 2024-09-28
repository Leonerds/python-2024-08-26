# O que é uma classe: classe é uma forma de representar uma coisa do mundo real em um objeto
class Pessoa:
    # nome e id são parâmentros

    # __init__ é o que chamamos de construtor, tem como objeto construir
    # um objeto com os dados necessários para o funcionamento correto
    def __init__(self, id: int, nome: str):
        # propriedades da classe
        self.id = id
        self.nome = nome
        self.altura = 0.0
        self.idade = 0
        self.peso = 0.0

def exemplo_com_classe():
    # instanciando um objeto chamado batatinha da classe Pessoa
    francisco = Pessoa(1, "Francisco")
    # Definindo o valor para a propriedade altura que pertence ao objeto francisco
    francisco.altura = 1.72
    francisco.peso = 120
    francisco.idade = 30
    print(f"Id: {francisco.id}")
    print(f"Nome: {francisco.nome}")
    print(f"Altura: {francisco.altura}")
    print(f"Peso: {francisco.peso}")
    print(f"Idade: {francisco.idade}\n")

    william = Pessoa(2, "William")
    print(f"Id: {william.id}")
    print(f"Nome: {william.nome}")
    print(f"Altura: {william.altura}")
    print(f"Peso: {william.peso}")
    print(f"Idade: {william.idade}\n")

class Produto:
    def __init__(self, id: int, nome: str, preco_unitario: float, quantidade: int):
        self.id = id
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

from typing import List
def exemplo_com_lista_de_objetos():
    # Criando uma lista de produtos, que será armazenado os objetos da classe Produto
    produtos: List[Produto] = []

    # Instanciando um objeto do Produto chamado play_station
    play_station = Produto(1, "Playstation 5 Pro", 6999.99, 1)
    # Adicionar o produto na lista de produtos
    produtos.append(play_station)

    xbox_series_x = Produto(2, "Xbox Series X", 3500, 2)
    produtos.append(xbox_series_x)

    # Por trás dos panos está acontecendo isto:
    # for i in range (0, len(produtos)):
    #   produto = produtos[i]
    #   print(produto.nome)
    # Percorrendo a lista de produtos para apresentar
    for produto in produtos:
        total_produto = produto.preco_unitario * produto.quantidade
        print(produto.nome, total_produto)
        

class Aluno:
    def __init__(self, id: int, nome: str, nota1: int, nota2: int, nota3: int):
        self.id = id
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

from typing import List

def aprovacao_alunos():
    alunos: List[Aluno] = []

    aluno1 = Aluno(1, "Leo", 10, 9, 8)
    alunos.append(aluno1)

    aluno2 = Aluno(2, "Lele", 10, 9, 10)
    alunos.append(aluno2)

    aluno3 = Aluno(3, "Lulu", 5, 5, 3)
    alunos.append(aluno3) 

    for aluno in alunos: 
        media_notas = (aluno.nota1 + aluno.nota2 + aluno.nota3) / 3
        if media_notas >= 7:
            print("Parabéns, você está aprovado: ", aluno.nome, "Sua média foi: ", media_notas)
        else:
            print("Você está reprovado: ", aluno.nome, "Sua média foi: ", media_notas)

if __name__ == "__main__":
    aprovacao_alunos()
