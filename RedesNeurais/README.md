# Experimentos de redes neurais artificiais

#### Este repositório apresenta todos os experimentos realizados na disciplina de Redes Neurais e Algoritmos Genéticos orientada pelo Prof. Dr. Daniel Roberto Cassar, do curso de bacharelado em Ciência, Tecnologia e Inovação da Ilum - Escola de Ciência.

#### Aqui você encontrará uma breve descrição de cada experimento que foi realizado, utilizando classes, instâncias e métodos desenvolvidos para solucionar problemas.

As redes neurais artificiais constituem uma estrutura de processamento capaz de armazenar conhecimento baseado em aprendizagem (experiência) e disponibilizar este conhecimento para a aplicação em diversas áreas. Seu processo se baseia no cérebro humano com as conexões entre os neurônios. Para entender de forma prática, é um processo análogo ao de engrenagens que fazem um relógio funcionar. Interpretando desta forma, os experimentos aqui desenvolvidos consistem em abrir esse relógio e trabalhar com cada engrenagem do sistema.

![engrenagem.png](https://github.com/raphaella220046/REDES-NEURAIS/blob/327d741d4cb8f1161a78d1e86b7deb37ff3f1fe5/Imagens/engrenagem.png)

#### Observações importantes:

- O arquivo funcoes.py contém todas as funções criadas durante o desenvolvimento dos algoritmos.

### Experimentos:


**O experimento R.01 - derivadas**

Apresenta uma breve demonstração de como calcular a derivada de uma função e representá-la em um gráfico.

**O experimento R.02 - classes**

Apresenta uma breve introdução a estruturação de classes e métodos denominados dunders que executam ações específicas dentro da classe criada. Também demonstra como alterar o estado de um objeto dentro e fora da classe.

**O experimento R.03 - construindo um grafo automaticamente**

Apresenta a construção automática de grafos, por meio de classes, criando propriedades para armazenar os valores dos dados, operadores que executarão ações sobre esses dados e rótulos para a identificação de cada elemento no grafo.

**O experimento R.04 - computando gradientes locais**

Apresenta a primeira aplicação do gradiente local em cada vértice da rede neural por backpropagation. Fazendo uma otimização para que a propagação ocorra de maneira automática, sabendo que a rede não é cíclica, ou seja, tem início em vértices raízes e fim em um vértice folha. Desta forma, a propagação é realizada aplicando o algoritmo autograd, tornando conhecido o gradiente local de cada vértice em que se propagar, por meio de uma ordenação topológica.

**O experimento R.05 - finalizando a classe Valor**

Este experimento apresenta a classe `Valor` com as operações matemáticas de adição, subtração, multiplicação, divisão, exponenciação, as funções exponencial e sigmoidal, com o objetivo de entender o funcionamento de uma classe.

**O experimento R.06 - redes neurais artificiais**

A classe Valor desenvolvida no experimento anterior é aplicada nesse experimento, a fim de construir uma rede neural. A rede neural foi construída criando um neurônio artificial, em seguida uma camada de neurônios e, por último multiplas camadas que integram a rede neural.

**O experimento R.07 - treinando uma rede neural**

O objetivo desse experimento é minimizar a função de perda, utilizando pesos e vises para manipular o valor de saída da rede neural. Esta não é uma rede neural eficiente e foi aplicada apenas para demonstração de seu funcionamento, entendo o processo de calcular o erro quadrático, propagar para toda a rede, e atualizar os parâmetros, conforme a taxa de aprendizado aplicada a cada época.

**O experimento R.08 - treinando uma rede neural com pytorch**

Nesse experimento uma rede neural de maior complexidade é treinada pelo Pytorch, uma biblioteca Python de aprendizado de máquina desenvolvida para implementação de aprendizado profundo. Foram aplicados métodos para normalização dos dados, conversão para float32, a função retificadora entre outros. Os dados foram separados em etapas de treino e teste.