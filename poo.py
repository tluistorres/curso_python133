# Classes:

# - São modelos ou templates que definem as características e comportamentos de um objeto.
# - São definidas usando a palavra-chave class.
# - Podem conter atributos (variáveis) e métodos (funções).

# Objetos:

# - São instâncias de uma classe.
# - São criados a partir de uma classe usando a sintaxe objeto = Classe().
# - Herdam os atributos e métodos da classe.

# Atributos:

# - São variáveis que são definidas dentro de uma classe ou objeto.
# - Podem ser acessados usando a sintaxe objeto.atributo.

# Métodos:

# - São funções que são definidas dentro de uma classe ou objeto.
# - Podem ser chamados usando a sintaxe objeto.método().

# Orientação a objetos: Paradigma de Programação.

class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.num_registro = None

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadllac')
    meu_veiculo.movimentar( )
    print(meu_veiculo.fabricante)

# Neste caso não está preservado os atributos. Vamos inser o comando geter.

class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

# Setter

    def set_num_registro(self, registro):
        self.__num_registro = registro

# Getter.

    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')

    def get_num_registro(self):
        return self.__num_registro       
    
class Carro(Veiculo):

# Método init será herdado. Mas vamos criar um método movimentar com o mesmo nome anterior.
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro muito!')  # Polimorfismo.

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)    # É uma referência a classe veículo.

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print(f'Eu voo  alto!')  # Polimorfismo.
    
if __name__ == '__main__':

#    meu_veiculo = Veiculo('GM', 'Cadllac')
#    meu_veiculo.movimentar( )
#    meu_veiculo.get_fabr_modelo()
#    meu_veiculo.set_num_registro("134445-8")
#    print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    meu_carro = Carro('Volkswagen','Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Audi', 'AS Sportback') 
    seu_carro.movimentar()   # Posso criar quantos objetos quizermos usando a mesma classe.
    seu_carro.get_fabr_modelo()  

    moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    meu_aviao.get_categoria()
    print(f'Categoria: {meu_aviao.get_categoria()}')

# Sou um veículo e me desloco!
# Modelo: Cadllac, Fabricante: GM.

# Sou um carro e ando pelas ruas!
# Modelo: Polo, Fabricante: Volkswagen.

# Sou um carro e ando pelas ruas!
# Modelo: AS Sportback, Fabricante: Audi.

# Corro muito!
# Modelo: Nightster Special, Fabricante: Harley-Davidson.

# Eu voo  alto!
# Modelo: 747, Fabricante: Boeing.

# Categoria: Comercial.

# class Televisão:
#     def __init__(self, canal_min, canal_max):
#         self.ligada = False
#         self.canal = 2
#         self.canal_min = canal_min
#         self.canal_max = canal_max
#     def muda_canal_para_baixo(self):
#         if self.canal -1 >= self.canal_min:
#             self.canal -= 1
#     def muda_canal_para_cima(self):
#         if self.canal + 1 <= self.canal_max:
#             self.canal += 1
# tv = Televisão(1, 99)
# for x in range(0, 120):
#     tv.muda_canal_para_cima()
# print(tv.canal)
# for x in range(0, 120):
#     tv.muda_canal_para_baixo()
# print(tv.canal)

# Saída: 99 e 1.
         
# Apresenta todos os canais no max e min.

# class Televisão:
#     def __init__(self, canal_min, canal_max):
#         self.ligada = False
#         self.canal = canal_min
#         self.canal_min = canal_min
#         self.canal_max = canal_max

#     def muda_canal_para_baixo(self):
#         if self.ligada and self.canal - 1 >= self.canal_min:
#             self.canal -= 1

#     def muda_canal_para_cima(self):
#         if self.ligada and self.canal + 1 <= self.canal_max:
#             self.canal += 1

#     def liga_desliga(self):
#         self.ligada = not self.ligada

# class Pilha:
#     def __init__(self, energia=100):
#         self.energia = energia

