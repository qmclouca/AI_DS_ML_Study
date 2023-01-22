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


