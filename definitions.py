# alteravel
BLACK = (0, 0, 0)
WHITISH = (255, 255, 255)
GRAY = (200, 200, 200)
DARKGREY = (40, 40, 40)
RED = (255, 0, 0)
YELLOW=(241, 225, 0)~
PINK=(255,192,203)
GREEN = (0, 255, 0)
BLUE = (0, 0, 100)
MCQUEEN=(243, 7, 21)
BGCOLOUR = BLUE

#alterar na terca
WIDTH = 630 
HEIGHT = 750 
FPS= 60 
title = "Rush Hour - The Game "
TILESIZE = 70 
GAME_SIZE = 4 

#menu buttons
class Button():
    def __init__(self, posicao, text_input, letra, base_color, hover, imagem=None):
        self.x_posicao = posicao [0]
        self.y_posicao = posicao [1]
        self.letra = letra
        self.base_color, self.hover = base_color, hover
        self.text_input = text_input
        self.imagem=imagem
        self.text = self.letra.render(self.text_input, True, self.base_color)
        self.rect = self.base_color.get_rect(center=(self.x_posicao, self.y_posicao))
        self.text_rect =self.text.get_rect(center=(self.x_posicao, self.y_posicao))

    def update (self, screen):
        screen.blit(self.text, self.text_rect)

    def checkForInput(self,position):
        #verificar
        if position [0] in range (self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
       #a cor do botão muda com o curso em cima
        if position [0] in range (self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            self.text = self.letra.render(self.text_input, True, self.hover)
        else:
            self.text= self.letra.render(self.text_input, True, self.base_color)



#define depth 'on' or 'off'
class DEPTH():
    def __init__(self, depth):
        self.depth = depth
    
depth = True
depth_options = DEPTH(depth)

#define breadth 'on' or 'off'
class BREADTH():
    def __init__(self, breadth):
        self.breadth = breadth
    
breadth = False
breadth_options = BREADTH(breadth)

#define A* 'on' or 'off'
class A_STAR():
    def __init__(self, a_star):
        self.a_star = a_star
    
a_star = False
a_star_options = A_STAR(a_star)

#define greedy 'on' or 'off'
class GREEDY():
    def __init__(self, greedy):
        self.greedy = greedy
    
greedy = False
greedy_options = GREEDY(greedy)


#define the search method being used:
class _SEARCH_METHOD_():
    def __init__(self, search_method):
        self.choose = search_method

search_method = _SEARCH_METHOD_('Depth')

def atualizar_search_method(depth_on, breadth_on, a_star_on, greedy_on):
    if depth_on:
        return DEPTH()
    elif breadth_on:
        return BREADTH()
    elif a_star_on:
        return A_STAR()
    elif greedy_on:
        return GREEDY()
    else:
        return None 


#perguntar a prof se isto e necessario**
class _DEPTH_():
    def __init__(self, depth):
        self.depth = depth
    
max_depth = 50
max_depth_options = _DEPTH_(max_depth)