import math

class Valor:
    def __init__(self, data, progenitor=(), operador_mae="", rotulo=""):
        self.data = data
        self.progenitor = progenitor
        self.operador_mae = operador_mae
        self.rotulo = rotulo
        self.grad = 0

    def __repr__(self):
        return f"Valor(data={self.data})"

    def __add__(self, outro_valor):
        if not isinstance(outro_valor, Valor): # Chega se é uma instância
            outro_valor = Valor(outro_valor)
        data = self.data + outro_valor.data
        progenitor = (self, outro_valor)
        operador_mae = "+"
        saida = Valor(data, progenitor, operador_mae)

        def propagar_adicao():
            self.grad += saida.grad * 1
            outro_valor.grad += saida.grad * 1

        saida.propagar = propagar_adicao

        return saida
    
    def __radd__(self, outro_valor): # Adição de outro_valor + self, faz a troca caso a soma não funcione
        return self + outro_valor

    def __mul__(self, outro_valor):
        if not isinstance(outro_valor, Valor): # Chega se é uma instância é um valor
            outro_valor = Valor(outro_valor)
        data = self.data * outro_valor.data
        progenitor = (self, outro_valor)
        operador_mae = "*"
        saida = Valor(data, progenitor, operador_mae)

        def propagar_multiplicacao():
            self.grad += saida.grad * outro_valor.data
            outro_valor.grad += saida.grad * self.data

        saida.propagar = propagar_multiplicacao

        return saida
    
    def __rmul__(self, outro_valor): # Multiplicação de outro_valor * self, faz a troca caso a operação não funcione
        return self * outro_valor
    
    def __pow__(self, expoente): # self ** expoente
        
        assert isinstance(expoente, (int, float)) # Assegura que a condição é verdadeira
        
        data = self.data ** expoente
        progenitor = (self,)
        operador_mae = f'**{expoente}'
        saida = Valor(data, progenitor, operador_mae)

        def propagar_exponenciacao():
            self.grad += saida.grad * expoente * (self.data ** (expoente - 1))

        saida.propagar = propagar_exponenciacao

        return saida
    
    def __truediv__(self, outro_valor): # self / outro_valor
        return self * outro_valor ** (-1)
        
    def __neg__(self): # - self
        return self * (-1)
    
    def __sub__(self, outro_valor): # self - outro_valor
        return self + (-outro_valor)
    
    def __rsub__(self, outro_valor): # outro_valor - self
        return self * (-1) + outro_valor
      
    def exp(self): # Não precisa de argumento, é a exponencial do número fornecido
        data = math.exp(self.data)
        progenitor = (self,) # o uso da vírgula é para o Python interprete como uma tupla e não como prioridade matemática
        operador_mae = 'exp'
        saida = Valor(data, progenitor, operador_mae)

        def propagar_exp():
            self.grad += saida.grad * data # A derivada da exponencial é ela mesma

        saida.propagar = propagar_exp

        return saida
    
    def sig(self):
        return self.exp() / (self.exp() + 1)

    def propagar(self):
        pass

    def propagar_tudo(self):
        ordem_topologica = []
        visitados = set()

        def constroi_ordem_topologica(v):
            if v not in visitados:
                visitados.add(v)
                for progenitor in v.progenitor:
                    constroi_ordem_topologica(progenitor)
                ordem_topologica.append(v)

        constroi_ordem_topologica(self)

        self.grad = 1  # o gradiente do vértice folha deve ser 1

        for v in reversed(ordem_topologica):
            v.propagar() 
