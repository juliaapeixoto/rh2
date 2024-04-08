import pygame
import sys
from definitions import *
from niveis import *
from pagtab6 import *
from definitions import * 
from RH_Board import *



imagem_do_fundo_do_mcqueen = pygame.image.load("fontes\imagens\_mcqueen.jpg")
imagem_do_fundo_do_botao_faisca=pygame.image.load("fontes\imagens\ frameforlevels.png")

def get_font(size): 
    font = pygame.font.Font("fontes\letras fonts\BungeeSpice-Regular\BungeeSpice.ttf", size)
    return font


def tab_6(screen, game):
    game
    if game == 'back':
        tab_6(screen)
    elif game == 'menu':
        main_menu(screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method)


#mudar os botões
def tab_6modofacil(screen):                                          
    while True:
        posicao_do_rato = pygame.mouse.get_posicao()
        screen.blit (imagem_do_fundo_do_botao_faisca, (0, 0))

        tab6_botaoparavoltaratras = Button(posicao=(480, 590), text_input="Voltar Atrás", 
                            letra=get_font(30), base_color="YELLOW", hover=(255, 255, 0))
        tab6_botaoparavoltaratras.changeColor(posicao_do_rato)
        tab6_botaoparavoltaratras.update(screen)

        LEVEL1_BUTTON = Button(posicao=(200,260), text_input= "LEVEL 1", letra=get_font(30), base_color="YELLOW", hover=(255, 255, 0))
        LEVEL1_BUTTON.changeColor(posicao_do_rato)
        LEVEL1_BUTTON.update(screen)       

        LEVEL2_BUTTON = Button(posicao=(425,260), text_input= "LEVEL 2", letra=get_font(30), base_color="YELLOW", hover=(255, 255, 0))
        LEVEL2_BUTTON.changeColor(posicao_do_rato)
        LEVEL2_BUTTON.update(screen)

        LEVEL3_BUTTON = Button(posicao=(200,385), text_input= "LEVEL 3", letra=get_font(30),base_color="YELLOW", hover=(255, 255, 0))
        LEVEL3_BUTTON.changeColor(posicao_do_rato)
        LEVEL3_BUTTON.update(screen)

        LEVEL4_BUTTON = Button(posicao=(425,385),text_input= "LEVEL 4", letra=get_font(30), base_color="YELLOW", hover=(255, 255, 0))
        LEVEL4_BUTTON.changeColor(posicao_do_rato)
        LEVEL4_BUTTON.update(screen)

        LEVEL5_BUTTON = Button(posicao=(310,515), text_input= "LEVEL 5", letra=get_font(30), base_color="YELLOW", hover=(255, 255, 0))     
        LEVEL5_BUTTON.changeColor(posicao_do_rato)
        LEVEL5_BUTTON.update(screen)

#substituir pelos levels que a carolina fizer - levelx_pieces
#substituir board pelo board que a maaria fez
#play_game_in_pygame é substituido por o que fizer depois

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tab6_botaoparavoltaratras.checkForInput(posicao_do_rato):
                    play(screen)
                elif LEVEL1_BUTTON.checkForInput(posicao_do_rato):                         
                    game = outrapags(screen, 'LEVEL 1', level1_pieces, RushHourBoard, search_method.choose, max_depth_options.depth)
                    tab6_botaoparavoltaratras(screen, game)
                elif LEVEL2_BUTTON.checkForInput(posicao_do_rato):                         
                    game = outrapags(screen, 'LEVEL 2', level2_pieces, RushHourBoard, search_method.choose, max_depth_options.depth)
                    tab6_botaoparavoltaratras(screen, game)
                elif LEVEL3_BUTTON.checkForInput(posicao_do_rato):                         
                    game = outrapags(screen, 'LEVEL 3', level3_pieces, RushHourBoard, search_method.choose, max_depth_options.depth)
                    tab6_botaoparavoltaratras(screen, game)
                elif LEVEL4_BUTTON.checkForInput(posicao_do_rato):                         
                    game = outrapags(screen, 'LEVEL 4', level4_pieces, RushHourBoard, search_method.choose, max_depth_options.depth)
                    tab6_botaoparavoltaratras(screen, game)
                elif LEVEL5_BUTTON.checkForInput(posicao_do_rato):                         
                    game = outrapags(screen, 'LEVEL 5', level5_pieces, RushHourBoard, search_method.choose, max_depth_options.depth)
                    tab6_botaoparavoltaratras(screen, game)

        pygame.display.update()


