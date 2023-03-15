import chess
import chess.polyglot
import random 
from piece_positioning import *


engine_white = False #Set the colour the engine plays


def engine_move(position, maxamizing_player, depth):
    try:
        opening_move = chess.polyglot.MemoryMappedReader("Perfect2021.bin").choice(position).move
        print("book move")
        return opening_move
    except:        
        if maxamizing_player == True:
            best_eval = -100000 #inital value of best eval, set very small so that all true evaluations will be chosen over it 
            for move in position.legal_moves:
                position.push(move)
                eval = minimax(position, depth-1, False)
                position.pop()
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            return best_move

        elif maxamizing_player == False:
            best_eval = 100000 #inital value of best eval, set very large so that all true evaluations will be chosen over it 
            for move in position.legal_moves:
                position.push(move)
                eval = minimax(position, depth-1, True)
                position.pop()
                if eval < best_eval:
                    best_eval = eval
                    best_move = move
            return best_move    

                

def minimax(position, depth, maximizing_player, alpha = -100000, beta = 100000):
    if depth == 0 or position.king(True) == None or position.king(False) == None or position.is_stalemate(): #End recursion if either depth == 0 or either king is dead
        eval = evaluation(position)
        return eval

    if maximizing_player == True:
        maxeval = -100000 #inital value of max eval, set very small so that all true evaluations will be chosen over it 
        for move in position.pseudo_legal_moves:
            position.push(move)
            eval = minimax(position, depth-1, False, alpha, beta)
            position.pop()
            maxeval = max(maxeval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxeval 

    if maximizing_player == False:
        mineval = 100000 #inital value of min eval, set very large so that all true evaluations will be chosen over it 
        for move in position.pseudo_legal_moves:
            position.push(move)
            eval = minimax(position, depth-1, True, alpha, beta)
            position.pop()
            mineval = min(mineval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return mineval 


def evaluation(position):
    global count
    eval = 0
    material = material_check(position) #Stores the result of material_check, i.e, [material count, enemy material]
    eval += material[0]    
    if material[1] == 5000 and len(position.pieces(1, engine_white)) == 0: #just king left and all pawns promoted
        eval += king_hunt(position)   
    elif material[1] <= 6500: #If endgame essentially 
        eval += piece_positioning_endgame(position) 
        eval += random.randint(-50,50)
    else:    
        eval += piece_positioning(position)
        eval += random.randint(-50,50) #To stop it always playing the same game    
    return eval


def material_check(position):
    wP = len(position.pieces(1,True))
    wN = len(position.pieces(2,True))
    wB = len(position.pieces(3,True))
    wR = len(position.pieces(4,True))
    wQ = len(position.pieces(5,True))
    wK = len(position.pieces(6,True))
    bP = len(position.pieces(1,False))
    bN = len(position.pieces(2,False))
    bB = len(position.pieces(3,False))
    bR = len(position.pieces(4,False))
    bQ = len(position.pieces(5,False))
    bK = len(position.pieces(6,False))
    material_count = wP*100 + wN*300 + wB*325 + wR*500 + wQ*900 + wK*5000 - bP*100 - bN*300 - bB*325 - bR*500 - bQ*900 - bK*5000  #Use Ficher's piece values (3.25 for Bishop). Source WIKI/Kasparovs Wired Vid. 5000 for king as > all other pieces combined
    if engine_white:
        enemy_material = bP*100 + bN*300 + bB*325 + bR*500 + bQ*900 + bK*5000
    else:
        enemy_material = wP*100 + wN*300 + wB*325 + wR*500 + wQ*900 + wK*5000     
    return [material_count, enemy_material]

def king_hunt(position):
    if engine_white:
        kings_squares = position.attacks(position.king(False))
        for square in kings_squares:
            if position.is_attacked_by(True, square):
                kings_squares.discard(square)
        king_mobility = len(kings_squares)
        if king_mobility == 0: #Dont stale mate
            score = -1000
        else:
            score = king_mobility * -100   
        return score
    
    else:
        kings_squares = position.attacks(position.king(True))
        for square in kings_squares:
            if position.is_attacked_by(False, square):
                kings_squares.discard(square)
        king_mobility = len(kings_squares)
        if king_mobility == 0: #Dont stale mate
            score = 1000
        else:
            score = king_mobility * 100   
        return score
  
