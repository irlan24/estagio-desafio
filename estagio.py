

# ========================= TESTE DE CODIGOS ======================================

# def Matematica(strArr):
#     quantFrase = [strArr]

#     print(quantFrase)
#     for i in range(strArr):
#         quantFrase.append(input('Digite suas frases: '))        
#         newFrase = ';'.join(map(str, quantFrase[1:])).strip()
#     print(newFrase)
#     print(len(newFrase))
  
  
#     return strArr

# # keep this function call here 
# print(Matematica(int(input('Numero de frases: '))))



# frase = ['oir', 'mundo', '23', 'primeiro']

# for item in frase:
#     if item.isdigit() == True:
#         print('MATEMATICA')
#     else:
#         print('Não tem numero')

# frase = 'ola mundo;teste frase'
# newFrase = frase.split()
# print(len(newFrase))
# ===============================================================================



# ============================== codigo principal do estagio======================================





def Matematica(strArr):
    separa_paralavra = []
    for palavra in strArr[1:]:       
        separa_paralavra.append(len(palavra.split()))  

    if strArr[0] < 1 or strArr[0] > 100:      # 0 < Número máximo de entradas <= 100  
        print('Numero de entrada nao permitida!')    
            
    elif max(separa_paralavra) > 100:     # 0 < Número máximo de palavras em uma frase < 100
        print('Numero de palavras na frase ultrapassado!')

    else:   # Execução do código principal
        new = []    # Verificador de número na frase
        Mat = []    # Nova Lista com substituição por MATEMATICA
        for frase in strArr[1:]:
            Mat.append(frase)                     
            if ' ' in frase:            
                palavra = frase.replace(' ', '')
                new.append(palavra.isalpha())                
            else:
                new.append(frase.isalpha()) 
        while False in new:
            indice = new.index(False)
            Mat[indice] = 'MATEMATICA'            
            new[indice] = 'feito'

        formatacao = ';'.join(Mat).split(';')   #Formatação
        # print(formatacao)

        newStrArr = ''
        for frase in formatacao:                
            reversao = ' '.join(frase.split()[::-1]) + ';'  #Reversão        
            # print(reversao)
            newStrArr += reversao    
        return newStrArr.strip()

# keep this function call here 

entrada= [4, 'Olá mundo', 'Tchau 3Mundo', 'mundo', 'Primeiro mundo']

print(Matematica(entrada))

# ============================= FIM DO CODIGO ======================================
# def test(ok):

#     new = []    
#     for frase in ok:        
#         if ' ' in frase:            
#             palavra = frase.replace(' ', '')
#             new.append(palavra.isalpha())                
#         else:
#             new.append(frase.isalpha())    
#     while False in new:
#         indice = new.index(False)
#         ok[indice] = 'MATEMATICA'
#         new[indice] = 'feito' 
    
#     return ok

        

# teste = ['irlan', 'primeiro mundo', 'mundo', 'Tchau mundo', '3 malucos']
# print(test(teste))



# separa_paralavra = ' '.join(frase[1:]).split(' ')




# def codigo(frase):
#     separa_paralavra = []
    
#     for palavra in frase[1:]:       
#         # separa_paralavra.append(new_func(palavra))
#         separa_paralavra.append(len(palavra.split()))
        


#     if frase[0] < 1 or frase[0] > 100:        # 0 < Número máximo de entradas <= 100  
#         print('Numero de entrada nao permitida')    

#     elif max(separa_paralavra) > 4:       # 0 < Número máximo de palavras em uma frase < 100
#         print('Numero de palavras na frase ultrapassado') 
    

#     else:            
#         return frase[1:] 
      
            
# teste = [4, 'Olá mundo', 'Primeiro mundo', '1 mundo', 'Tchau mundo']

# print(codigo(teste))           
        
            
            


        
# if False in new:
#         for i in range(tamanho):
#             ok[new.index(False)] = 'MATEMATICA'


    







    









