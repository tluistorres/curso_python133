class Televisão:
    def __init__(self, canal_min, canal_max):
        self.ligada = False
        self.canal = canal_min
        self.canal_min = canal_min
        self.canal_max = canal_max

    def muda_canal_para_baixo(self):
        if self.ligada and self.canal - 1 >= self.canal_min:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.ligada and self.canal + 1 <= self.canal_max:
            self.canal += 1

    def liga_desliga(self):
        self.ligada = not self.ligada

class Pilha:
    def __init__(self, energia=100):
        self.energia = energia

    def consumo(self, consumo):
        if consumo > self.energia:
            consumo = self.energia
        self.energia -= consumo
        return self.energia

class ControleRemoto:
    def __init__(self, televisão, pilha):
        self.televisão = televisão
        self.pilha = pilha

    def liga(self):
        if not self.televisão.ligada and self.pilha.consumo(1) > 0:
            self.televisão.ligada = True

    def desligada(self):
        if self.televisão.ligada and self.pilha.consumo(1) > 0:
            self.televisão.ligada = False

    def canal_mais(self):
        if self.pilha.consumo(1) > 0:
            self.televisão.muda_canal_para_cima()

    def canal_menos(self):
        if self.pilha.consumo(1) > 0:
            self.televisão.muda_canal_para_baixo()

# Fazer no interpretador do Python os seguintes comandos:

# python -i remoto.py ( 1º comando ):

# >>>tv = Televisão(2, 14)
# >>>pilha = Pilha(5)
# >>>controle = ControleRemoto(tv, pilha)
# >>>tv.canal
# 2
# >>>pilha.energia 
# 5
# >>>controle.canal_mais()
# >>>tv canal
# 3
# >>>tv.ligada
# False
# >>>controle.liga
# tv.ligada
# True