import numpy as np
lst = [1,3,2,8,5,6,7,4,9,10] #cria lista
print(np.array(lst)) #converte lista em array
print(np.arange(0,10,2)) #cria array de 0 a 10 de 2 em 2
print(np.arange(0,10)) #cria array de 0 a 10
print(np.zeros(10)) #cria array de 10 zeros
print(np.zeros((3,3))) #cria matriz 3x3 de zeros
print(np.eye(4)) #cria matriz identidade
print(np.linspace(0,10,3)) #cria array de 0 a 10 com 3 elementos
print(np.random.rand(5)) #cria array de 5 numeros aleatorios entre 0 e 1 com distribuicao uniforme
print(np.random.rand(5,5)) #cria matriz 5x5 de numeros aleatorios entre 0 e 1 com distribuicao uniforme
print(np.random.randn(2)) #cria array de 2 numeros aleatorios entre -1 e 1 com distribuicao normal
print(np.random.randn(4,4)) #cria matriz 4x4 de numeros aleatorios entre -1 e 1 com distribuicao normal
print(np.random.randint(1,100,10)) #cria array de 10 numeros aleatorios entre 1 e 100 com distribuicao uniforme
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]]) #cria matrizprint(matriz) 
matriz.reshape(1,9) #transforma matriz em array
print(matriz)
print(matriz.shape) #retorna dimensoes da matriz
print(matriz.max()) #retorna maior valor da matriz
print(matriz.min()) #retorna menor valor da matriz
print(matriz.argmax()) #retorna indice do maior valor da matriz
print(matriz.argmin()) #retorna indice do menor valor da matriz
print(matriz.dtype) #retorna tipo de dados da matriz
print(matriz.sum()) #retorna soma dos elementos da matriz
print(matriz.sum(axis=0)) #retorna soma dos elementos das colunas da matriz
print(matriz.sum(axis=1)) #retorna soma dos elementos das linhas da matriz
print(matriz.mean()) #retorna media dos elementos da matriz
print(matriz.mean(axis=0)) #retorna media dos elementos das colunas da matriz
print(matriz.mean(axis=1)) #retorna media dos elementos das linhas da matriz
print(matriz.std()) #retorna desvio padrao dos elementos da matriz
print(matriz.std(axis=0)) #retorna desvio padrao dos elementos das colunas da matriz
print(matriz.std(axis=1)) #retorna desvio padrao dos elementos das linhas da matriz
print(matriz.var()) #retorna variancia dos elementos da matriz
print(matriz.var(axis=0)) #retorna variancia dos elementos das colunas da matriz
print(matriz.var(axis=1)) #retorna variancia dos elementos das linhas da matriz
print(matriz[0]) #retorna primeira linha da matriz
print(matriz[0][0]) #retorna elemento da primeira linha e primeira coluna da matriz
print(matriz[0,0]) #retorna elemento da primeira linha e primeira coluna da matriz
print(matriz[0:2]) #retorna primeira e segunda linha da matriz
print(matriz[0:2,0:2]) #retorna primeira e segunda linha e primeira e segunda coluna da matriz
print(matriz[matriz>5]) #retorna elementos maiores que 5 da matriz
print(matriz[matriz<5]) #retorna elementos menores que 5 da matriz
print(matriz[matriz==5]) #retorna elementos iguais a 5 da matriz
print(matriz[matriz!=5]) #retorna elementos diferentes de 5 da matriz
print(matriz[matriz>=5]) #retorna elementos maiores ou iguais a 5 da matriz
print(matriz[matriz<=5]) #retorna elementos menores ou iguais a 5 da matriz
print(matriz[matriz%2==0]) #retorna elementos pares da matriz
print(matriz[matriz%2!=0]) #retorna elementos impares da matriz
print(matriz[matriz%2==1]) #retorna elementos impares da matriz

mtzAleatoria = np.random.randint(0,100,25) #cria array de 25 numeros aleatorios entre 0 e 100
mtzAleatoria_transposta = np.array(mtzAleatoria).T #transpose array
print("matriz aleatoria: ")
print(mtzAleatoria) 
print("matriz aleatoria transposta: ")
print(mtzAleatoria_transposta) #printa array transposto
