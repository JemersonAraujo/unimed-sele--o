class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_em_ordem(No):
    if No:
        # Percorre a subárvore esquerda
        percorrer_em_ordem(No.esquerda)
        
        # Visita o nó atual
        print(No.valor, end=" ")
        
        # Percorre a subárvore direita
        percorrer_em_ordem(No.direita)

# Criar a árvore binária
raiz = No(3)
raiz.esquerda = No(2)
raiz.direita = No(5)
raiz.esquerda.esquerda = No(1)
raiz.esquerda.direita = No(4)

# Percorrer e imprimir a árvore em ordem
print("Árvore binária em ordem:")
percorrer_em_ordem(raiz)