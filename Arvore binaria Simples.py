class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_em_ordem(No):
    if No:
        
        percorrer_em_ordem(No.esquerda)
       
        print(No.valor, end=" ")
        
        percorrer_em_ordem(No.direita)


raiz = No(3)
raiz.esquerda = No(2)
raiz.direita = No(5)
raiz.esquerda.esquerda = No(1)
raiz.esquerda.direita = No(4)


print("Árvore binária em ordem:")
percorrer_em_ordem(raiz)