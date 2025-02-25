# AULA 01

## Nomenclatura
- Um arquivo .py em Python, chamamos de módulo.
- Uma pasta dentro do workspace, chamamos de diretório.

1. Cases
``snake_case`` -> Tudo minúsculo, palavras separadas por underline.
``camelCase`` -> Primeira letra da primeira palavra em minúsculo, e toda próxima palavra a primeira letra em maiúsculo.

## Observações
1. Python é uma linguagem fracamente tipada.

# AULA 2

1. Para informar quantas casas decimais você quer após a vírgula, utilizamos o comando =>  :.2f
2. Ao dividirmos dois números inteiros, caso seja necessário, ocorre uma conversão implícita [casting].

# AULA 3
1. Em Python, no momento que vamos realizar alguma operação, existe uma precedência.
Primeiramente, realizamos a * e a /.
Depois, a + e a - .
Podemos utiizar os () para quebrar ou organizar uma operação.

2. Em Python, toda vez que utilizamos o método `input()`, a entrada automaticamente será do tipo `string`.

3. Para converter uma `string` para `int` ou `float`, podemos utilizar os métodos `int()` ou `float()`.

# AULA 05
## ESTRUTURAS DE REPETIÇÃO
1. for
=> Você irá utilizar quando de antemão se sabe a quantidade de vezes que a repetição irá acontecer. Normalmente, é utilizado para `iterar` sobre elementos de uma sequência.
1.1 - range() => Gera uma sequência de números. (inclusivo, exclusivo).

2. while
=> Será utilizado quando você não sabe ao certo quantas vezes a repetição irá aontecer. Será executado enquanto a condição for verdadeira.

# AULA 06
## COMANDOS DE DESVIO
1. continue -> Significa continuar, basicamente se uma condição for favorável, ela será desconsiderada.
2. break -> Significa quebrar, quando utilizado irá finalizar o loop mais próximo.

## FUNÇÕES
=> é um bloco de código que é reutilizável. Serve para deixar o código mais organizado e eficiente. `Executam uma tarefa específica.`


# AULA 07
## PRINCÍPIOS DA PROGRAMAÇÃO ORIENTADA A OBJETOS (P.O.O.)
1. ENCAPSULAMENTO
2. HERANÇA -> é um conceito de POO que permite que uma classe herde atributos e métodos de outra, evitndo a repetição de código.
3. POLIMORFISMO
4. ABSTRAÇÃO

## PALAVRAS RESERVADAS EM POO
1. class -> é uma palavra-chave em python onde você cria um `molde`. Toda classe pode ter atributos e métodos, 
sendo que os atributos precisam estar dentro de um método chamado construtor (__init__).
2. object -> é o nome dado a cada `cópia` criada da classe. Também conhecido como instância.
3. __init__ -> é um inicializador(construtor) onde você informa que toda cópia precisa passar aquees valores no momento da criação. 
É um método especial.
4. self -> referencia o atributo atual da classe(valor).


## TERMOS UTILIZADOS EM POO
1. método -> é uma função que está dentro de uma classe. É uma ação.
2. atributo -> são as características de uma classe.

## HERANÇA
Teremos dois tipos de classes:
- superClass -> é a classe pai, é a que oferece a herança.
- subclass -> é a classe filha, que herda a herança.




## Atalhos no VScode
``CTRL + B`` => Oculta ou exibe o explorador.
``CTRL + ;`` => Comenta ou descomenta um código.
``CTRL + C`` => Copiar.
``CTRL + V`` => Colar.
``CTRL + Z`` => Desfaz última operação realizada.
``Shift + Alt + seta`` => Duplica linha.
``CTRL + B`` => Oculta ou exibe o terminal.
``CTRL + D`` => Seleciona a próxima ocorrência da palavra.
``Alt + Z`` => Realiza uma quebra de linha.

## Atalhos do Windows
``Windows + ç`` => Oculta ou exibe o explorador.