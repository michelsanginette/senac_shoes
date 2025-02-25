'''### **Carrinho de Compras 🛒**

💡 **Enunciado**:

Crie um programa que permita adicionar produtos a um carrinho de compras. 
O programa deve continuar pedindo produtos até que o usuário digite "finalizar". 
No final, exiba todos os produtos comprados.

📝 **Regras:**

- O usuário digita o nome do produto e ele é adicionado a uma lista.
- Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.'''

carrinho = [] # Criação de uma lista vazia.

while True:
    produto = input("🛒 Digite um produto para adicionar ao carrinho ( ou 'finalizar' para encerrar): ")

    if produto.lower() == "finalizar":
        print("🛒 Fechando o carrinho.")
        break

    carrinho.append(produto) # Chamando a lista carrinho e adicionando o produto passado pelo cliente.
    print(f"✅ {produto} adicionado ao carrinho!")

if len(carrinho) > 0:
    print(" 🍉 Você comprou:")
    for item in carrinho:
        print(f'🛍️  {item}')
else:
    print("🛑 Nenhum produto foi comprado.")
