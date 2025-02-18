# 3. **Atualizar Cardápio**
    
# Crie um dicionário para o cardápio e adicione um novo sabor com preço. 
# Atualize o preço de um sabor existente e remova um sabor do cardápio.

cardapio = {
    "Mussarela": 29.90,
    "Calabresa": 32.90,
    "Frango com Catupiry": 39.90,
    "Quatro Queijos": 43.90
}

cardapio["Pepperoni"] = 38.90

cardapio["Mussarela"] = 32.90

cardapio.pop("Calabresa")

print("Cardápio atualizado:")
for sabor, preco in cardapio.items():
    print(f'{sabor}: R${preco:.2f}')