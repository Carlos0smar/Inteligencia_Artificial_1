from math import inf as infinity
from random import choice
import platform
import time
from os import system



HUMANO = -1
COMPUTADOR = +1
board = [[0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0]]

def evaluate(estado):
    """
    Función de evaluación del estado de finalización del juego.
     : parametro: estado, estado actual del tablero
     : devuelve: +1 si COMPUTADOR gana; -1 si el HUMANO gana; 0 en caso de empate
    """
    if wins(estado, COMPUTADOR):
        score = +1
    elif wins(estado, HUMANO):
        score = -1
    else:
        score = 0

    return score

def wins(estado, player):
    """
    Esta funcion verifica si un jugador especifico gana. Posibilidades:
    * cuatro filas    [X X X X] or [O O O O] = 18 posibilidades
    * cuatro columnas    [X X X X] or [O O O O]= 18 posibilidades
    * cuatro diagonales [X X X X] or [O O O O]= 18 posibilidades(contantdo de izquierda a derecha y de derecha a izquierda)
    * En total son 54 posibilidades
    :parametro estado, el estado del tablero actual
    :parametro player: un HUMANOo o un COMPUTADORutador
    :devuelve: True si un jugador gana

    """
#se crea una lista con las posibles combinaciones ganadoras
    for it in range(len(estado)):
        #iteración para filas 1-4
        if estado[it][0] == estado[it][1] == estado[it][2] == estado[it][3] == player:
            return True
        #iteración para filas 2-5
        elif estado[it][1] == estado[it][2] == estado[it][3] == estado[it][4] == player:
            return True
        #iteración para filas 3-6
        elif estado[it][2] == estado[it][3] == estado[it][4] == estado[it][5] == player:
            return True
        #iteración para columnas 1-4
        elif estado[0][it] == estado[1][it] == estado[2][it] == estado[3][it] == player:
            return True
        #iteración para columnas 2-5
        elif estado[1][it] == estado[2][it] == estado[3][it] == estado[4][it] == player:
            return True
        #iteración para columnas 3-6
        elif estado[2][it] == estado[3][it] == estado[4][it] == estado[5][it] == player:
            return True

    #iteración para diagonales-centro-izquierda-derecha
    if estado[0][0] == estado[1][1] == estado[2][2] == estado[3][3] == player:
        return True
    elif estado[1][1] == estado[2][2] == estado[3][3] == estado[4][4] == player:
        return True
    elif estado[2][2] == estado[3][3] == estado[4][4] == estado[5][5] == player:
        return True
    #iteración para diagonales-col1-izquierda-derecha
    elif estado[0][1] == estado[1][2] == estado[2][3] == estado[3][4] == player:
        return True
    elif estado[1][2] == estado[2][3] == estado[3][4] == estado[4][5] == player:
        return True
    #iteración para digonales-col2-izquierda-derecha
    elif estado[0][2] == estado[1][3] == estado[2][4] == estado[3][5] == player:
        return True
    #iteración para diagonales-row1-izquierda-derecha
    elif estado[1][0] == estado[2][1] == estado[3][2] == estado[4][3] == player:
        return True
    elif estado[2][1] == estado[3][2] == estado[4][3] == estado[5][4] == player:
        return True
    #iteración para diagonales-row2-izquierda-derecha
    elif estado[2][0] == estado[3][1] == estado[4][2] == estado[5][3] == player:
        return True

    #iteración para diagonales-centro-derecha-izquierda
    if estado[0][5] == estado[1][4] == estado[2][3] == estado[3][2] == player:
        return True
    elif estado[1][4] == estado[2][3] == estado[3][2] == estado[4][1] == player:
        return True
    elif estado[2][3] == estado[3][2] == estado[4][1] == estado[5][0] == player:
        return True
    #iteración para diagonales-col1-derecha-izquierda
    elif estado[0][4] == estado[1][3] == estado[2][2] == estado[3][1] == player:
        return True
    elif estado[1][3] == estado[2][2] == estado[3][1] == estado[4][0] == player:
        return True
    #iteración para diagonales-col2-derecha-izquierda
    elif estado[0][3] == estado[1][2] == estado[2][1] == estado[3][0] == player:
        return True
    #iteración para diagonales-row1-derecha-izquierda
    elif estado[1][5] == estado[2][4] == estado[3][3] == estado[4][2] == player:
        return True
    elif estado[2][4] == estado[3][3] == estado[4][2] == estado[5][1] == player:
        return True
    #iteración para diagonales-row2-derecha-izquierda
    elif estado[2][5] == estado[3][4] == estado[4][3] == estado[5][2] == player:
        return True
    return False


def game_over(estado):
    """
    Esa funcion verifica si el HUMANO o el COMPUTADOR gana
    :parametro estado, estado del tablero actual
    :devuelve: True si el HUMANO o el COMPUTADOR gana
    """
    return wins(estado, HUMANO) or wins(estado, COMPUTADOR)


def empty_cells(estado):
    """
    Cada celda vacía se agregará a la lista de celdas
    :parametro estado, estado de tablero actual
    :devuelve, una lista de las celdas vacias
    """
    cells = []

    for x, fila in enumerate(estado):
        for y, cell in enumerate(fila):
            if cell == 0:
                cells.append([x, y])
    return cells

