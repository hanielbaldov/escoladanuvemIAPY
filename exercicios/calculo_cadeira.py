# Esse código tem o objetivo de calcular o preço total do produto 

#Variaveis com detalhes do produto
nome_produto = "Cadeira infantil"
preco_unitario = 12.40
quantidade = 3 

#Variavel com preço total do produto 
preco_total = quantidade * preco_unitario 


print(f"Produto: {nome_produto}")
print(f"Preço unitário: {preco_unitario: .2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total {preco_total: .2f}")