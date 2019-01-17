import cv2 
import numpy as np 
import csv
import glob

def salva_txt(array, nome):
    np.savetxt(nome, array, fmt='%s', delimiter=", ")        


def cria_vetor(file, nome):
    imagem = cv2.imread(file, 0)
    imagem_r = cv2.resize(imagem, (288, 1))
    array = np.array(imagem_r)
    salva_txt(array, nome)

arquivo = glob.glob("/home/tamires/ia/IA/bd2/hand_0/*.png")
i = 0
for a in arquivo:
   cria_vetor(a, '0_'+ str(i) +'.txt')
   i+=1
