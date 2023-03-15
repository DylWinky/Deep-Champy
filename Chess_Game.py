import pygame as p
import chess
import chess.pgn
from Chess_Engine import *

p.init
champy_logo = p.transform.scale(p.image.load("Images/Champy.jpg"),(32, 32)) #Logo on window
p.display.set_icon(champy_logo) #Logo on window
board = chess.Board()
game = chess.pgn.Game() #For pgn
node = game #For pgn writing

width = height = 400 
dimension = 8 #dimensions of chess board are 8x8 
sq_size = height//dimension 
images = {} #Dictionary of images
piece_translation = {(1, True):'wP', (2, True):'wN', (3, True):'wB', (4, True):'wR', (5,True):'wQ', (6,True):'wK',      #Dictionary to store the translation from the chess library to a more standard notation for pieces
                (1, False):'bP', (2, False):'bN', (3, False):'bB', (4, False):'bR', (5,False):'bQ', (6,False):'bK'}      

square_translation = {} #Dictionary to store translation of squares from (x,y) to integer as is used by chess library 
square = -1 #Generating the dictionary
for row in range(dimension):
    for column in range(dimension):
        square += 1 
        square_translation[(column,row)] = square
   
if engine_white == True:
    human_turn = False #Used to keep track of whether its the players turn, or the engines 
    game.headers["White"] = "Deep Champy" #Sets the header for the pgn output
elif engine_white == False:
    human_turn = True    
    game.headers["Black"] = "Deep Champy"

node = game #For pgn writing                          


def load_images(): #Putting the images in out dictionary
    pieces = ['wR','wQ','wP','wN','wK','wB','bR','bQ','bP','bN','bK','bB']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"),(sq_size, sq_size))

def main():
    global node
    global human_turn
    screen = p.display.set_mode((width,height))
    load_images()
    sq_selected = () #Stores a tuple representing the coordinates of the last square the user selected (x,y)
    player_clicks = [None, None] #Stores the last two clicks from the user, used to make a move
    promotion = False

    running = True
    while running: #game loop

        if human_turn == True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    print(game) #For PGN
                    running = False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_q:     
                        print ("queening?")
                        promotion = True   
                if event.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos() #(x,y) location of mouse click. Remember that pygame coordinates start from top left
                    column = location[0]//sq_size
                    row = 7 - location[1]//sq_size     
                    sq_selected = (column,row)
                    if sq_selected == player_clicks[0]: #If the user clicks same square twice
                        sq_selected = ()
                        player_clicks = [None, None]
                    elif player_clicks[0] == None:
                        player_clicks[0] = sq_selected  
                    elif player_clicks[1] == None:
                        player_clicks[1] = sq_selected   
                        make_move(player_clicks, promotion) #player_clicks now has two values so make a 
                        if board.is_game_over():
                            game.headers["Result"] = board.result()
                            print(game) #For PGN
                            print("Grrr, u win!")
                            running = False
                            break
                        player_clicks = [None, None] #Clears player_clicks ready for the next move
                        promotion = False

        elif human_turn == False:
            p.event.set_blocked(None) #Prevents events being added to queue when engine is thinking (eg user clicks), as this can cause pygame to think its being unresponsive since engine can take a long time
            deep_champy_move = engine_move(board,engine_white, 3)
            p.event.set_allowed(None)
            board.push(deep_champy_move)
            node = node.add_variation(deep_champy_move)
            if board.is_game_over(): 
                game.headers["Result"] = board.result()
                print(game) #For PGN
                print("Meow, GG!") 
                running = False
                break
            human_turn = True                   


        
        draw_position(screen, board, player_clicks) 
        p.display.flip() #Updates the screen
        


def draw_position(screen, board, player_clicks):
    if human_turn:
        p.display.set_caption("YOUR TURN")
    else:
        p.display.set_caption("DEEP CHAMPY'S TURN")    
    draw_board(screen, player_clicks)
    draw_pieces(screen, board)

def draw_board(screen, player_clicks):
        colours = [p.Color("grey"), p.Color("white")]
        for row in range(dimension):
            for column in range(dimension):
                if (column,row) == player_clicks[0]:
                    p.draw.rect(screen,p.Color("green"),p.Rect(column*sq_size,((7*sq_size)-(row*sq_size)),sq_size,sq_size)) #Highlights selected square
                else:
                    colour = colours[((row+column)%2)]
                    p.draw.rect(screen,colour,p.Rect(column*sq_size,((7*sq_size)-(row*sq_size)),sq_size,sq_size))

def draw_pieces(screen, board):
    square = -1
    for row in range(dimension):
            for column in range(dimension):
                square += 1 
                nasty_piece = (board.piece_type_at(square), board.color_at(square))
                if nasty_piece != (None,None):
                    piece = piece_translation[nasty_piece]
                    screen.blit(images[piece], p.Rect(column*sq_size,((7*sq_size)-(row*sq_size)),sq_size,sq_size))

def make_move(player_clicks, promotion):
    global node
    global human_turn
    sq_1 = square_translation[player_clicks[0]]
    sq_2 = square_translation[player_clicks[1]]
    if promotion == True:
        move = chess.Move(sq_1,sq_2, 5)
        if move in board.legal_moves:
            board.push(move)
            node = node.add_variation(move)
            human_turn = False
    elif promotion == False:
        move = chess.Move(sq_1, sq_2)
        if move in board.legal_moves:
            board.push(move)  
            node = node.add_variation(move) #For PGN writing
            human_turn = False 
                 
        

if __name__ == "__main__":  #Python convention - doesnt run if imported 
    main()