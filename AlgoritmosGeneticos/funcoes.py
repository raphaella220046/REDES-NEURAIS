import random

def gene_cb():
    '''Gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor 0 ou 1'''
    
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def individuo_cb(n):
    ''' Gera um indivíduo para o problema das caixas binárias.
    
    Args:
        n = número de genes do indivíduo
        
    Return:
        Uma lista com n genes. Cada gene é um valor 0 ou 1.'''
    
    individuo = []
    
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo

def populacao_cb(tamanho, n):
    '''Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho = tamanho da população
        n = número de indivíduos
        
    Return:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.'''
    
    populacao = []
    
    for _ in range(tamanho): # o uso do _ é para uma variável que não será usada no algoritmo
        populacao.append(individuo_cb(n))
    return populacao
    
def selecao_roleta_max(populacao, fitness):
    '''Seleciona individuos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Arg:
        população = lista com todos os indivíduos da população
        fitness = valor da função objetivo dos indivíduos da população
        
    Return:
        População dos indivíduos selecionados.'''
    
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def cruzamento_ponto_simples(pai, mae):
    '''Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando um indivíduo
        mãe: uma lista representando um indivíduo
    
    Return:
        Duas listas sendo que cada uma representa um filho dos pais que foram os argumentos.'''
    
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def mutacao_cb(individuo):
    '''Realiza a mutação de um gene no problema das caixas binárias.
    
    Args:
        individuo: uma lista representando um individuo no problema das caixas binárias.
    
    Return:
        Um individuo com um gene mutado.'''
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo
    

def funcao_objetivo_cb(individuo):
    '''Computa a função objetivo no problema das caixas binárias.
    
    Args:
        individuo = lista contendo os genes das caixas binárias
        
    Return:
        Um valor representando a soma dos genes do indivíduo.'''
    
    return sum(individuo) + 1 # Para evitar dar erro no fit em uma seleção de indivíduos com apenas genes 0

def funcao_objetivo_pop_cd(populacao):
    '''Calcula a função objetivo para todos os membros de uma população.
    
    Args:
        populacao = lista com todos os indivíduos da população
    
    Return:
        Lista dos valores representando a fitness de cada indivíduo da população.'''
        
    fitness = []
    
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness