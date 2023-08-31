import numpy as np

alfabeto = 'abcdefghijklmnopqrstuvwxyz '
alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"

# Função que converte uma string para matriz one-hot
def para_one_hot(msg: str) -> np.ndarray:
    try:
        msg = msg.lower()
        matriz = np.zeros((len(msg), len(alfabeto)))
        for i in range(len(msg)):
            matriz[i][alfabeto.index(msg[i])] = 1
        return matriz.T
    except:
        print('Erro ao converter string para one-hot: CARACTERE INVÁLIDO')

# Função que converte uma matriz one-hot para string
def para_string(M: np.ndarray) -> str:
    try:
        msg = ''
        for i in range(M.shape[1]):
            msg += alfabeto[np.argmax(M[:,i])]
        return msg
    except:
        print('Erro ao converter one-hot para string: CARACTERE INVÁLIDO')

# Função que cifra uma mensagem usando a matriz de permutação P
def cifrar(msg: str, P: np.ndarray) -> str:
    try:
        return para_string((P @ para_one_hot(msg)))
    except:
        print('Erro ao cifrar mensagem: CARACTERE INVÁLIDO')

# Função que decifra uma mensagem cifrada usando a matriz de permutação P
def decifrar(msg: str, P: np.ndarray) -> str:
    try:
        return para_string(np.linalg.inv(P) @ para_one_hot(msg))
    except:
        print('Erro ao decifrar mensagem: CARACTERE INVÁLIDO')

# Função que cifra uma mensagem pelo enigma
def enigma(msg: str, P: np.ndarray, E: np.ndarray) -> str:
    try:
        msg_cifrada = ""
        msg = msg.lower()
        for i in range(len(msg)):
            char_atual = msg[i]
            index = alfabeto.index(char_atual)
            alfabeto_novo = para_string(P)
            msg_cifrada += alfabeto_novo[index]
            P = cifrar(alfabeto_novo, E)
            P = para_one_hot(P)
        return msg_cifrada
    except:
        print('Erro ao cifrar-enigma mensagem: CARACTERE INVÁLIDO')

# Função que recupera uma mensagem cifrada pelo enigma
def de_enigma_1(msg: str, P: np.ndarray, E: np.ndarray) -> str:
    try:  
        msg_decifrada = ""
        msg = msg.lower()
        indice = 0
        for letra in msg:
            for u in range(indice):
                letra = decifrar(letra, E)
            letra = decifrar(letra, P)
            msg_decifrada += letra
            indice += 1
        return msg_decifrada
    except:
        print('Erro ao decifrar-enigma mensagem: CARACTERE INVÁLIDO')

# Metodologia 2
def de_enigma_2(msg: str, P: np.ndarray, E: np.ndarray) -> str:
    try:  
        msg_decifrada = ""
        msg = msg.lower()
        for i in range(len(msg)):
            char_atual = msg[i]
            alfabeto_novo = para_string(P)
            index = alfabeto_novo.index(char_atual)
            msg_decifrada += alfabeto[index]
            P = cifrar(alfabeto_novo, E)
            P = para_one_hot(P)
        return msg_decifrada
    except:
        print('Erro ao decifrar-enigma mensagem: CARACTERE INVÁLIDO')

print(para_one_hot('o bolo de chocolate fica pronto quatro horas da tarde'))
print(para_string(para_one_hot('o bolo de chocolate fica pronto quatro horas da tarde')))
print(cifrar('o bolo de chocolate fica pronto quatro horas da tarde', para_one_hot(alfabeto_cifrado)))
print(decifrar(cifrar('o bolo de chocolate fica pronto quatro horas da tarde', para_one_hot(alfabeto_cifrado)), para_one_hot(alfabeto_cifrado)))
print(enigma('o bolo de chocolate fica pronto quatro horas da tarde', para_one_hot(alfabeto_cifrado), para_one_hot(cifrador_auxiliar)))
print(de_enigma_1(enigma('o bolo de chocolate fica pronto quatro horas da tarde', para_one_hot(alfabeto_cifrado), para_one_hot(cifrador_auxiliar)), para_one_hot(alfabeto_cifrado), para_one_hot(cifrador_auxiliar)))
print(de_enigma_2(enigma('o bolo de chocolate fica pronto quatro horas da tarde', para_one_hot(alfabeto_cifrado), para_one_hot(cifrador_auxiliar)), para_one_hot(alfabeto_cifrado), para_one_hot(cifrador_auxiliar)))

# Exemplo de erro de caractere inválido
print(enigma('o bolo de chocolate fica pronto quatro hor!as da tarde', para_one_hot(alfabeto_cifrado), para_one_hot(cifrador_auxiliar)))