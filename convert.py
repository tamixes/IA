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

arquivo = glob.glob("/home/tamires/ia/IA/bd2/*.png")
i = 0
for a in arquivo:
   cria_vetor(a, 'teste_'+ str(i) +'.csv')
   i+=1



# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_0_bot_seg_1_cropped.png', '5_0.1.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_0_bot_seg_2_cropped.png', '5_0_2.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_0_bot_seg_3_cropped.png', '5_0_3.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_0_bot_seg_4_cropped.png', '5_0_4.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_0_bot_seg_5_cropped.png', '5_0_5.csv')

# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_1_bot_seg_1_cropped.png', '5_1_0.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_1_bot_seg_2_cropped.png', '5_1_2.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_1_bot_seg_3_cropped.png', '5_1_3.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_1_bot_seg_4_cropped.png', '5_1_4.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_1_bot_seg_5_cropped.png', '5_1_5.csv')

# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_2_bot_seg_1_cropped.png', '5_2_1.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_2_bot_seg_2_cropped.png', '5_2_2.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_2_bot_seg_3_cropped.png', '5_2_3.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_2_bot_seg_4_cropped.png', '5_2_4.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_2_bot_seg_5_cropped.png', '5_2_5.csv')


# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_3_bot_seg_1_cropped.png', '5_3_1.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_3_bot_seg_2_cropped.png', '5_3_2.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_3_bot_seg_3_cropped.png', '5_3_3.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_3_bot_seg_4_cropped.png', '5_3_4.csv')
# cria_vetor('/home/tamires/IA/Projeto-ASL/Images/teste1/hand5_3_bot_seg_5_cropped.png', '5_3_5.csv')