#     def consumo(self, consumo):
#         if consumo > self.energia:
#             consumo = self.energia
#         self.energia -= consumo
#         return self.energia

# class ControleRemoto:
#     def __init__(self, televisão, pilha):
#         self.televisão = televisão
#         self.pilha = pilha

#     def liga(self):
#         if not self.televisão.ligada and self.pilha.consumo(1) > 0:
#             self.televisão.ligada = True

#     def desligada(self):
#         if self.televisão.ligada and self.pilha.consumo(1) > 0:
#             self.televisão.ligada = False

#     def canal_mais(self):
#         if self.pilha.consumo(1) > 0:
#             self.televisão.muda_canal_para_cima()

#     def canal_menos(self):
#         if self.pilha.consumo(1) > 0:
#             self.televisão.muda_canal_para_baixo()

# # Exemplo de uso
# tv = Televisão(1, 99)
# pilha = Pilha()
# controle = ControleRemoto(tv, pilha)

# controle.liga()
# print(tv.ligada)

# controle.canal_mais()
# print(tv.canal)

# controle.canal_menos()
# print(tv.canal)

# controle.desligada()
# print(tv.ligada)

# Saída: True
# 2
# 1
# False.

# Resumo: A associação de classes e objetos é possível graças aos conceitos de Programação Orientada a Objetos (POO). Aqui estão algumas razões pelas quais isso é possível:

# 1. Encapsulamento: As classes permitem encapsular dados e comportamentos, criando uma unidade autônoma que pode ser reutilizada.

# 2. Herança: As classes podem herdar propriedades e comportamentos de outras classes, permitindo a criação de hierarquias de classes.

# 3. Composição: As classes podem ser compostas por outras classes, permitindo a criação de objetos complexos.

# 4. Polimorfismo: As classes podem ter métodos com o mesmo nome, mas com comportamentos diferentes, permitindo a criação de objetos que podem ser tratados de maneira diferente.

# 5. Abstração: As classes permitem abstrair detalhes de implementação, permitindo que os objetos sejam tratados como unidades autônomas.

# A associação de classes e objetos permite:

# - Reutilização de código
# - Criação de sistemas complexos
# - Melhoria da legibilidade e manutenibilidade do código
# - Facilitação da comunicação entre os desenvolvedores

# Exemplos de associação de classes e objetos:

# - Uma classe Carro pode ter uma classe Motor como atributo.
# - Uma classe Universidade pode ter uma classe Departamento como atributo.
# - Uma classe ContaBancária pode ter uma classe Cliente como atributo.

# Executando o arquivo remoto.py no modo interativo do Python!

# Com o comando python -i remoto.py, você está:

# 1. Executando o arquivo remoto.py como um script Python.
# 2. Abrindo uma sessão interativa do Python após a execução do script.

# Isso permite que você:

# - Veja a saída do script.
# - Acesse as variáveis e funções definidas no script.
# - Execute comandos Python adicionais.

# Você pode usar isso para:

# - Depurar seu código.
# - Testar funções e variáveis.
# - Explorar o comportamento do seu script.

# Exemplo de um banco:


# Nesse exemplo, temos duas classes:

# - Cliente: representa um cliente com atributos como nome e telefone.
# - Conta: representa uma conta bancária com atributos como número, cliente, saldo e operações. Tem métodos para depositar, sacar, consultar o saldo e gerar o extrato.

# O exemplo de uso mostra como criar um cliente, criar uma conta, realizar operações bancárias e gerar o extrato da conta.

# Saída: 

# Depósito realizado com sucesso! Saldo atual: R$1500.00
# Saque realizado com sucesso! Saldo atual: R$1300.00
# Saldo atual: R$1300.00
# Extrato da conta:
# Depósito: R$500.00
# Saque: R$200.00
# Saldo atual: R$1300.00


# Essa saída mostra:

