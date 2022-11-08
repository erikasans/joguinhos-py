#coding: utf-8
import pygame as pg #importa o modulo
from random import randrange

#define variaveis para facilitar na definição de cores
white =(255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (135, 206, 250)

# testa se o jogo esta iniciando corretamente
try:
    pg.init()
except:
    print("o módulo pygame nao iniciou com sucesso")

# variaveis para tamanho da tela e objeto
width = 560
height = 520
tamanho=10

relogio = pg.time.Clock()
background = pg.display.set_mode((width, height)) # abre uma janela e define o tamanho da tela
pg.display.set_caption("Snake") # nomeia a janela do jogo

def text(msg, cor, tam, x, y): #função para criar texto
    font = pg.font.SysFont("Arial", tam)
    txt1 = font.render(msg, True, cor)
    background.blit(txt1, [x, y])
def cobra(CobraXY): # função para criar cobra
    for XY in CobraXY:
        pg.draw.rect(background, black,[ XY[0], XY[1], tamanho, tamanho])

def apple(pos_x, pos_y): # função para criar maça
    pg.draw.rect(background, red, [pos_x, pos_y, tamanho, tamanho])

#função jogo
def jogo():
    sair = True
    gover = False
    pos_x = randrange(0, width-tamanho, 10)# determina o espaço da cobra na tela e ocomo ira se mover
    pos_y = randrange(0, height-tamanho, 10)
    m_x = randrange(0, width-tamanho, 10)
    m_y = randrange(0, height-tamanho, 10)
    vel_x = 0
    vel_y = 0
    CobraXY = []
    Comp = 1
    while sair:
        while gover:
            background.fill(white)
            text("Fim de jogo, para continuar tecle Space  ou S para sair:", red, 22, width/8, height/2)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:  # fecha o jogo
                    sair = False
                    gover = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        sair = True
                        gover = False
                        pos_x = randrange(0, width - tamanho, 10)
                        pos_y = randrange(0, height - tamanho, 10)
                        m_x = randrange(0, width - tamanho, 10)
                        m_y = randrange(0, height - tamanho, 10)
                        vel_x = 0
                        vel_y = 0
                        CobraXY = []
                        Comp = 1
                    if event.key == pg.K_s:
                        sair = False
                        gover = False
        for event in pg.event.get():
            if event.type == pg.QUIT:#fecha o jogo
                sair = False
            if event.type == pg.KEYDOWN:#inicio configuração dos botões
                if event.key == pg.K_LEFT and vel_x != tamanho:
                    vel_y = 0
                    vel_x = -tamanho
                if event.key == pg.K_RIGHT and vel_x != -tamanho:
                    vel_y = 0
                    vel_x = +tamanho
                if event.key == pg.K_DOWN and vel_y != -tamanho:
                    vel_x = 0
                    vel_y = +tamanho
                if event.key == pg.K_UP and vel_y != tamanho:
                    vel_x = 0
                    vel_y = -tamanho
        if sair:
            background.fill(blue)
            pos_x+= vel_x
            pos_y+= vel_y

            CobraInicio = [] # movimento da cobra
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > Comp:
                del CobraXY[0]


            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                gover = True

            pg.draw.rect(background, black, [40, height-40, width, 0])

            cobra(CobraXY)
            if pos_x == m_x and pos_y == m_y: # quando a cobra come
                m_x = randrange(0, width - tamanho, 10)
                m_y = randrange(0, height - tamanho, 10)
                Comp += 1
            apple(m_x,m_y)
            pg.display.update()
            relogio.tick(10) # velocidade
            if pos_x > width:
                gover = True
            if pos_x < 0:
                gover = True
            if pos_y > height:
                gover = True
            if pos_y < 0:
                gover = True


jogo()
pg.quit()
