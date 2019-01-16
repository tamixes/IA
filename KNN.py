import csv
import math
import random
import operator


def loadData(file, prop):
    """file eh o arquivo e prop a proporcao de divisao"""
    test_file = []
    training_file = []

    with open(file, 'rb') as f:
        data = list(csv.reader(f)) 
        for linha in range(len(data)):
            """pra cada linha no arquivo transforma o valor atual por um valor float
                vai ate -1 pq o ultimo eh a classe"""
            for valor in range(len(data[0])-1):
                """substitui no arquivo"""
                data[linha][valor] = float(data[linha][valor])
                """separa randomicamente os dados usando a proporcao passada"""
            if random.random() <= prop:
                training_file.append(data[linha])
            else:
                test_file.append(data[linha])
    """retorna as duas listas de treino e teste"""            
    return training_file, test_file
            

def euclideanDistance(instance1, instance2):
    """essa funcao recebe duas instancias para fazer o calculo da distancia
       onde a primeira instancia eh comparada com todas as instancias da lista de treino"""
    distance = 0
    """nao pega a ultima posicao pq eh o nome do treco"""
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

def getNeighbors(training_file, test_instance, k, dist):
    """essa funcao encontra os vizinhos mais proximos da instancia de teste"""
    distances = []
    """percorre as linhas do arquivo de treino"""
    for linha in range(len(training_file)):
        """calcula a distancia da instancia de treino em relacao ao conjunto de teste"""
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
    """pega a lista de listas retornada pela funcao de cima"""
    votes = {}
    """percorre todas as linhas da lista e pega o ultimo elemento de cada lista"""
    for linha in range(len(neighbor)):
        answer = neighbor[linha][-1]
        if answer in votes:
            votes[answer] += 1
        else:
            votes[answer] = 1
    """"dicionario onde key eh o nome e value eh o contador de ocorrencia da key
        organizando o dicionario temos a key com mais votes"""
    organized_votes = sorted(votes.iteritems(), key=operator.itemgetter(1), reverse=True)

    return organized_votes[0][0]


def getAccuracy(test_file, predict):
    """compara o arquivo de teste com as predicao e retorna a % de acerto"""
    corret = 0

    for linha in range(len(test_file)):
        if(test_file[linha][-1]) in predict[linha]:
            corret += 1
    return (corret/float(len(test_file)))*100.0

##################################################### MAIN ###########################################
def main():

    proporcao = 0.67

    treino, teste =  loadData("dados.csv", proporcao)

    print("Conjunto de treio: " + repr(len(treino)))
    print("Conjunto de teste: " + repr(len(teste)))

    predicoes = []
    k = 1

    for linha in range(len(teste)):
        vizinhos = getNeighbors(treino, teste[linha], k, hamDistance)
        resultado = getResponse(vizinhos)
        predicoes.append(resultado)
        print("PREDICAO:"+repr(resultado) + 'ATUAL:'+repr(teste[linha][-1]))
    precisao = getAccuracy(teste, predicoes)
    print("PRECISAO: " + repr(precisao  ) + '%')



########################################## CHAMADA DO MAIN ############################################
main()