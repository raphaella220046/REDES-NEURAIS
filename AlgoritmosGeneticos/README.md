# Experimentos de otimização e algoritmos genéticos

Coloque seus experimentos de algoritmos genéticos nesta pasta.

Esceva um README aqui para guiar o leitor sobre seus experimentos realizados.

#### Este repositório apresenta todos os experimentos realizados na disciplina de Redes Neurais e Algoritmos Genéticos do curso de Ciência, Tecnologia e Inovação da Ilum - Escola de Ciência.

#### Aqui você encontrará uma breve descrição de cada experimento que foi realizado, utilizando funções e métodos nativos do Python para solucionar problemas de otimização.

#### Observações importantes:
- O arquivo funcoes.py contém todas as funções criadas durante o desenvolvimento dos algoritmos.

### Experimentos:


**O Experimento A.01 - busca aleatoria** consiste em um problema de maximização, cujo fit é o valor máximo de caixas. Foi realizado com o intuito de solucionar o problema de otimização com caixas binárias. A solução apresentada é probabilística e o resultado obtido varia em cada execução do algoritmo, podendo ou não ser encontrada a função objetivo.

**O Experimento A.02 - busca em grade** Ao contrário do experimento anterior, foi realizado com o intuito de testar todas as possibilidades de um conjunto binário. A solução apresentada é determinística e o resultado obtido é constante em todas as vezes que o algoritmo é executado. Desta maneira, a função objetivo sempre estará entre as combinações apresentadas.

**O Experimento A.03 - algoritmo genetico** é um algoritmo probabilístico e cria uma população aleatória para, em seguida, gerar um cruzamento aleatório entre os indivíduos, por meio da combinação de genes dos pais e das mães. Por último, é utilizada uma função para fazer uma mutação aleatória nos genes desse indivíduo.

**O Experimento A.04 - caixas nao-binarias** é um algoritmo que gera uma população de indivíduos, cujos genes não são binários, mas compreende um intervalo de 0 a 100 (incluso). Sendo assim, as funções utilizadas no experimento anterior foram alteradas considerando a variável de valor máximo em cada caixa.Foi constatado que dada a alta probabilidade de variabilidade genética entre os indivíduos em cruzamento, além das mutações ocorrerem ao acaso, é bastante improvável que o algoritmo apresente o fitness esperado.