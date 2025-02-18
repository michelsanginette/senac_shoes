"""
Homogêneo -> Aceita apenas um tipo de dado.
Heterogêneo -> Aceita dados de tipos diferentes.
As estruturas de dados são declaradas com snake_case;
"""

# Declaração Listas
# Ordenadas, mutáveis e heterogêneas

sabores = ["mussarela", "calabresa", "frango com catupiry", "portuguesa"]
dados_pizza = ["mussarela", 26.90, True]
# print("Sabores disponíveis: ", sabores)
# print("Informações da Pizza: ", dados_pizza)


# Operações com Listas
# 1. append() -> Adiciona um novo valor ao final da lista.
sabores.append("marguerita")
print("Sabores disponíveis: ", sabores)

# 2. remove() -> Remove um elemento da lista.
sabores.remove("calabresa")
print("Sabores disponíveis: ", sabores)

# 3. Acessando os elementos. []
pizzas = ["mussarela", "calabresa", "frango com catupiry", "portuguesa"]
print(pizzas[0])
print(pizzas[1])
print(pizzas[-1])
