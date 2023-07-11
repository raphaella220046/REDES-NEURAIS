# <span style="font-family: Garamond;"> <font color=#993399> __Redes Neurais e Algoritmos Genéticos__ </span>
<hr>
    
## Conteúdo :card_index_dividers:

<hr>

Este repositório apresenta os experimentos realizados durante a disciplina de Redes Neurais e Algoritmos Genéticos orientada pelo Prof. Dr. Daniel Roberto Cassar durante o 3º semestre do curso de Ciência, Tecnologia e Inovação da Ilum Escola de Ciência.

Aqui você encontra os arquivos organizados em duas pastas: [`AlgoritmosGeneticos`](https://github.com/raphaella220046/REDES-NEURAIS/tree/main/AlgoritmosGeneticos) e [`RedesNeurais`](https://github.com/raphaella220046/REDES-NEURAIS/tree/main/RedesNeurais).
    
## Algoritmos Genéticos :dna:
    
<hr>

Um algoritmo genético é uma técnica de busca e otimização inspirada na teoria da evolução e na genética. É usado para resolver problemas de otimização e busca em espaços de solução grandes ou complexos. Os GAs imitam o processo de seleção natural e evolução das espécies para encontrar soluções ótimas ou quase ótimas.

As etapas do funcionamento de um algoritmo genético podem ser descritas basicamente por:

1. Codificação do problema: Primeiramente, é necessário definir uma representação para as possíveis soluções do problema a ser resolvido. Esta representação pode ser uma cadeia de bits, uma lista de números, uma estrutura de dados, etc. Essa representação é chamada de "gene".
    
2. Definição do indivíduo: Cada "indivíduo" é determinado aleatoriamente por uma sequência de genes.

3. Inicialização da população: Uma população inicial de possíveis "indivíduos" é gerada aleatoriamente. Cada indivíduo na população inicial representa uma possível solução para o problema.

4. Avaliação da aptidão (fitness): A qualidade de cada indivíduo da população é avaliada por meio de uma função objetivo ou métrica (fitness function). Essa função atribui um valor numérico a cada indivíduo com base em sua qualidade ou desempenho na resolução do problema.

5. Seleção: Os indivíduos mais aptos da população são selecionados para reproduzir e gerar descendentes. Indivíduos com maior aptidão são mais propensos a serem selecionados, mas a seleção de indivíduos menos aptos também é permitida para manter a diversidade genética.

6. Operadores Genéticos: Operadores genéticos são aplicados a indivíduos selecionados para criar descendentes. Os operadores genéticos comuns são cruzamento e mutação. O cruzamento mistura o material genético de dois ou mais indivíduos para criar novos indivíduos. A mutação introduz mudanças aleatórias no material genético de um indivíduo.

7. Substituição: Os novos indivíduos criados pelos operadores genéticos substituem uma parte da população original. Esse processo é repetido até que um critério de término seja alcançado, como um número máximo de gerações ou uma solução bem-sucedida.

8. Convergência: À medida que as gerações progridem, espera-se que a população converja para soluções mais ótimas. Os indivíduos mais aptos têm maior probabilidade de serem selecionados e se reproduzirem, transmitindo suas características às gerações subsequentes.

9. Término: O algoritmo genético termina quando os critérios de término estabelecidos são atingidos. Pode ser uma solução satisfatória para o problema, um número máximo de gerações ou algum outro critério definido.

Algoritmos genéticos são especialmente úteis ao enfrentar problemas complexos de otimização com múltiplas variáveis e restrições. Eles podem encontrar soluções aproximadas em um tempo razoável, embora não haja garantia de encontrar a solução ótima global em todos os casos. A eficácia de um algoritmo genético depende da qualidade da função objetivo, da seleção de operadores genéticos adequados e da configuração dos parâmetros do algoritmo.

    
## Redes Neurais :brain:
    
<hr>
    
![MIT-Neural-Networks-SL.gif](https://github.com/raphaella220046/REDES-NEURAIS/blob/main/Imagens/MIT-Neural-Networks-SL.gif)
    
As redes neurais são modelos computacionais inspirados na estrutura e funcionamento do cérebro humano. Essas redes são usadas para processamento de informações e aprendizado de máquina em uma ampla variedade de aplicações.

Uma rede neural é composta por unidades de processamento chamadas neurônios artificiais ou nós, que são organizados em camadas. As informações fluem por essas camadas de nós, onde cada nó realiza operações matemáticas simples e envia seu resultado para os nós da próxima camada. A estrutura em camadas e as conexões entre os nós permitem que a rede neural modele relacionamentos complexos e execute tarefas de processamento de informações.

Os componentes fundamentais de uma rede neural podem ser descritos como:

1. Neurônios artificiais:
    - Cada neurônio artificial recebe uma ou várias entradas e produz uma saída através de uma função de ativação.
    - A função de ativação pode ser linear ou não linear e é utilizada para introduzir não linearidades e maior capacidade de representação na rede.
    - Neurônios artificiais são conectados uns aos outros por conexões ponderadas.

2. Camadas:
    - Os neurônios são organizados em camadas dentro da rede neural.
    - Uma rede neural típica consiste em uma camada de entrada, uma ou mais camadas ocultas e uma camada de saída.
    - A camada de entrada recebe os dados de entrada, enquanto a camada de saída produz os resultados finais ou previsões da rede.
    - As camadas ocultas são responsáveis por processarem as informações intermediárias e extraírem características relevantes.

3. Conexões ponderadas:
    - Cada conexão entre dois neurônios é associada a um peso ou valor numérico.
    - Os pesos determinam a influência relativa das entradas na saída do neurônio.
    - Durante o treinamento da rede neural, os pesos são ajustados para melhorar o desempenho da rede em uma tarefa específica.

4. Funções de ativação:
    - Cada neurônio aplica uma função de ativação à sua entrada para produzir a saída.
    - Algumas funções de ativação comuns incluem a função sigmoide, a função ReLU (Unidade Linear Retificada) e a função softmax.
    - A função de ativação introduz não linearidades na rede, permitindo aprender relações não lineares nos dados.

5. Propagação direta:
    - Durante a propagação direta, os dados de entrada são passados pela rede neural, camada por camada, até atingir a camada de saída.
    - Em cada camada, as entradas são combinadas ponderadamente com os pesos e a função de ativação correspondente é aplicada.

6. Aprendizagem e treinamento:
    - O processo de treinamento de uma rede neural envolve ajustar os pesos das conexões para que a rede aprenda com os dados e melhore seu desempenho em uma tarefa específica.
    - O algoritmo de treinamento mais comum é o backpropagation, que aplica o gradiente local de maneira descendente para ajustar os pesos e minimizar uma função de perda.

7. Propagação do erro:
    - Durante o treinamento, é calculado o erro entre as saídas produzidas pela rede e os valores desejados.
    - O erro é propagado para trás pela rede, calculando as contribuições de cada conexão para o erro total.
    - Usando o gradiente descendente, os pesos são ajustados na direção que reduz o erro.

8. Generalização e previsão:
    - Uma vez treinada a rede neural, ela pode generalizar e fazer previsões sobre novos dados.
    - A rede aplica operações de propagação direta usando os pesos ajustados durante o treinamento para produzir resultados.

As redes neurais são modelos poderosos e flexíveis usados em uma ampla gama de aplicações, como reconhecimento de imagem, processamento de linguagem natural, previsão de séries temporais, jogos e muitas outras áreas de pesquisa e desenvolvimento científico e tecnológico.