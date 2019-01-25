# -*- coding: utf-8 -*-

import csv
import math
import numpy as np
from  decimal import Decimal
import random 
from random import randrange
from random import seed
from random import shuffle
import operator


def loadData(file):
    # """file é o arquivo e prop a proporção de divisao"""
    # test_file = []
    # training_file = []
    arquivo_conteudo = []
    
    with open(file, 'rb') as f:
        data = list(csv.reader(f)) 
        for linha in range(len(data)):
            arquivo = data[linha]
            arquivo_conteudo = arquivo[:-1]
            arquivo_conteudo = map(int, arquivo_conteudo)
            mini = min(arquivo_conteudo)
            maxi = max(arquivo_conteudo)
            """pra cada linha no arquivo transforma a posição 
               atual pela normalização vai ate -1 pq o ultimo é o label"""
            for p in range(len(arquivo_conteudo)):
                """substitui no arquivo"""
                valor = arquivo_conteudo[p]
                arquivo_conteudo[p] = (valor - mini)/float(maxi-mini)
                """separa randomicamente os dados usando a proporção passada"""
            arquivo_conteudo.append(arquivo[-1])
    #         if random.random() < prop:
    #             training_file.append(arquivo_conteudo)
    #         else:
    #             test_file.append(arquivo_conteudo)
    # """retorna as duas listas de treino e teste"""     
    return arquivo_conteudo #training_file, test_file
            

def euclideanDistance(instance1, instance2):
    """essa função recebe duas instancias para fazer o calculo da distancia
       onde a primeira instancia é comparada com todas as instancias da lista de treino"""
    distance = 0
    """não pega a ultima posicao pq é o nome do treco"""
    for element in range(len(instance2)-1):
        """vai calculando a distancia e adicionando na variavel distancia"""
        distance += pow((float(instance1[element]) - float(instance2[element])), 2)
    """retorna a raiz quadrada da distancia"""
    return math.sqrt(distance)      


def manhattanDistance(instance1, instance2):
    distance = 0
    for element in range(len(instance2)-1):
        distance += (float(instance1[element]) - float(instance2[element]))
    return distance


def hamDistance(instance1, instance2):
    distance = 0
    for element in range(len(instance2)-1):
        if instance1[element] != instance2[element]:
            distance += 1
    return distance 


def cossenoDistance(instance1, instance2):
    xx, xy, yy = 0, 0, 0

    for element in range(len(instance2)-1):
        x = instance1[element]; y = instance2[element]
        xx += x*x
        yy += y*y
        xy += x*y
    return xy/math.sqrt(xx*yy)


def nth_root(value, n_root):
 
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)
 

def minkowski_distance(instance1, instance2, p_value):
    distance = 0
    distance += nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(instance1, instance2)),p_value)
    return distance

def train_test_split(dataset, prop):
    train = list()
    train_size = prop * len(dataset)
    teste = list(dataset)
    while len(train) < train_size:
	    index = randrange(len(teste))
	    train.append(teste.pop(index))
    return train, teste

def cross_validation(dataset, folds):

    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / folds)
    for i in range(folds):
	    fold = list()
	    while len(fold) < fold_size:
		    index = randrange(len(dataset_copy))
		    fold.append(dataset_copy.pop(index))
	    dataset_split.append(fold)
    return dataset_split
    # """file é o arquivo e prop a proporção de divisao"""
    # test_file = []
    # training_file = []
    
    # with open(file, 'rb') as f:
    #     data = list(csv.reader(f)) 
    #     for linha in range(len(data)):
    #         arquivo = data[linha]
    #         arquivo_conteudo = arquivo[:-1]
    #         arquivo_conteudo = map(int, arquivo_conteudo)
    #         mini = min(arquivo_conteudo)
    #         maxi = max(arquivo_conteudo)
    #         """pra cada linha no arquivo transforma a posição 
    #            atual pela normalização vai ate -1 pq o ultimo é o label"""
    #         for p in range(len(arquivo_conteudo)):
    #             """substitui no arquivo"""
    #             valor = arquivo_conteudo[p]
    #             arquivo_conteudo[p] = (valor - mini)/float(maxi-mini)
    #             """separa randomicamente os dados usando a proporção passada"""
    #         arquivo_conteudo.append(arquivo[-1])  
    #         if randomize:
    #             f = arquivo_conteudo
    #             shuffle(f)
    #         slices = [f[i::folds] for i in xrange(folds)] 
    #         for i in xrange(folds): 
    #             test_file = slices[i]
    #             training_file = [f
    #                 for s in slices if s is not test_file
    #                 for f in s]
    #         return training_file, test_file
            

def confusion_matrix(actual, predicted):
	unique = set(actual)
	matrix = [list() for x in range(len(unique))]
	for i in range(len(unique)):
		matrix[i] = [0 for x in range(len(unique))]
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for i in range(len(actual)):
		x = lookup[actual[i]]
		y = lookup[predicted[i]]
		matrix[y][x] += 1
	return unique, matrix


