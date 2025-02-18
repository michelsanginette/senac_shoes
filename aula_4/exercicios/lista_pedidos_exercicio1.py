# 1. **Lista de Pedidos**    
# Crie uma lista de sabores de pizzas pedidos` pelo cliente. Adicione `3 sabores à lista` e `remova 1 sabor.` Exiba o pedido final.

sabores = ['Mussarela', 'Calabresa', 'Frango com Catupiry']

sabores.append('Portuguesa')
sabores.append('Bacon')
sabores.append('Marguerita')

sabores.remove('Calabresa')

print("Pedido final da pizza:", sabores)