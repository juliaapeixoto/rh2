from RH_Board import*
from game import *
from levels import * 
from copy import deepcopy
from RH_Algorithms import breadth_first_search
from RH_Algorithms import depth_first_search
from RH_Algorithms import a_star_manhattan
from RH_Algorithms import greedy_search_manhattan
from definitions import Button
import pygame
from sys import exit
#alteravel -parte das coisas que queria ver com voces
WIDTH = 630
HEIGHT = 750
ROWS = 7
COLUMNS = 6
SIZE = 70

imagem_do_fundo_do_mcqueen = pygame.image.load("fontes\imagens\_mcqueen.jpg")
imagem_do_fundo_do_botao_faisca=pygame.image.load("fontes\imagens\ frameforlevels.png")

def get_font(size): 
    font = pygame.font.Font("fontes\letras fonts\BungeeSpice-Regular\BungeeSpice.ttf", size)
    return font

# aqui estamos a criar os nossos veículos, de forma a que fiquem retangulos coloridos e unidos - fiz nas 6*6 porque sao as que temos agora
# Definir ROWS, COLUMNS, SIZE conforme necessário - NAO SEI SE PRECISAMOS DISTO AAA -ok esquecam precisamos estou a entender
ROWS = 6
COLUMNS = 6
SIZE = 50

def veiculoscriar(board):
    veiculoscriados = {}

    for x_matrix in range(ROWS):
        for y_matrix in range(COLUMNS):
            y_board = x_matrix
            x_board = y_matrix

            piece_id = board[x_matrix][y_matrix]
            rect = pygame.Rect(x_board * SIZE, y_board * SIZE, SIZE, SIZE)

            if piece_id in veiculoscriar:
                veiculoscriados[piece_id].append(rect)
            else:
                veiculoscriados[piece_id] = [rect]

    return veiculoscriados

# juntar retangulos iguais
def rectangles_union(piece_id, veiculoscriados):
    for rectangle in veiculoscriados[piece_id]:
                if rectangle == veiculoscriados[piece_id][0]:
                    old_rect = rectangle
                else:
                    new_rect = old_rect.union(rectangle)
                    old_rect = new_rect
    return new_rect


# draws the board e carritos -isto precisamos - O a B C O X TEM DE ESTAR EM LEVELS
def draw_board(screen, game_board_surface, board):
    veiculoscriados = veiculoscriar(board)
    

    for piece_id in veiculoscriados:
        if piece_id == 'X':
            for rectangle in veiculoscriados[piece_id]:
                pygame.draw.rect(game_board_surface, 'RED', rectangle)
        elif piece_id == 'O':
            new_rect = rectangles_union(piece_id, veiculoscriados)
            pygame.draw.rect(game_board_surface, 'YELLOW', new_rect)
        elif piece_id == 'C':
            new_rect = rectangles_union(piece_id, veiculoscriados)
            pygame.draw.rect(game_board_surface, 'PINK', new_rect)
        elif piece_id == 'A':
            new_rect = rectangles_union(piece_id, veiculoscriados)
            pygame.draw.rect(game_board_surface, 'GREEN', new_rect)
        elif piece_id == 'B':
            new_rect = rectangles_union(piece_id, veiculoscriados)
            pygame.draw.rect(game_board_surface, 'BLUE', new_rect)
        else:
            if len(veiculoscriados[piece_id]) == 0:
                for rectangle in veiculoscriados[piece_id]:
                    pygame.draw.rect(game_board_surface, 'WHITE', rectangle)


def detect_piece_id(level, mouse_position_down):
    x_mouse_position_down, y_mouse_position_down = mouse_position_down
    
    # Calcula a posição na matriz com base na posição do mouse - 160 e 105 são valores fixos que ajustam as coordenadas do mouse para alinhar corretamente com a grade do tabuleiro do jogo, permitindo uma detecção precisa de qual célula da matriz foi clicada com o mouse. Certifique-se de ajustar esses valores de acordo com o layout e o tamanho do tabuleiro do seu jogo, para garantir que as posições do mouse sejam mapeadas corretamente para as células da matriz.
    x_matrix = (y_mouse_position_down - 160) // SIZE
    y_matrix = (x_mouse_position_down - 105) // SIZE
    
    # Obtém o ID da peça na posição da matriz
    piece_id = level.board[x_matrix][y_matrix]
    
    # Verifica se a peça pode ser movida (se não for uma peça vazia '0' ou um obstáculo '*')
    if piece_id in ['0', '*']:
        moving = False
    else:
        moving = True
    
    # Retorna o ID da peça e um indicador de se a peça pode ser movida
    return piece_id, moving


