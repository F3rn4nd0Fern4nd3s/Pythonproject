'''
Soma dos valores dos produtos!!
'''

carrinho = []

carrinho.append(('Produto 1', 30.53))
carrinho.append(('Produto 2', 20.254))
carrinho.append(('Produto 3', 50.253))
carrinho.append(('Produto 3', 20.251))
carrinho.append(('Produto 3', 53.259))

x = sum([float(t2) for t1, t2 in carrinho]) # soma todos os valores dos produtos  't2' !!


print(x)