def play(screen):
    pygame.display.set_caption("click to play")
    while True:
      PLAY_MOUSE_POS = pygame.mouse.get_pos() #***
      screen.blit (imagem_do_fundo_do_botao_faisca, (0, 0))

      DIF_TEXT = get_font(30).render("CLICK ON THE LEVEL YOU WANT TO PLAY", True, RED)
      DIF_RECT = DIF_TEXT.get_rect(center= (316, 200))
      screen.blit(DIF_TEXT, DIF_RECT)

      PLAY_BACK = Button(posicao=(310, 600), text_input ="Voltar Atrás", letra=get_font(30), base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png")) 
      PLAY_BACK.changeColor(PLAY_MOUSE_POS)
      PLAY_BACK.update(screen)

      facil=Button(posicao=(230,310), text_input="tabuleiro 6*6", letra=get_font(25),base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png")) 
      facil.changeColor(PLAY_MOUSE_POS)
      facil.update(screen)

      for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN:
                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                     main_menu(screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method)
             if event.type == pygame.MOUSEBUTTONDOWN:
                if facil.checkForInput(PLAY_MOUSE_POS):
                     tab_6modofacil(screen)
                     
      pygame.display.update()


def options_methods (screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method): 
    pygame.display.set_caption("Opção de Modo de Pesquisa")

    OPTIONS_BACK = Button(posicao=(210,325), text_input="Voltar Atrás", letra=get_font(25),base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png"))
    
    OPTIONS_TEXT = get_font(40).render("OPÇÕES", True, YELLOW)
    DIF_RECT = OPTIONS_TEXT.get_rect(center= (316, 155))

    DEPTH = Button (posicao=(210,325), text_input="Depth-First Search", letra=get_font(25),base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png"))
    BREADTH = Button (posicao=(210,325), text_input="Breadth_First Search", letra=get_font(25),base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png"))
    A_STAR = Button (posicao=(210,325), text_input="A_STAR", letra=get_font(25),base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png")) 
    GREEDY = Button (posicao=(210,325), text_input="Greedy", letra=get_font(25),base_color="YELLOW", hover=(255, 255, 0), imagem=pygame.image.load("fontes\imagens\_botap.png"))
    
    #**eliminar
    DEPTH = Button(posicao=(210,545), text_input= "DEPTH:", font=get_font(20), base_color="Pink", hovering_color=(173, 216, 230))

    #**rever amanha

    while True:
        OPTIONS_MOUSE_POS= pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    atualizar_search_method(search_method)
                    main_menu(screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method)
                if DEPTH_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= True
                    breadth_options.breadth = True
                    a_star_options.a_star = False
                    greedy_options.greedy = False
                if DEPTH_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                if BREADTH_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = True
                    a_star_options.a_star = False
                    greedy_options.greedy = False
                if BREADTH_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                if A_STAR_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                if A_STAR_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = False
                    a_star_options.a_star = False
                    greedy_options.greedy = True
                if GREEDY_ON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = False
                    a_star_options.a_star = False
                    greedy_options.greedy = True
                if GREEDY_OFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    depth_options.depth= False
                    breadth_options.breadth = False
                    a_star_options.a_star = True
                    greedy_options.greedy = False
                
                    #**eliminar 
                if first_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    max_depth_options.depth = 15
                if second_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    max_depth_options.depth = 50
                if third_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    max_depth_options.depth = 100



        screen.blit (imagem_do_fundo_do_botao_faisca, (0, 0))

        screen.blit(OPTIONS_TEXT, DIF_RECT)
#**achoque isto passa para cima - ver

             
        if depth_options.depdth == True:
            DEPTH_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            DEPTH_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
        else:
            DEPTH_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            DEPTH_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
        DEPTH.update(screen)
        DEPTH_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        DEPTH_ON_BUTTON.update(screen)
        DEPTH_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        DEPTH_OFF_BUTTON.update(screen)
            
        if breadth_options.breadth == True:
            BREADTH_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            BREADTH_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
        else:
            BREADTH_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            BREADTH_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
        BREADTH.update(screen)
        BREADTH_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BREADTH_ON_BUTTON.update(screen)
        BREADTH_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BREADTH_OFF_BUTTON.update(screen)
  
        if a_star_options.a_star == True:
            A_STAR_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            A_STAR_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
        else:
            A_STAR_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            A_STAR_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
        A_STAR.update(screen)
        A_STAR_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        A_STAR_ON_BUTTON.update(screen)
        A_STAR_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        A_STAR_OFF_BUTTON.update(screen)

        if greedy_options.greedy == True:
            GREEDY_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            GREEDY_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hovering_color=(253, 136, 48))
        else:
            GREEDY_ON_BUTTON = Button(posicao=(400,320), text_input= "ON", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))
            GREEDY_OFF_BUTTON = Button(posicao=(480,320), text_input= "OFF", letra=get_font(20), base_color=(255, 160, 48), hover=(253, 136, 48))   
        GREEDY.update(screen)
        GREEDY_ON_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        GREEDY_ON_BUTTON.update(screen)
        GREEDY_OFF_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        GREEDY_OFF_BUTTON.update(screen)
#**Eliminar -aaa estou quase finished
        if max_depth_options.depth == 15:
            first_BUTTON = Button(image=None, pos=(320,545),
                            text_input= "15", font=get_font(20), base_color='Green', hovering_color='Pink')
            second_BUTTON = Button(image=None, pos=(400,545),
                                    text_input= "50", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            third_BUTTON = Button(image=None, pos=(480,545),
                            text_input= "100", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        elif max_depth_options.depth == 50:
            first_BUTTON = Button(image=None, pos=(320,545),
                            text_input= "15", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            second_BUTTON = Button(image=None, pos=(400,545),
                                    text_input= "50", font=get_font(20), base_color='Green', hovering_color='Pink')
            third_BUTTON = Button(image=None, pos=(480,545),
                            text_input= "100", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
        else:
            first_BUTTON = Button(image=None, pos=(320,545),
                            text_input= "15", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            second_BUTTON = Button(image=None, pos=(400,545),
                                    text_input= "50", font=get_font(20), base_color=(173, 216, 230), hovering_color='Pink')
            third_BUTTON = Button(image=None, pos=(480,545),
                            text_input= "100", font=get_font(20), base_color='Green', hovering_color='Pink')
        DEPTH.update(screen)
        first_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        first_BUTTON.update(screen)
        second_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        second_BUTTON.update(screen)
        third_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        third_BUTTON.update(screen)

        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)       

        atualizar_search_method(search_method)
        pygame.display.update()


def main_menu(screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method): 
    pygame.display.set_caption("Menu")
    while True:
        screen.blit (imagem_do_fundo_do_mcqueen, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXTO = get_font(40).render("MENU PRINCIPAL", True, (173, 216, 230))
        MENU_RECT = MENU_TEXTO.get_rect(center= (316, 200))
        screen.blit(MENU_TEXTO, MENU_RECT)

        CLICA_PARA_JOGAR = Button(posicao=(316, 312), text_input="CLICA PARA JOGAR", letra=get_font(25),base_color=(255, 160, 48), hover=(253, 136, 48))
        OPTIONS_BUTTON = Button(posicao=(316, 425),text_input="NÍVEIS", font=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48))
        QUIT_BUTTON = Button(posicao=(316, 535), text_input="QUIT", font=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48))

        for button in [CLICA_PARA_JOGAR, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLICA_PARA_JOGAR.checkForInput(MENU_MOUSE_POS):
                    play(screen)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options_methods(screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def start_pygame():
    pygame.init()
    screen = pygame.display.set_mode((630,750))
    main_menu(screen, depth_options, breadth_options, a_star_options, greedy_options, max_depth_options, search_method)
