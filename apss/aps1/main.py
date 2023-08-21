import pygame
import numpy as np
import random
from Classes.planeta import Planeta
from Classes.alvo import Alvo
from Classes.objeto import Objeto
import time

pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)

# Estado inicial do jogo, ou, "nivel 0"
state = {
    'level': 0,
    'objeto': Objeto(100.0, 100.0),
    'planetas': [Planeta(300, 400, 80, 0.005)],
    'alvos': [Alvo(600, 400)],
    'chances': 10,
    'mouse_click': False
}

# Função para mudar de nível a partir do estado atual
def level_change():
    if state['level'] == 1:
        state['objeto'] = Objeto(750.0, 20.0)
        state['planetas'] = [Planeta(200, 600, 100, 0.0005), Planeta(600, 200, 100, 0.0005)]
        state['alvos'] = [Alvo(400, 400), Alvo(400, 600)]

    if state['level'] == 2:
        state['objeto'] = Objeto(750.0, 20.0)
        state['planetas'] = [Planeta(200, 500, 100, 0.005), Planeta(600, 500, 100, 0.005)]
        state['alvos'] = [Alvo(400, 400), Alvo(400, 600), Alvo(400, 200)]
    
    if state['level'] == 3:
        screen.fill(BLACK)
        screen.blit(pygame.font.SysFont('Arial', 50).render('Você venceu!', True, (0,255,0)), (250, 250))
        pygame.display.update()
        pygame.quit()

        

rodando = True

while rodando:
    #colisão com parede
    if state['objeto'].s[0] < 0 or state['objeto'].s[0] > 800 or state['objeto'].s[1] < 0 or state['objeto'].s[1] > 800:
        state['objeto'].s = state['objeto'].s0.copy()
        state['objeto'].v = np.array([0,0])
        state['mouse_click'] = False
        # Se acabarem as chances, o jogo acaba
        if state['chances'] == 0:
            rodando = False
    
    # Eventos
    for event in pygame.event.get():
        # Fechar a janela
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN and state['chances'] > 0 and not state['mouse_click']:
            state['mouse_click'] = True
            state['chances'] -= 1 
            mouse = pygame.mouse.get_pos()
            mouse = np.array(mouse)
            v = mouse - state['objeto'].s
            mod = np.linalg.norm(v)
            cos = v[0] / mod
            sen = v[1] / mod

            hipW = 2
            w = np.array([cos*hipW, sen*hipW])
            s = state['objeto'].s

            #Processar posicoes
            state['objeto'].set_v(w)
    state['objeto'].s += state['objeto'].v 

    # Objeto colidindo com o planeta
    for planeta in state['planetas']:
        if np.linalg.norm(planeta.s - state['objeto'].s) < planeta.raio:
            planet_pull = planeta.atrator * (planeta.s - state['objeto'].s)
            state['objeto'].v += planet_pull

    # Objeto colidindo com o alvo
    alvo_hitsum = 0
    for alvo in state['alvos']:
        if alvo.hit:
            alvo_hitsum += 1
        if np.linalg.norm(alvo.s - state['objeto'].s) < 35:
            state['alvos'].remove(alvo)
            state['objeto'].v = np.array([0,0])
            state['mouse_click'] = False
            alvo.hit = True
    if alvo_hitsum == len(state['alvos']):
        state['level'] += 1
        level_change()
    
    # Controlar frame rate
    clock.tick(FPS)

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar os planetas, alvos e objetos
    for planeta in state['planetas']:
        planeta.draw(screen)

    for alvo in state['alvos']:
        alvo.draw(screen)

    state['objeto'].draw(screen)

    # Atualizar a tela
    pygame.display.update()

# Terminar tela
pygame.quit()