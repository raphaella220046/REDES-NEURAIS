# Experimentos de otimização e algoritmos genéticos

Coloque seus experimentos de algoritmos genéticos nesta pasta.

Esceva um README aqui para guiar o leitor sobre seus experimentos realizados.

#### Este repositório apresenta todos os experimentos realizados na disciplina de Redes Neurais e Algoritmos Genéticos do curso de Ciência, Tecnologia e Inovação da Ilum - Escola de Ciência.

#### Aqui você encontrará uma breve descrição de cada experimento que foi realizado, utilizando funções e métodos nativos do Python para solucionar problemas de otimização.

#### Observações importantes:

- O arquivo funcoes.py contém todas as funções criadas durante o desenvolvimento dos algoritmos.
- Foram definidos como gene cada elemento dentro de uma lista, indivíduo que é um agrupamento de genes, ou seja, uma lista, e população que é um conjunto de listas.
- A solução dos problemas têm por base três etapas: seleção, cujos indivíduos são selecionados aleatoriamente para compor uma população, cruzamento entre esses indivíduos que ocorre utilizando estratégias específicas para cada situação, e mutação que é a troca genes a cada dois indivíduos na população e que também ocorre considerando as particularidades de cada experimento.

### Experimentos:


**O Experimento A.01 - busca aleatoria**

Consiste em um problema de maximização, cujo fit é o valor máximo de caixas. Foi realizado com o intuito de solucionar o problema de otimização com caixas binárias. A solução apresentada é probabilística e o resultado obtido varia em cada execução do algoritmo, podendo ou não ser encontrada a função objetivo.

**O Experimento A.02 - busca em grade**

Ao contrário do experimento anterior, foi realizado com o intuito de testar todas as possibilidades de um conjunto binário. A solução apresentada é determinística e o resultado obtido é constante em todas as vezes que o algoritmo é executado. Desta maneira, a função objetivo sempre estará entre as combinações apresentadas.

**O Experimento A.03 - algoritmo genetico**

É um algoritmo probabilístico e cria uma população aleatória para, em seguida, gerar um cruzamento aleatório entre os indivíduos, por meio da combinação de genes dos pais e das mães. Por último, é utilizada uma função para fazer uma mutação aleatória nos genes desse indivíduo.

**O Experimento A.04 - caixas nao-binarias**

É um algoritmo que gera uma população de indivíduos, cujos genes não são binários, mas compreende um intervalo de 0 a 100 (incluso). Sendo assim, as funções utilizadas no experimento anterior foram alteradas considerando a variável de valor máximo em cada caixa.Foi constatado que dada a alta probabilidade de variabilidade genética entre os indivíduos em cruzamento, além das mutações ocorrerem ao acaso, é bastante improvável que o algoritmo apresente o fitness esperado.

**experimento A.05 - descobrindo a senha**

Este é um algoritmo para resolver um problema de minimização que consiste em descobrir a senha determinada pela distância que as senhas estimadas estão em relação à essa senha determinada, elegendo a senha com melhor fit. Ele funciona a partir de uma lista com a senha de caracteres diversos criada, cada caracter é convertido para um número. Em seguida, são geradas senhas aleatórias com a mesma quantidade de caracteres da senha criada. É aplicada a seleção por torneio, onde as senhas combatem entre si e o melhor fit é definido ao comparar as distâncias entre a senha criada e as melhores senhas geradas. Todo o processo tem convergência para a diferença zero, quando a senha é encontrada.

**experimento A.06 - o caixeiro viajante**

Este algoritmo é aplicado ao problema de identificar a menor distância que um caixeiro viajante pode percorrer e retornar para a cidade de partida, dada uma determinada quantidade de cidades. Buscando alcançar esse objetivo, foi definido aleatoriamente cada indivíduo com a condição de que cada um tenha uma sequência de cidades não repetidas. Em seguida, foi gerada uma população com esses indivíduos. Então, foi aplicado o fitness para obter indivíduos com a menor distância percorrida, comparando dentro dessa população. Logo após, foi executado o cruzamento ordenado entre os indivíduos, evitando ter sequências com repetição. Adiante, ocorreu a mutação por troca para produzir os melhores indivíduos gerados no cruzamento, mantendo as sequências com cidades unitárias. Por fim, foi aplicado novamente o fitness para obter o indivíduo que contém cidades cujo ordenamento apresenta a menor distância.