# 1. O depósito de R$500,00 realizado com sucesso e o saldo atualizado para R$1500,00.
# 2. O saque de R$200,00 realizado com sucesso e o saldo atualizado para R$1300,00.
# 3. O saldo atual da conta, que é R$1300,00.
# 4. O extrato da conta, que mostra as operações realizadas (depósito e saque) e o saldo atual.

# Nesse exemplo, temos duas contas correntes (conta1 e conta2) e dois clientes (cliente1 e cliente2). Cada conta tem suas próprias operações e saldo.

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Nº{self.número} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(['SAQUE', valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'EXTRATO CC Nº {self.número}\n')
        for operação in self.operações:
            print(f'{operação[0]:10s} {operação[1]:10.2f}')
        print(f'\n Saldo: {self.saldo:10.2f}\n')

# Criação de objetos
joão = Cliente("João da Silva", "4579-5678")
maria = Cliente("Maria da Silva", "7824-8085")
conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria, joão], 2, 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()

# Saida:

# EXTRATO CC Nº 1

# DEPÓSITO      1000.00
# SAQUE           50.00
# SAQUE          190.00

#  Saldo:     760.00

# EXTRATO CC Nº 2

# DEPÓSITO       500.00
# DEPÓSITO       300.00
# DEPÓSITO        95.15
# SAQUE          250.00

#  Saldo:     645.15.

# Criação do banco: Nesse exemplo, a classe Banco tem métodos para criar contas, listar contas e buscar contas. A classe Conta tem métodos para depositar, sacar e exibir o extrato. A classe Cliente tem um método para exibir o nome e telefone do cliente.

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"

class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(['DEPÓSITO', valor])

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(['SAQUE', valor])

    def extrato(self):
        print(f'EXTRATO CC Nº {self.número}\n')
        for operação in self.operações:
            print(f'{operação[0]:10s} {operação[1]:10.2f}')
        print(f'\n Saldo: {self.saldo:10.2f}\n')

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def criar_conta(self, clientes, número, saldo=0):
        conta = Conta(clientes, número, saldo)
        self.contas.append(conta)
        return conta

    def listar_contas(self):
        for conta in self.contas:
            print(f"Conta Nº {conta.número} - Clientes: {[cliente.nome for cliente in conta.clientes]}")

    def buscar_conta(self, número):
        for conta in self.contas:
            if conta.número == número:
                return conta
        return None

# Criação do banco
banco = Banco("Banco XYZ")

# Criação de clientes
joão = Cliente("João da Silva", "4579-5678")
maria = Cliente("Maria da Silva", "7824-8085")
pedro = Cliente("Pedro da Silva", "9123-4567")

# Criação de contas
conta1 = banco.criar_conta([joão], 1, 1000)
conta2 = banco.criar_conta([maria, joão], 2, 500)
conta3 = banco.criar_conta([pedro], 3, 2000)

# Listagem de contas
banco.listar_contas()

# Imprimir extratos das contas
conta1.extrato()
conta2.extrato()
conta3.extrato()

# Saída:

# Conta Nº 1 - Clientes: ['João da Silva']
# Conta Nº 2 - Clientes: ['Maria da Silva', 'João da Silva']
# Conta Nº 3 - Clientes: ['Pedro da Silva']


# EXTRATO CC Nº 1

# DEPÓSITO      1000.00

#  Saldo:    1000.00

# EXTRATO CC Nº 2

# DEPÓSITO       500.00

#  Saldo:     500.00

# EXTRATO CC Nº 3

# DEPÓSITO      2000.00

#  Saldo:    2000.00

########################################################################################

# Herança:

# A herança é um conceito fundamental na programação orientada a objetos (POO). Ela permite que uma classe herde as propriedades e métodos de outra classe, criando uma relação de pai-filho entre elas.

# Benefícios da Herança:

# 1. Reutilização de código: A herança permite reutilizar o código da classe pai, evitando a duplicação de código.
# 2. Hierarquia de classes: A herança ajuda a criar uma hierarquia de classes, onde as classes mais específicas herdam as propriedades e métodos das classes mais gerais.
# 3. Flexibilidade: A herança permite que as classes filhas adicionem ou modifiquem as propriedades e métodos herdadas da classe pai.

# Classe pai (ou superclasse).

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def imprimir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

# Classe filha (ou subclasse) que herda de Veiculo.

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)      # Chama o construtor da classe pai
        self.portas = portas

    def imprimir_informacoes(self):
        super().imprimir_informacoes()      # Chama o método da classe pai
        print(f"Portas: {self.portas}")

meu_carro = Carro("Volkswagen", "Gol", 2015, 4)     # Criação de objetos

meu_carro.imprimir_informacoes()          # Chamada ao método imprimir_informacoes()

# Saída:

# Marca: Volkswagen
# Modelo: Gol
# Ano: 2015
# Portas: 4

# Nesse exemplo, a classe ContaEspecial herda da classe Conta e adiciona um atributo limite que representa o limite de saque da conta. O método sacar é sobrescrito para considerar o limite de saque.

class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return self.saldo

class ContaEspecial(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# Criação de objetos
conta = Conta(123, "João")
conta_especial = ContaEspecial(456, "Maria", limite=2000)

# Testes
conta.depositar(1000)
print(conta.consultar_saldo())  # Saída: 1000
conta.sacar(500)
print(conta.consultar_saldo())  # Saída: 500

conta_especial.depositar(1000)
print(conta_especial.consultar_saldo())  # Saída: 1000
conta_especial.sacar(1500)
print(conta_especial.consultar_saldo())  # Saída: -5

# Saída: 

# 1000
# 500
# 1000
# -500

########################################################################################

# Essa classe Lista oferece métodos para adicionar, remover, buscar, imprimir, obter o tamanho, limpar, ordenar e reverter a lista.

class Lista:
    def __init__(self):
        self.elementos = []

    def adicionar(self, elemento):
        self.elementos.append(elemento)

    def remover(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
        else:
            print("Elemento não encontrado na lista")

    def buscar(self, elemento):
        return elemento in self.elementos

    def imprimir(self):
        print(self.elementos)

    def tamanho(self):
        return len(self.elementos)

    def limpar(self):
        self.elementos.clear()

    def ordenar(self):
        self.elementos.sort()

    def reverso(self):
        self.elementos.reverse()

lista = Lista()      # Exemplo de uso.

# Adicionar elementos

lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)

# Imprimir lista

lista.imprimir()  # Saída: [1, 2, 3, 4, 5]

# Remover elemento

lista.remover(3)

# Imprimir lista

lista.imprimir()  # Saída: [1, 2, 4, 5]

# Buscar elemento

print(lista.buscar(4))  # Saída: True

# Tamanho da lista

print(lista.tamanho())  # Saída: 4

# Limpar lista

lista.limpar()

# Imprimir lista

lista.imprimir()  # Saída: []

# Ordenar lista (não funciona com lista vazia)

lista.adicionar(5)
lista.adicionar(2)
lista.adicionar(8)
lista.ordenar()
lista.imprimir()  # Saída: [2, 5, 8]

# Reverso da lista

lista.reverso()
lista.imprimir()  # Saída: [8, 5, 2]

# Saida: 

# [1, 2, 3, 4, 5]
# [1, 2, 4, 5]
# True
# 4
# []
# [2, 5, 8]
# [8, 5, 2]

# Aqui está um exemplo de uma classe ListaUnica que garante que os elementos adicionados sejam únicos:

class ListaUnica:
    def __init__(self):
        self.elementos = []

    def adicionar(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remover(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
        else:
            print("Elemento não encontrado na lista")

    def buscar(self, elemento):
        return elemento in self.elementos

    def imprimir(self):
        print(self.elementos)

    def tamanho(self):
        return len(self.elementos)

    def limpar(self):
        self.elementos.clear()

# Exemplo de uso:

lista = ListaUnica()

# Adicionar elementos
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(2)  # Não adiciona novamente o elemento 2
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(4)  # Não adiciona novamente o elemento 4

# Imprimir lista
lista.imprimir()  # Saída: [1, 2, 3, 4]

# Remover elemento
lista.remover(3)

# Imprimir lista
lista.imprimir()  # Saída: [1, 2, 4]

# Buscar elemento
print(lista.buscar(4))  # Saída: True

# Tamanho da lista
print(lista.tamanho())  # Saída: 3

# Limpar lista
lista.limpar()

# Imprimir lista
lista.imprimir()  # Saída: []

# Saída:

# [1, 2, 3, 4]
# [1, 2, 4]
# True
# 3
# []

# Chave como propriedade apenas para leitura(nome.py)

from functools import total_ordering

class Nome:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

nome = Nome("João")       # Criar uma instância da classe Nome

print(nome.nome)   # Acessar a propriedade nome com Saída: João

try:                            # Tentar modificar a propriedade nome.
    nome.nome = "Maria"
except AttributeError:
    print("A propriedade nome é apenas para leitura")

nome = Nome("João")       # Criar uma instância da classe Nome

print(nome.nome)   # Acessar a propriedade nome com Saída: João



# Saída:

# João
# A propriedade nome é apenas para leitura.

# Programa 10.2 Chave como propriedade apaenas para leitura(nome.py):

from functools import total_ordering

@total_ordering

class Nome:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    def __repr__(self):
        return f'<Class {type(self).__name__} em 0x{id(self):x} Nome: {self.__nome} Chave: {self.__chave}>'
    def __eq__(self, outro):
        return self.nome == outro.nome
    def __lt__(self, outro):
        return self.nome < outro.nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if valor is None or not valor.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()
    nome = Nome("João")
print(repr(nome))  # Saída: <Class Nome em 0x7f937f16c9d0 Nome: João Chave: joão>
# A propriedade nome é apenas para leitura
# João
# <__main__.Nome object at 0x000001A99D1DD950>

# Explicação deste procedimento: Pontos positivos:
# 1. Uso de decoradores: O uso do decorador @total_ordering é uma boa prática para implementar a ordenação total na classe.
# 2. Implementação de métodos especiais: A implementação dos métodos especiais __str__, __repr__, __eq__ e __lt__ é correta e permite uma representação adequada da classe.
# 3. Uso de propriedades: O uso de propriedades (@property) é uma boa prática para encapsular os atributos da classe e fornecer uma interface de acesso controlada.
# 4. Validação de dados: A validação de dados no setter da propriedade nome é uma boa prática para garantir a consistência dos dados.

# Código melharado segumdo o "ChapGpt" da Meta:

from functools import total_ordering

@total_ordering
class Nome:
    """
    Classe que representa um nome.

    Atributos:
        nome (str): O nome.
        chave (str): A chave do nome (nome em minúsculas).
    """

    def __init__(self, nome):
        """
        Inicializa a classe Nome.

        Args:
            nome (str): O nome.
        """
        self.nome = nome

    def __str__(self):
        """
        Retorna o nome como string.

        Returns:
            str: O nome.
        """
        return self.nome

    def __repr__(self):
        """
        Retorna a representação da classe Nome.

        Returns:
            str: A representação da classe Nome.
        """
        return f"<Class {type(self).__name__} em 0x{id(self):x} Nome: {self.nome} Chave: {self.chave}>"

    def __eq__(self, outro):
        """
        Verifica se dois nomes são iguais.

        Args:
            outro (Nome): O outro nome.

        Returns:
            bool: True se os nomes forem iguais, False caso contrário.
        """
        return self.nome == outro.nome

    def __lt__(self, outro):
        """
        Verifica se um nome é menor que outro.

        Args:
            outro (Nome): O outro nome.

        Returns:
            bool: True se o nome for menor que o outro, False caso contrário.
        """
        return self.nome < outro.nome

    @property
    def nome(self):
        """
        Retorna o nome.

        Returns:
            str: O nome.
        """
        return self._nome

    @nome.setter
    def nome(self, valor):
        """
        Define o nome.

        Args:
            valor (str): O nome.

        Raises:
            ValueError: Se o nome for nulo ou em branco.
        """
        if valor is None or not valor.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self._nome = valor
        self._chave = self._cria_chave(valor)

    @property
    def chave(self):
        """
        Retorna a chave do nome.

        Returns:
            str: A chave do nome.
        """
        return self._chave

    @staticmethod
    def _cria_chave(nome):
        """
        Cria a chave do nome.

        Args:
            nome (str): O nome.

        Returns:
            str: A chave do nome.
        """
        return nome.strip().lower()
# Criar uma instância da classe Nome
nome = Nome("João")

# Printar o nome
print(nome)

# Printar a chave do nome
print(nome.chave)

# Criar outra instância da classe Nome
nome2 = Nome("Maria")

# Comparar os nomes
print(nome < nome2)  # Saída: True
print(nome == nome2)  # Saída: False

# Isso significa que:

# - O nome é "João".
# - A chave do nome (em minúsculas) é "joão".
# - O nome "João" é menor que o nome "Maria" (True).
# - O nome "João" não é igual ao nome "Maria" (False).

# Esse código criará uma instância da classe Nome, printará o nome e a chave do nome, e comparará dois nomes.


# As principais mudanças incluem:

# - Adição de docstrings para explicar o propósito da classe, métodos e atributos.
# - Uso de convenção de nomenclatura única (PEP 8) para os atributos e métodos.
# - Melhoria na estrutura e organização do código.
# - Adição de raises para os métodos que podem levantar exceções.


########################################################################################

# Atributos e métodos de classe:

# Atributos de Classe:

# Atributos de classe são variáveis que são compartilhadas por todas as instâncias de uma classe. Eles são definidos dentro da definição da classe, mas fora de qualquer método.

# Exemplo:

class Veiculo:
    tipo = "veiculo"

    def __init__(self, cor):
        self.cor = cor
print(Veiculo.tipo)  # Acessar o atributo de classe
                       
carro = Veiculo("azul") # Criar uma instância da classe
print(carro.tipo) 

 # Acessar o atributo de classe através da instância Saída: veiculo

# Atributos de Instância:

# Atributos de instância são variáveis que são únicas para cada instância de uma classe. Eles são definidos dentro do método __init__ da classe.

# Exemplo:

class Veiculo:
    def __init__(self, cor):
        self.cor = cor
carro = Veiculo("azul")   # Criar uma instância da classe.

print(carro.cor)  # Acessar o atributo de instância: Saída: azul.

# Métodos de Classe:

# Métodos de classe são funções que são compartilhadas por todas as instâncias de uma classe. Eles são definidos dentro da definição da classe e são chamados utilizando o nome da classe.

# Exemplo:

class Veiculo:
    def __init__(self, cor):
        self.cor = cor

    def descricao(self):
        return f"Veiculo {self.cor}"

carro = Veiculo("azul")   # Criar uma instância da classe

# print(carro.descricao())  # Chamar o método de classe: Saída: Veiculo azul.


# Métodos Estáticos:

# Métodos estáticos são funções que não dependem de nenhuma instância da classe e não têm acesso aos atributos da classe. Eles são definidos utilizando o decorador @staticmethod.

# Exemplo:

class Veiculo:
    def __init__(self, cor):
        self.cor = cor

    @staticmethod
    def calcular_velocidade(distancia, tempo):
        return distancia / tempo

velocidade = Veiculo.calcular_velocidade(100, 5)  # Chamar o método estático.
print(velocidade)                 # Saída: 20.0.

# Saída:

# veiculo
# veiculo
# azul
# 20.0

#########################################################################################