def print_confusion_matrix(unique, matrix):
    #A é o valor atual, P o valor da predição

	print('******MATRIZ DE CONFUSÃO******\n\n(A)' + ' '.join(str(x) for x in unique))
	print('(P)---------------------')
	for i, x in enumerate(unique):
		print("%s | %s" % (x, ' '.join(str(x) for x in matrix[i])))
        print('\n*********FIM DA MATRIZ*********')


def getNeighbors(training_file, test_instance, k, dist):
    """essa função encontra os vizinhos mais proximos da instancia de teste"""
    distances = []
    """percorre as linhas do arquivo de treino"""
    for linha in range(len(training_file)):
        """calcula a distancia da instancia de treino em relação ao conjunto de teste"""
        distance = dist(test_instance, training_file[linha])
        """armazena numa tupla contendo a instancia de teste e a distancia da instancia de treino"""
        distances.append((training_file[linha], distance))
    """as mais proximas ficam nos primeiros lugares"""    
    distances.sort(key=operator.itemgetter(1))
    
    neighbor = []
    """armazena em vizinho"""
    for x in range(k):
        neighbor.append(distances[x][0])
    """retorna uma lista com as instancias que estao mais proximas"""
    return neighbor


def getResponse(neighbor):
    """pega a lista de listas retornada pela função de cima"""
    votes = {}
    """percorre todas as linhas da lista e pega o ultimo elemento de cada lista"""
    for linha in range(len(neighbor)):
        answer = neighbor[linha][-1]
        if answer in votes:
            votes[answer] += 1
        else:
            votes[answer] = 1
    """"dicionario onde key é o nome e value é o contador de ocorrencia da key
        organizando o dicionario temos a key com mais votes"""
    organized_votes = sorted(votes.iteritems(), key=operator.itemgetter(1), reverse=True)

    return organized_votes[0][0]


def getAccuracy(test_file, predict):
    """compara o arquivo de teste com as predicao e retorna a % de acerto"""
    correct = 0

    for linha in range(len(test_file)):
        if(test_file[linha][-1]) in predict[linha]:
            correct += 1
    return (correct/float(len(test_file)))*100.0


def f1_score_single(atual, predicao):
    atual = set(atual)
    predicao = set(predicao)
    cross_size = len(atual & predicao)
    if cross_size == 0: return 0.
    p = 1. * cross_size / len(predicao)
    r = 1. * cross_size / len(atual)
    return 2 * p * r / (p + r)
    

def f1_score(atual, predicao):
    return np.mean([f1_score_single(x, y) for x, y in zip(atual, predicao)])


 

##################################################### MAIN ###########################################
def main():

    proporcao = 0.66
 
    treino, teste =  loadData("DATA_BASE.csv", proporcao)

    print("Conjunto de treio: " + repr(len(treino)))
    print("Conjunto de teste: " + repr(len(teste))+"\n")

    predicoes = []
    a = []
    k = 3

    for linha in range(len(teste)):
        vizinhos = getNeighbors(treino, teste[linha], k, euclideanDistance)
        resultado = getResponse(vizinhos)
        predicoes.append(resultado)
        atual = teste[linha][-1]
        a.append(atual)
        print("PREDICAO:"+repr(resultado) + ' ATUAL:'+repr(teste[linha][-1]))
        
    precisao = getAccuracy(teste, predicoes)
    print("\nPRECISAO: " + repr(precisao) + '%\n\n')
    measure = f1_score(a, predicoes)
    print("\nF-MEASURE: " + repr(measure) + '%\n\n')
    unique, matrix = confusion_matrix(a, predicoes)
    print_confusion_matrix(unique, matrix)

def main_validation():
   
    seed(1)
    data = "DATA_BASE.csv"
    dados = loadData(data)
    proporcao = 0.66
    cruzado = cross_validation(dados, 10)
    treino, teste = train_test_split(cruzado, proporcao)

    print("Conjunto de treino: " + repr(len(treino)))
    print("Conjunto de teste: " + repr(len(teste))+"\n")

    predicoes = []
    a = []
    k = 3

    for linha in range(len(teste)):
        vizinhos = getNeighbors(treino, teste[linha], k, manhattanDistance)
        resultado = getResponse(vizinhos)
        predicoes.append(resultado)
        print("PREDICAO:"+repr(resultado) + ' ATUAL:'+repr(teste[linha][-1]))
    precisao = getAccuracy(teste, predicoes)
    print("PRECISAO: " + repr(precisao  ) + '%')
    print("\nPRECISAO: " + repr(precisao) + '%\n\n')
    measure = f1_score(a, predicoes)
    print("\nF-MEASURE: " + repr(measure) + '%\n\n')
    unique, matrix = confusion_matrix(a, predicoes)
    print_confusion_matrix(unique, matrix)

    


########################################## CHAMADA DO MAIN ############################################

main_validation()
#main()