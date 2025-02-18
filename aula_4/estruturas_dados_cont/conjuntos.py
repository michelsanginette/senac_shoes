'''
Os conjuntos não são ordenados, são mutáveis, heterogêneos ou homogêneos e não permitem elementos dupkicados.
'''

# Declaração dos conjuntos
ingredientes = {"mussarela", "calabresa", "tomate", "azeitona"}
print("🧀 Ingredientes básicos: ", ingredientes)

# Operações com os conjuntos
# Adicionar itens:
ingredientes.add("orégano")
print("🧀 Ingredientes atualizados: ", ingredientes)

# Remover itens:
ingredientes.remove("azeitona")
print("🧀 Ingredientes após remoção: ", ingredientes)

# União de conjuntos:
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("🍅 Todos os ingredientes:", todos_ingredientes)

# Interseção de conjuntos: Aparecem em ambos os conjuntos
pizza_vegana = {"tomate", "azeitona", "rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("🥬 Ingredientes comuns:", comuns)



