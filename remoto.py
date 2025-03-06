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
