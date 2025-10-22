#criando a classe Tabuleiro
class Tabuleiro():
    #o init cria o tabuleiro, inicialmente vazio, formado de listas de listas
    def __init__(self)-> None:
        self.tabuleiro = [["","","","","","","",""],
                          ["","","","","","","",""],
                          ["","","","","","","",""],
                          ["","","","","","","",""],
                          ["","","","","","","",""],
                          ["","","","","","","",""],
                          ["","","","","","","",""],
                          ["","","","","","","",""]]

    def is_vazia(self, posicao: tuple)-> bool:
        # o metodo verifica se alguma casa está vazia
        if self.tabuleiro[posicao[0]][posicao[1]]:
            return False
        else:
            return True

    def is_no_tabuleiro(self, nova_posicao: tuple)-> bool: 
        # o metodo verifica se uma posição está no tabuleiro
        if nova_posicao[0] >= 0 and nova_posicao[0] < 8 and nova_posicao[1] >= 0 and nova_posicao[1] < 8:
            return True
        else:
            return False
        
    def print_tabuleiro(self)-> None:
        #printa o tabuleiro atual no formato 8x8
        for c in self.tabuleiro:
            print(c)
        

#criando a classe Peca
class Peca():
    #Argumentos: Nome, posição inicial e o tabuleiro em q ela está
    #faz uma agregação com Tabuleiro
    def __init__(self, nome: str, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        self.posicao_inicial = posicao_inicial
        self.nome = nome
        tabuleiro.tabuleiro[posicao_inicial[0]][posicao_inicial[1]] = self.nome

    def is_padrao_de_movimento(self, posicao: tuple)-> bool:
        #metodo q verifica se o movimento pode ser feita pela peca 
        # (está no padrão), pra Peca() é generica
        return True

    def mover(self, nova_posicao: tuple, tabuleiro: Tabuleiro)-> None:
        #o metodo coloca a peca na nova posição (se possivel) e apaga a antiga
        if tabuleiro.is_vazia(nova_posicao) and tabuleiro.is_no_tabuleiro(nova_posicao) and self.is_padrao_de_movimento(nova_posicao):
            tabuleiro.tabuleiro[self.posicao_inicial[0]][self.posicao_inicial[1]] = ""
            tabuleiro.tabuleiro[nova_posicao[0]][nova_posicao[1]] = self.nome
            self.posicao_inicial = nova_posicao
            print("Movimento Válido")
        else:
            print("Movimento Inválido")

#As classe das pecas herdam da classe Peca(), então são iguais o __init__() 
# e mover(), so mudando o is_padrao_de_movimento
#classe Peao()
class Peao(Peca):
    def __init__(self, nome: str, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        super().__init__(nome, posicao_inicial, tabuleiro)
    
    #retorna True se a peca está sendo movida uma ou duas casa a frente
    def is_padrao_de_movimento(self, posicao: tuple)-> bool:
        if (posicao[0] == self.posicao_inicial[0] + 1 or posicao[0] == self.posicao_inicial[0] + 2) and posicao[1] == self.posicao_inicial[1]:
            return True
        else: 
            return False

    def mover(self, nova_posicao: tuple, tabuleiro: Tabuleiro)-> None:
        return super().mover(nova_posicao, tabuleiro)


#classe Torre()
class Torre(Peca):
    def __init__(self, nome: str, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        super().__init__(nome, posicao_inicial, tabuleiro)

    def is_padrao_de_movimento(self, posicao: tuple) -> bool:
        #retorna True somente se a torre se move apenas na vertica ou apenas na horizontal
        if posicao[0] == self.posicao_inicial[0] or posicao[1] == self.posicao_inicial[1]:
            return True
        else:
            return False
        
    def mover(self, nova_posicao: tuple, tabuleiro: Tabuleiro)-> None:
        return super().mover(nova_posicao, tabuleiro)
    

#classe Bispo()
class Bispo(Peca):
    def __init__(self, nome: str, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        super().__init__(nome, posicao_inicial, tabuleiro)
    
    def is_padrao_de_movimento(self, posicao: tuple) -> bool:
        #calculando o modulo de x e y (variação)
        modulo_x = abs(posicao[0] - self.posicao_inicial[0])
        modulo_y = abs(posicao[1] - self.posicao_inicial[1])

        # o movimentp é diagonal somente se foi andado a mesma quantidade de 
        #casas andadas na horizontal for a mesma na vertical
        if modulo_x == modulo_y:
            return True
        else:
            return False
        
    def mover(self, nova_posicao: tuple, tabuleiro: Tabuleiro)-> None:
        return super().mover(nova_posicao, tabuleiro)
    
    
#classe Cavalo()    
class Cavalo(Peca):
    def __init__(self, nome: str, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        super().__init__(nome, posicao_inicial, tabuleiro)
   
    def is_padrao_de_movimento(self, posicao: tuple) -> bool:
        modulo_x = abs(posicao[0] - self.posicao_inicial[0])
        modulo_y = abs(posicao[1] - self.posicao_inicial[1])

        #o moviemnto de L pode ser representado como duas casa a uma direção
        # e uma pra outra. O codigo verifica se essa é a condição da nova 
        if (modulo_x == 2 and modulo_y == 1) or (modulo_x == 1 and modulo_y == 2):
            return True
        else:
            return False
        
    def mover(self, nova_posicao: tuple, tabuleiro: Tabuleiro)-> None:
        return super().mover(nova_posicao, tabuleiro)
    
#classe Rainha()
class Rainha(Peca):
    def __init__(self, nome: str, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        #faz uma composição com Bispo e Torre
        super().__init__(nome, posicao_inicial, tabuleiro)
        self.bispo = Bispo(nome, posicao_inicial , tabuleiro)
        self.torre = Torre(nome, posicao_inicial, tabuleiro)
    
    def is_padrao_de_movimento(self, posicao: tuple)-> bool:
        #usa os metodos de Bispo e Torre para definir o padrão de movimento de Rainha
        if self.bispo.is_padrao_de_movimento(posicao) or self.torre.is_padrao_de_movimento(posicao):
            return True
        else:
            return False

    def mover(self, nova_posicao, tabuleiro)-> None:
        return super().mover(nova_posicao, tabuleiro)
    

#classe Rei()
class Rei(Peca):
    def __init__(self, nome, posicao_inicial: tuple, tabuleiro: Tabuleiro)-> None:
        super().__init__(nome, posicao_inicial, tabuleiro)

    def is_padrao_de_movimento(self, posicao: tuple) -> bool:
        modulo_x = abs(posicao[0] - self.posicao_inicial[0])
        modulo_y = abs(posicao[1] - self.posicao_inicial[1])

        #verifica se anda somente uma casa em alguma direção
        if modulo_x <= 1 and modulo_y <= 1 and (posicao != self.posicao_inicial):
            return True
        else:
            return False
        
    def mover(self, nova_posicao: tuple, tabuleiro: Tabuleiro)-> None:
        return super().mover(nova_posicao, tabuleiro)


#classe Jogo()
class Jogo:
    #cria um tabuleiro ao ser criado (composição)
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.pecas = []

    def adicionar_peca(self, peca: Peca):
        #adicona peca ao jogo
        self.pecas.append(peca)

    def mover_peca(self, peca: Peca, nova_posicao: tuple):
        #move a peca, por meio do metodo mover() de Peca()
        peca.mover(nova_posicao, self.tabuleiro)

    def mostrar_tabuleiro(self):
        #printa o tabuleiro
        self.tabuleiro.print_tabuleiro()


#TESTE
#instanciando os objeto
#criando um Jogo() (que cria uma Tabuleiro())
jogo = Jogo()

#Instanciando as Pecas e colocando elas no tabuleiro
p1 = Peao("P", (1, 0), jogo.tabuleiro)
t1 = Torre("T", (0, 0), jogo.tabuleiro)
b1 = Bispo("B", (0, 2), jogo.tabuleiro)
c1 = Cavalo("C", (0, 1), jogo.tabuleiro)
q1 = Rainha("Q", (0, 3), jogo.tabuleiro)
k1 = Rei("K", (0, 4), jogo.tabuleiro)

#adicionando as pecas ao jogo
for p in [p1, t1, b1, c1, q1, k1]:
    jogo.adicionar_peca(p)

#Teste Prático:
print("Tabuleiro inicial:")
jogo.mostrar_tabuleiro()

print("Movendo peão duas casas:")
jogo.mover_peca(p1, (3, 0))
jogo.mostrar_tabuleiro()

print("Movendo torre na coluna:")
jogo.mover_peca(t1, (2, 0))
jogo.mostrar_tabuleiro()

print("Movendo bispo na diagonal:")
jogo.mover_peca(b1, (2, 4))
jogo.mostrar_tabuleiro()

print("Movendo cavalo em L:")
jogo.mover_peca(c1, (2, 2))
jogo.mostrar_tabuleiro()

print("Movendo rainha na diagonal:")
jogo.mover_peca(q1, (3, 6))
jogo.mostrar_tabuleiro()

print("Movendo rei uma casa:")
jogo.mover_peca(k1, (1, 4))
jogo.mostrar_tabuleiro()

#Testando movimento Invalidos:

#movimento fora do padrão da peca:
print("\nTeste: Movimento inválido do Cavalo")
jogo.mover_peca(c1, (3, 3))  
print("\nTeste: Movimento inválido do Peão")
jogo.mover_peca(p1, (3, 1))  

#casa ocupada
print("\nTeste: Movimento para casa ocupada")
jogo.mover_peca(t1, (2, 4))  

"""Considerações Finais:
Seria possivel criar as peças pretas e ja colocar as peças na posição correta,
mas seria inutil, pois o jogo não é jogavel de qualquer jeito (não foi há
captura, por exemplo). Portanto optei por não adicionar essa funcionalidades."""
