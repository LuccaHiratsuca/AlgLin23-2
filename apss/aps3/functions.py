import itertools
import numpy as np

#Criando índices 
def criar_indices(min_i,max_i,min_j,max_j):
    L = list(itertools.product(range(min_i,max_i),range(min_j,max_j)))
    idx_i = np.array([i[0] for i in L])
    idx_j = np.array([i[1] for i in L])
    idx = np.vstack((idx_i,idx_j))
    return idx


def transform(image, angle, scale):
    radians = np.radians(angle)
    image_ = np.zeros_like(image)

    X = criar_indices(0,image.shape[0],0,image.shape[1])
    X = np.vstack((X,np.ones(X.shape[1])))

    #Tipos de matrizes de transformação
    T = np.array([[1,0, image.shape[0]/2],[0,1,image.shape[1]/2],[0,0,1]]) #Translação
    T2 = np.array([[1,0, -image.shape[0]/2],[0,1,-image.shape[1]/2],[0,0,1]]) #Translação 2
    R = np.array([[np.cos(radians),-np.sin(radians),0],[np.sin(radians),np.cos(radians),0],[0,0,1]]) #Rotação
    S = np.array([[scale,0,0],[0,scale,0],[0,0,1]]) #Escala

    # Matriz de transformação final
    Xd = T @ R @ S @ T2

    # Inversa da matriz de transformação, para evitar buracos na imagem, em outras palavras, artefatos
    Xd = np.linalg.inv(Xd) @ X

    #Filtro para evitar que os índices fiquem fora da imagem
    filtro = (Xd[0,:] >= 0) & (Xd[0,:] < image.shape[0]) & (Xd[1,:] >= 0) & (Xd[1,:] < image.shape[1])
    
    #Transformando os índices em inteiros
    X = X.astype(int)
    Xd = Xd.astype(int)

    #Aplicando o filtro
    X = X[:,filtro]
    Xd = Xd[:,filtro]

    #Aplicando a transformação na imagem
    image_[X[0,:],X[1,:]] = image[Xd[0,:],Xd[1,:]]
 
    return image_



    


    