def valid_move(x, y):
    """
    Un movimiento es válido si la celda elegida está vacía
    :parametro x, coordenada X
    :parametro y, coordenada Y 
    :devuelve: True si la posicion del tablero[x][y] esta vacia
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False

def set_move(x, y, player):
    """
    Establece un movimiento en el tablero, si las coordenadas son validas
    :parametro x, coordenada X
    :parametro y, coordenada Y
    :parametro player, jugador actual
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False

#se agrega alpha y beta
def minimax(estado, depth, player, alpha, beta):
    """
    Funcion IA que elige la mejor movida
    AI function that choice the best move
    :parametro estado, estado actual en el tablero
    :param depth, indice del nodo en el arbol (0 <= depth < 36), pero nunca treinta y seis.
    :param player, un HUMANO o un COMPUTADOR
    :devuelve, una lista con [la mejor fila, la mejor columna, el mejor score]
    """
    
    # si el juego termina, o alcanza la profundidad maxima, retorna el estado en score
    if depth == 0 or game_over(estado):
        score = evaluate(estado)
        return [-1, -1, score]

#se agrega alpha y beta
    if player == COMPUTADOR:
#si el jugador es el computador, se busca el maximo valor
        best = [-1, -1, -infinity]
#recorre las celdas vacias y las llena con el jugador
        for cell in empty_cells(estado):
            x, y = cell[0], cell[1]
            #se asigna el valor del jugador a la celda
            estado[x][y] = player
            score = minimax(estado, depth - 1, -player, alpha, beta)
            estado[x][y] = 0
            #se asigna la posisión de la celda del mejor movimiento
            score[0], score[1] = x, y
            #se pregunta si el score es mayor a best(mejor score anterior, al empezar el juego es -infinito) ya que se busca maximizar
            if score[2] > best[2]:
                #se asigna el nuevo mejor score(que es el mayor)
                best = score
                #determina el mayor entre el mejor score y el valor de alpha(que es el mejor-mayor score del anterior)
                alpha = max(alpha, best[2])
                #si alpha es mayor o igual a beta, se corta el bucle
            if alpha >= beta:
                break
        #devuelve el mejor score
        return best
    else:
#si el jugador es el humano, se busca el minimo valor
        best = [-1, -1, +infinity]
#recorre las celdas vacias y las llena con el jugador
        for cell in empty_cells(estado):
            x, y = cell[0], cell[1]
            #se asigna el valor del jugador a la celda
            estado[x][y] = player
            score = minimax(estado, depth - 1, -player, alpha, beta)
            estado[x][y] = 0
            #se asigna la posisión de la celda del mejor movimiento
            score[0], score[1] = x, y
            #se pregunta si el score es menor a best(mejor score anterior, al empezar el juego es +infinito) ya que se busca minimizar
            if score[2] < best[2]:
                #se asigna el nuevo mejor score(que es el menor)
                best = score
                #determina el menor entre el mejor score y el valor de beta(que es el mejor-menor score del anterior)
                beta = min(beta, best[2])
            #si alpha es mayor o igual a beta, se corta el bucle
            if alpha >= beta:
                break
        #devuelve el mejor score
        return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(estado, c_choice, h_choice):
    """
    Print the board on console
    :param estado: current estado of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '------------------------------'

    print('\n' + str_line)
    for fila in estado:
        for cell in fila:
            symbol = chars[cell]
            print(f'| {symbol} |', end = '')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    Esta funcion llama a la funcion minimax si la profundidad es < 9,
    caso contrario esta elige una coordenada aleatoria.
    :param c_choice: COMPUTADOR elije X o O
    :param h_choice: HUMANO elije X o O
    :return:
    """
    #se inicializan alpha y beta
    alpha = -infinity
    beta = +infinity
    
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Juega COMPUTADOR [{c_choice}]')
    render(board, c_choice, h_choice)
    #la profundidad es menor a 32, se llama a la funcion minimax
    if depth > 32:
        #se elige una coordenada aleatoria
        x = choice([0, 1, 2, 3, 4, 5])
        y = choice([0, 1, 2, 3, 4, 5])
    else:
        move = minimax(board, depth, COMPUTADOR, alpha , beta)
        x, y = move[0], move[1]

    set_move(x, y, COMPUTADOR)
    time.sleep(1)

def HUMANO_turn(c_choice, h_choice):
    """
    El HUMANO juega eligiendo una movida valida.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    #los movimientos validos son los que estan en el diccionario 
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4:[0,3],  5:[0,4], 6:[0,5],
        7: [1, 0], 8: [1, 1], 9: [1, 2], 10:[1,3], 11:[1,4], 12:[1,5],
        13: [2, 0], 14: [2, 1], 15: [2, 2], 16:[2,3], 17:[2,4], 18:[2,5],
        19: [3, 0], 20: [3, 1], 21: [3, 2], 22:[3,3], 23:[3,4], 24:[3,5],
        25: [4, 0], 26: [4, 1], 27: [4, 2], 28:[4,3], 29:[4,4], 30:[4,5],
        31: [5, 0], 32: [5, 1], 33: [5, 2], 34:[5,3], 35:[5,4], 36:[5,5]
    }

    clean()
    print(f'turno HUMANO [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 36:
        try:
            move = int(input('Use los numeros (1..36): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMANO)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if HUMANO is the first

    # HUMANO chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting COMPUTADORuter's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # HUMANO may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        HUMANO_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMANO):
        clean()
        print(f'HUMANO turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMPUTADOR):
        clean()
        print(f'COMPUTADORuter turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()