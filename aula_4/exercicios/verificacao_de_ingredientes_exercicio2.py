# Verificação de Ingredientes
# Dado dois conjuntos de ingredientes, 
# exiba os ingredientes comuns entre eles e os que estão disponíveis apenas em um conjunto.

ingredientes_1 = {"tomate", "bacon", "ovo", "queijo"}
ingredientes_2 = {"presunto", "bacon", "ovo", "pepperoni"}

ingredientes_comum = ingredientes_1.intersection(ingredientes_2)
ingredientes_unicos = ingredientes_1 ^ (ingredientes_2)

print("Ingredientes comuns:", ingredientes_comum)

print("Ingredientes exclusivos:", ingredientes_unicos)
