# Experimentos de redes neurais artificiais

#### Este repositório apresenta todos os experimentos realizados na disciplina de Redes Neurais e Algoritmos Genéticos orientada pelo Prof. Dr. Daniel Roberto Cassar, do curso de bacharelado em Ciência, Tecnologia e Inovação da Ilum - Escola de Ciência.

#### Aqui você encontrará uma breve descrição de cada experimento que foi realizado, utilizando funções e métodos nativos do Python para solucionar problemas de otimização.

![engrenagem.png](https://github.com/raphaella220046/REDES-NEURAIS/blob/327d741d4cb8f1161a78d1e86b7deb37ff3f1fe5/Imagens/engrenagem.png)

As redes neurais artificiais têm um processo análogo ao de engrenagens que fazem um relógio funcionar. Os experimentos desenvolvidos consistem em abrir esse relógio e trabalhar cada engrenagem do sistema.

#### Observações importantes:

- O arquivo funcoes.py contém todas as funções criadas durante o desenvolvimento dos algoritmos.

### Experimentos:


**O Experimento R.01 - derivadas**

Apresenta uma breve demonstração de como calcular a derivada de uma função e representá-la em um gráfico.

**O Experimento R.02 - classes**

Apresenta uma breve introdução a estruturação de classes e métodos denominados dunders que executam ações específicas dentro da classe criada. Também demonstra como alterar o estado de um objeto dentro e fora da classe.

**O Experimento R.03 - construindo um grafo automaticamente**

Apresenta a construção automática de grafos, por meio de classes, criando propriedades para armazenar os valores dos dados, operadores que executarão ações sobre esses dados e rótulos para a identificação de cada elemento no grafo.

**O Experimento R.04 - computando gradientes locais**

Apresenta a primeira aplicação do gradiente local em cada vértice da rede neural por backpropagation. Fazendo uma otimização para que a propagação ocorra de maneira automática, sabendo que a rede não é cíclica, ou seja, tem início em vértices raízes e fim em um vértice folha. Desta forma, a propagação é realizada aplicando o algoritmo autograd, tornando conhecido o gradiente local de cada vértice em que se propagar, por meio de uma ordenação topológica.