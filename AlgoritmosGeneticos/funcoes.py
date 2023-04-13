import random

def gene_cb():
    
    '''Gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor 0 ou 1
    '''
    
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


def gene_cnb(valor_max_caixa):
    
    '''Gera um gene válido para o problema das caixas não -binárias
    
    Args:
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        Um valor de 0 a 'valor_max_caixa' (incluso)
    '''
    
    gene = random.randint (0, valor_max_caixa)
    return gene


def gene_caracter(caracteres):
    
    '''Sorteia um caracter
    
    Args:
        caracteres: caracteres possíveis de serem sorteados
        
    Returns:
        Retorna um caracter dentro dos possíveis de serem sorteados
    '''
    
    caracter = random.choice(caracteres)
    return caracter


def individuo_cb(n):
    
    ''' Gera um indivíduo para o problema das caixas binárias.
    
    Args:
        n = número de genes do indivíduo
        
    Return:
        Uma lista com n genes. Cada gene é um valor 0 ou 1.
    '''
    
    individuo = []
    
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def individuo_cnb(numero_genes, valor_max_caixa):
    
    '''Gera um indivíduo válido para o problema das caixas não binárias
    
    Args:
        numero_genes: número de genes na lista que representa o indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
    
    Returns:
        Uma lista que representa um indivíduo válido para o problema das CNB
    '''
    
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


def individuo_senha(tamanho_senha, caracteres):
    
    '''Cria um candidato para o problema da senha
    
    Args:
        tamanho_senha: número inteiro representando o tamanho da senha
        caracteres: caracteres possíveis a serem sorteados
        
    Returns:
        Lista com n letras
    '''
    
    candidato = []
    
    for n in range(tamanho_senha):
        candidato.append(gene_caracter(caracteres))
    
    return candidato


def populacao_cb(tamanho, n):
    
    '''Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho = tamanho da população
        n = número de indivíduos
        
    Return:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
    '''
    
    populacao = []
    
    for _ in range(tamanho): # o uso do _ é para uma variável que não será usada no algoritmo
        populacao.append(individuo_cb(n))
    return populacao


def individuo_cv(cidades):
    
    '''Sorteia um caminho possível no problema do caixeiro viajante.
    
    Args:
        cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Return:
        Retorna uma lista de nomes de cidades formando um caminho onde visitamos cada cidade
        apenas uma vez.
    '''

    nomes = list(cidades.keys())
    random.shuffle(nomes) # método usado para reorganizar a ordem de elementos na sequência da lista
    return nomes


def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    
    '''Cria uma população de indivíduos para o problema das caixas não-binárias
    
    Args:
        tamanho_populacao: número de indivíduos da população
        numero_genes: número de genes do indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        uma lista onde cada item representa um indivíduo
    '''
    
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, caracteres):
    
    '''Cria população inicial no problema da senha
    
    Args:
        tamanho: tamanho da população
        tamanho_senha: número inteiro que representa o tamanho da senha
        caracteres: caracteres possíveis de serem sorteados
        
    Returns:
        Lista com todos os indivíduos da população no problema da senha
    '''
    
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, caracteres))
    return populacao


def populacao_inicial_cv(tamanho, cidades):
    
    '''Cria população inicial no problema do caixeiro viajante.
    
    Args:
        tamanho: Tamanho da população.
        cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Returns:
        Lista com todos os indivíduos da população no problema do caixeiro viajante.
    '''
    
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def funcao_objetivo_cb(individuo):
    
    '''Computa a função objetivo no problema das caixas binárias.
    
    Args:
        individuo = lista contendo os genes das caixas binárias
        
    Return:
        Um valor representando a soma dos genes do indivíduo.
    '''
    
    return sum(individuo) + 1 # Para evitar dar erro no fit em uma seleção de indivíduos com apenas genes 0


