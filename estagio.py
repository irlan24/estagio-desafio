

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
               
    if strArr[0] < 1 or strArr[0] > 100:        # 0 < Número máximo de entradas <= 100
        print('Numero de entrada nao permitida!')

    separa_paralavra = []
    for palavra in strArr[1:]:      # 0 < Número máximo de palavras em uma frase < 100 
        separa_paralavra.append(len(palavra.split()))        
    if max(separa_paralavra) > 100:
        print('Numero de palavras na frase ultrapassado!')

    else:
        formatacao = ';'.join((strArr)[1:]).split(';')
        # print(formatacao)

        newStrArr = ''
        for frase in formatacao:                
            reversao = ' '.join(frase.split()[::-1]) + ';'        
            # print(reversao)
            newStrArr += reversao    
        return newStrArr

# keep this function call here 

entrada= [4, 'Olá mundo', 'Tchau Mundo', '1 mundo', 'Primeiro mundo']

print(Matematica(entrada))

# ============================= FIM DO CODIGO ======================================



# separa_paralavra = ' '.join(frase[1:]).split(' ')




# def codigo(frase):    
#         separa_paralavra = []
#         if frase[0] < 1 or frase[0] > 100:      # 0 < Número máximo de entradas <= 100
#             print('Numero de entrada nao permitida')
#         for palavra in frase[1:]:       # 0 < Número máximo de palavras em uma frase < 100         
#                 separa_paralavra.append(len(palavra.split()))
#                 print(separa_paralavra)
#         if max(separa_paralavra) > 5:
#                 print('Numero de palavras na frase ultrapassado')



#         else:            
#             return frase[1:]

            
            
            
        
 
# teste = [4, 'Olá mundo', 'Primeiro mundo', '1 mundo i i i ', 'Tchau mundo']


# print(codigo(teste))           
        
            
            
        



    
        



    







    