def detect_direction(mouse_position_down, mouse_position_up):
    x_down, y_down = mouse_position_down
    x_up, y_up = mouse_position_up
    
    # Calculate the differences along x and y axes
    dx = x_up - x_down
    dy = y_up - y_down
    
    # Determine the direction based on the larger absolute difference
    if abs(dx) >= abs(dy):
        direction = 'left' if dx < 0 else 'right'
    else:
        direction = 'up' if dy < 0 else 'down'
    
    return direction

#-----------------------------
#AQUI JUNTAMOS A PAGINA INICIAL COM AS OUTRAS 
def outrapags(screen, level, pieces, board, search_method, max_depth):
    level_pieces = deepcopy(pieces)
    board = create_board(level_pieces, board)
    game = game(level_pieces, board)
   

    pygame.init()
    pygame.display.set_caption("RUSH HOUR - THE GAME")
 #**perguntar -|

    board_surface = pygame.Surface((420,490))
    board_surface.fill('GREY')
    board_rectangle = board_surface.get_rect(topleft = (105,130))
    pieces_move_surface = pygame.Surface((280, 350))
    pieces_move_rectangle = pieces_move_surface.get_rect(topleft = (175,200))

    botao_do_nivel=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
    
    botao_voltar_atras=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
    
    botao_desistir=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
    botao_menu=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
    
    botao_voltar_atentar=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
#botao acho que se retira
    CONTINUE_BUTTON=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 

    CONTINUE_YES_BUTTON=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
    
    CONTINUE_NO_BUTTON=Button( posicao=(318, 45), text_input=level, letra=get_font(25), base_color=(255, 160, 48), hover=(253, 136, 48), image=pygame.image.load("fontes/imagens/botap.png")) 
    
    run = True
    moving = False
    while run:
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position_down = pygame.mouse.get_pos()

                if CONTINUE_YES_BUTTON.checkForInput(mouse_position_down):
                    return 'back'

                if CONTINUE_NO_BUTTON.checkForInput(mouse_position_down):
                    pygame.quit()
                    exit()

                if botao_desistir.checkForInput(mouse_position_down):
                    pygame.quit()
                    exit()

                if botao_voltar_atras.checkForInput(mouse_position_down):
                    return 'back'
                
                if botao_menu.checkForInput(mouse_position_down):
                    return 'menu'
                

                if pieces_move_rectangle.collidepoint(mouse_position_down):
                    moving = True
                    piece_id, moving = detect_piece_id(game, mouse_position_down)

                if botao_voltar_atentar.checkForInput(mouse_position_down):
                    level_pieces = deepcopy(pieces)
                    game_board = create_game_board(level_pieces, board)
                    game = game(level_pieces, game_board)

            elif event.type == pygame.MOUSEBUTTONUP and moving == True: 
                mouse_position_up = pygame.mouse.get_pos()
                direction = detect_direction(mouse_position_down, mouse_position_up) 
                if direction == None:
                    pass
                else: #retirar aqui
                    stamp = False
                    if game.win() == False:
                        game.move_pieces(piece_id, direction, stamp)
                    else:
                        pass
                    HINT_BUTTON=Button(image=pygame.image.load("Resources\Images\_button.png"), pos=(169, 710), 
                                    text_input='HINT', font=get_font(25), base_color=(173, 216, 230), hovering_color="Pink")
                    if colorblind_options == False:
                        colorblind = False
                moving = False


        screen.blit(imagem_do_fundo_do_mcqueen, (0,0))
        screen.blit(pieces_move_surface, pieces_move_rectangle)
        screen.blit(board_surface, board_rectangle)
        draw_board(screen, board_surface, game.board, colorblind)
        screen.blit(imagem_do_fundo_do_botao_faisca, (0, 0))
        
        botao_do_nivel.update(screen)

        botao_menu.changeColor(mouse_position)
        botao_menu.update(screen)

        botao_voltar_atras.changeColor(mouse_position)
        botao_voltar_atras.update(screen)

        botao_voltar_atras.changeColor(mouse_position)
        botao_voltar_atentar.update(screen)

        if game.win() == False:
            botao_desistir.changeColor(mouse_position)
            botao_desistir.update(screen)

        if game.win() != False:
            CONTINUE_BUTTON.update(screen)

            CONTINUE_YES_BUTTON.changeColor(mouse_position)
            CONTINUE_YES_BUTTON.update(screen)

            CONTINUE_NO_BUTTON.changeColor(mouse_position)
            CONTINUE_NO_BUTTON.update(screen)

        pygame.display.update()      