def funcao_objetivo_pop_cb(populacao):
    
    '''Calcula a função objetivo para todos os membros de uma população.
    
    Args:
        populacao = lista com todos os indivíduos da população
    
    Return:
        Lista dos valores representando a fitness de cada indivíduo da população.
    '''
        
    fitness = []
    
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_cnb(individuo):
    
    '''Calcula o fitness do indivíduo para o problema das caixas não-binárias
    
    Args:
        individuo: lista que representa um indivíduo dentro do problema das CNB
        
    Returns:
        Um valor que representa o fitness do indivíduo
    '''
    
    fitness = sum(individuo)
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    
    '''Calcula o fitness da população completa
    
    Args:
        populacao: lista com todos os indivíduos da população
        
    Returns:
        Uma lista com o fitness de cada indivíduo em ordem
    '''
    
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop


def funcao_objetivo_senha(individuo, senha_verdadeira):
    
    '''Computa a função objetivo de um indivíduo no problema da senha
    
    Args:
      individuo: lista contendo os caracteres da senha
      senha_verdadeira: a senha que o algoritmo está tentando descobrir
      
    Returns:
      A diferença entre a senha proposta e a senha verdadeira (essa diferença é medida caracter por
      caracter, quanto mais distante um caracter estiver do caracter verdadeiro, maior é essa
      diferença.
    '''
    diferenca = 0

# A função ord transforma cada caracter do computador em um numérico que é específico para cada um
    for caracter_candidato, caracter_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(caracter_candidato) - ord(caracter_oficial))

    return diferenca


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    
    '''Computa a função objetivo de uma população no problema da senha
    
    Args:
        populacao: lista com todos os indivíduos da população
        senha_verdadeira: a senha que você está tentando descobrir
        
    Returns:
        Lista contendo os valores da métrica de distância entre as senhas
    '''
    
    resultado = []
    
    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))
        
    return resultado


def funcao_objetivo_cv(individuo, cidades):
    
    '''Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    
    Args:
        individuo: Lista contendo a ordem das cidades que serão visitadas
        cidades: Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
        
    Returns:
        A distância percorrida pelo caixeiro seguindo o caminho contido no indivíduo.
        Lembrando que após percorrer todas as cidades em ordem, o caixeiro retorna para a cidade
        original de onde começou sua viagem.
    '''

    distancia = 0
    
    for posicao in range(len(individuo) - 1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    # Calculando o caminho de volta para a cidade inicial
    
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso

    return distancia


def funcao_objetivo_pop_cv(populacao, cidades):
    
    '''Computa a função objetivo de uma população no problema do caixeiro viajante.
    
    Args:
        populacao: uma lista com todos os indivíduos da população
        cidades: dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas
        das cidades
        
    Returns:
        Lista contendo a distância percorrida pelo caixeiro para todos os indivíduos da população
    '''

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado


def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    
    '''Computa a função objetivo de um candidato no problema da mochila.
    
    Args:
        individuo: uma lista binária contendo a informação de quais objetos serão selecionados
        objetos: dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor
        limite: número indicando o limite de peso que a mochila aguenta
        ordem_dos_nomes: uma lista contendo a ordem dos nomes dos objetos
        
    Returns:
        Valor total dos itens inseridos na mochila considerando a penalidade para quando o peso
        excede o limite
    '''
    
    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        valor_mochila = 0.01
        
    return valor_mochila

def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    
    '''Computa a função objetivo de uma população no problema da mochila
    
    Args:
        populacao: uma lista com todos os indivíduos da população
        objetos: dicionário onde as chaves são os nomes dos objetos e os valores são dicionários com
        a informação do peso e valor
        limite: número indicando o limite de peso que a mochila aguenta
        ordem_dos_nomes: uma lista contendo a ordem dos nomes dos objetos
        
    Returns:
        Lista contendo o valor dos itens da mochila de cada indivíduo.
    '''

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado


def mutacao_cb(individuo):
    
    '''Realiza a mutação de um gene no problema das caixas binárias.
    
    Args:
        individuo: uma lista representando um individuo no problema das caixas binárias.
    
    Return:
        Um individuo com um gene mutado.
    '''
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    
    '''Realiza a mutação do indivíduo
    
    Args:
        individuo: indivíduo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        Indivíduo que sofreu a mutação
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


def mutacao_senha(individuo, caracteres):
    
    '''Realiza a mutação de um gene no problema da senha
    
    Args:
        individuo: uma lista representando um indivíduo no problema da senha
        caracteres: caracteres possíveis de serem sorteados
        
    Return:
        Um indivíduo (senha) com o gene modificado
    '''
    
    gene = random.randint(0, len(individuo) -1)
    individuo[gene] = gene_caracter(caracteres)
    return individuo


def mutacao_de_troca(individuo):
    
    '''Troca o valor de dois genes.
    
    Args:
        individuo: uma lista representado um indivíduo.
        
    Return:
        O indivíduo recebido como argumento, porém com dois dos seus genes trocados de posição.
    '''
    pass
    
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo


def selecao_roleta_max(populacao, fitness):
    
    '''Seleciona individuos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Arg:
        população = lista com todos os indivíduos da população
        fitness = valor da função objetivo dos indivíduos da população
        
    Return:
        População dos indivíduos selecionados.
    '''
    
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    
    '''Faz a seleção de uma população usando torneio
    
    Nota: apenas funciona para problemas de minimização
    
    Args:
        populacao: população do problema
        fun_objetivo: função objetivo
        tamanho_torneio: quantidade de indivíduos que batalham entre si
    
    Returns:
        Lista com os indivíduos selecionados com o mesmo tamanho da população
    '''
    
    selecionados = []
    
    # Variável criada para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))
    
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)
        
        minimo_fitness = float('inf')
        
        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]
            
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit
        
        selecionados.append(selecionado)
        
    return selecionados


def cruzamento_ponto_simples(pai, mae):
    
    '''Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando um indivíduo
        mãe: uma lista representando um indivíduo
    
    Return:
        Duas listas sendo que cada uma representa um filho dos pais que foram os argumentos.
    '''
    
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def cruzamento_ordenado(pai, mae):
    
    '''Operador de cruzamento ordenado.
    Args:
        pai: uma lista representando um indivíduo
        mae : uma lista representando um indivíduo
        
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
        Estas listas mantém os genes originais dos pais, porém altera a ordem deles
    '''
    
    pass
    
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1)
    
    filho1 = pai [corte1:corte2]
    for gene in mae:
        if gene in mae:
            if gene not in filho1:
                filho1.append(gene)
    
    filho2 = mae [corte1:corte2]
    for gene in pai:
        if gene in mae:
            if gene not in filho2:
                filho2.append(gene)
                
    return filho1, filho2


def cria_cidades(n):
    
    '''Cria um dicionário aleatório de cidades com suas posições (x,y).
    
    Args:
        n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
        
    Returns:
        Dicionário contendo o nome das cidades como chaves e a coordenada no plano cartesiano das
        cidades como valores.
    '''

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


def distancia_entre_dois_pontos(a, b):
    
    '''Computa a distância Euclidiana entre dois pontos em R^2
    
    Args:
        a: lista contendo as coordenadas x e y de um ponto.
        b: lista contendo as coordenadas x e y de um ponto.
        
    Returns:
        Distância entre as coordenadas dos pontos a e b.
    '''

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist

def computa_mochila(individuo, objetos, ordem_dos_nomes):
    
    ''' Computa o valor total e peso total de uma mochila
    
    Args:
        individuo: uma lista contendo a informação de quais indivíduos serão selecionados
        objetos: dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor
        ordem_dos_nomes: lista contendo a ordem dos nomes dos objetos
        
    Returns:
        valor_total: valor total dos itens da mochila em unidades de dinheiros
        peso_total: peso total dos itens da mochila em unidades de massa
    '''
    
    valor_total = 0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]['valor']
            peso_do_item = objetos[nome_do_item]['peso']
            
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item
        
    return valor_total, peso_total
