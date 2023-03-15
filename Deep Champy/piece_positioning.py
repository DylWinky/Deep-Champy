
"""
Tables read from top to bottom and left to right (top left = a1), 
This is beacause of the numbering system from chess library which is used as index, 0 is a1, while 0th element in list is 1st. 
"""
pawn_table = [ #I try and make it so it favours the ideal pawn centre, keeps its kingside castle intact, and favours potentially dangerous passed pawns.
 0,  0,  0,  0,  0,  0,  0,  0,  
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  5,  10,  10,  -20,  0,  0,
 0,  0,  10,  20,  20,  -10,  -10,  -10,          
 0,  0,  0,  5,  15,  15,  0,  0,
 30,  30,  30,  30,  30,  30,  30,  30,
 40,  40,  40,  40,  40,  40,  40,  40,
 0,  0,  0,  0,  0,  0,  0,  0 ]


knight_table = [                         #Basiaclly control the centre.    
 0, 0,  0,  0,  0,  0,  0,  0,  
 5,  10,  15,  15,  15,  15,  10,  5,
 10,  15,  20,  20,  20,  20,  15,  10,
 15, 20,  25,  25,  25,  25,  20,  15,          
 15,  25,  30,  30,  30,  30,  25,  15,
 10, 15,  20,  20,  20,  20,  15,  10,  
 5,  10,  15,  15,  15,  15,  10,  5,
 0,  5,  5,  5,  5,  5,  5,  0, ]


bishop_table = [                         #Favours the most common bishop development as seen in standard openings.
 0,  0,  0,  0,  0,  0,  0,  0,  
 0,  30,  0,  10,  10,  0,  30,  0,
 0,  30,  20,  20,  20,  30,  0,  0,
 0,  0,  25,  0,  0,  25,  0,  0,          
 0,  20,  0,  0,  0,  0,  20,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0 ]

rook_table = [   
 0,  0,  10,  20,  20,  15,  0,  0,  #Prefer centre files. Support from the back rank. Rooks on the 7th are strong
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,          
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 50,  50,  50,  50,  50,  50,  50,  50,
 0,  0,  0,  0,  0,  0,  0,  0 ]

queen_table = [   
 0,  0,  0,  0,  0,  0,  0,  0,  
 0,  0,  15,  15,  10,  0,  0,  0,      #Queen = supporting acctress (aboids centre). Sligt plus to queenside development
 0,  10,  0,  0,  0,  -30,  -40,  -50,
 10,  0,  -50,  -60,  -60,  -50,  0,  0,          
 0,  0,  -50,  -60,  -60,  -50,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0 ]

king_table = [   
 70,  70,  50,  0,  0,  20,  90,  70,  
 -50,  -50,  -50,  -50,  -50,  -50,  -50,  -50,
 -60,  -60,  -60,  -60,  -60,  -60,  -60,  -60,
 -70,  -70,  -70,  -70,  -70,  -70,  -70,  -70,          
 -70,  -70,  -70,  -70,  -70,  -70,  -70,  -70,
 -70,  -70,  -70,  -70,  -70,  -70,  -70,  -70,
 -70,  -70,  -70,  -70,  -70,  -70,  -70,  -70,
 -70,  -70,  -70,  -70,  -70,  -70,  -70,  -70 ]

"""
Endgame piece tables. Makes everything favour the centre. Pawns wanna be pushed. Rooks still like the 7th.
"""


king_table_endgame = [                         #Basiaclly control the centre.    
 0, 5,  5,  5,  5,  5,  5,  0,  
 5,  10,  15,  15,  15,  15,  10,  5,
 10,  15,  20,  20,  20,  20,  15,  10,
 15, 20,  25,  25,  25,  25,  20,  15,          
 15,  20,  25,  25,  25,  25,  20,  15,
 10, 15,  20,  20,  20,  20,  15,  10,  
 5,  10,  15,  15,  15,  15,  10,  5,
 0,  5,  5,  5,  5,  5,  5,  0, ] 

pawn_table_endgame = [                         #Push em baby
 0,  0,  0,  0,  0,  0,  0,  0,
 10,  10,  10,  10,  10,  10,  10,  10,          
 21,  21,  21,  21,  21,  21,  21,  21,
 33,  33,  33,  33,  33,  33,  33,  33,
 46,  46,  46,  46,  46,  46,  46,  46,
 60,  60,  60,  60,  60,  60,  60,  60,          
 75,  75,  75,  75,  75,  75,  75,  75,
 91,  91,  91,  91,  91,  91,  91,  91, ]

knight_table_endgame = [                         #Basiaclly control the centre.    
 0, 5,  5,  5,  5,  5,  5,  0,  
 5,  10,  15,  15,  15,  15,  10,  5,
 10,  15,  20,  20,  20,  20,  15,  10,
 15, 20,  25,  25,  25,  25,  20,  15,          
 15,  20,  25,  25,  25,  25,  20,  15,
 10, 15,  20,  20,  20,  20,  15,  10,  
 5,  10,  15,  15,  15,  15,  10,  5,
 0,  5,  5,  5,  5,  5,  5,  0, ]

bishop_table_endgame = [                         #Basiaclly control the centre.    
 0, 5,  5,  5,  5,  5,  5,  0,  
 5,  10,  15,  15,  15,  15,  10,  5,
 10,  15,  20,  20,  20,  20,  15,  10,
 15, 20,  25,  25,  25,  25,  20,  15,          
 15,  20,  25,  25,  25,  25,  20,  15,
 10, 15,  20,  20,  20,  20,  15,  10,  
 5,  10,  15,  15,  15,  15,  10,  5,
 0,  5,  5,  5,  5,  5,  5,  0, ]

queen_table_endgame = [                         #Basiaclly control the centre.    
 0, 5,  5,  5,  5,  5,  5,  0,  
 5,  10,  15,  15,  15,  15,  10,  5,
 10,  15,  20,  20,  20,  20,  15,  10,
 15, 20,  25,  25,  25,  25,  20,  15,          
 15,  20,  25,  25,  25,  25,  20,  15,
 10, 15,  20,  20,  20,  20,  15,  10,  
 5,  10,  15,  15,  15,  15,  10,  5,
 0,  5,  5,  5,  5,  5,  5,  0, ]

rook_table_endgame = [                         #Basiaclly control the centre. Rooks on the 7th are strong    
 0, 5,  5,  5,  5,  5,  5,  0,  
 5,  10,  15,  15,  15,  15,  10,  5,
 10,  15,  20,  20,  20,  20,  15,  10,
 15, 20,  25,  25,  25,  25,  20,  15,          
 15,  20,  25,  25,  25,  25,  20,  15,
 10, 15,  20,  20,  20,  20,  15,  10,  
 40,  40,  40,  40,  40,  40,  40,  40,
 0,  5,  5,  5,  5,  5,  5,  0, ]

def piece_positioning(position):
    pawns = sum([pawn_table[i] for i in position.pieces(1, True)]) - sum([pawn_table[i] for i in position.pieces(1, False).mirror()])
    knights = sum([knight_table[i] for i in position.pieces(2, True)]) - sum([knight_table[i] for i in position.pieces(2, False).mirror()])
    bishops = sum([bishop_table[i] for i in position.pieces(3, True)]) - sum([bishop_table[i] for i in position.pieces(3, False).mirror()])
    rooks = sum([rook_table[i] for i in position.pieces(4, True)]) - sum([rook_table[i] for i in position.pieces(4, False).mirror()])
    queens =  sum([queen_table[i] for i in position.pieces(5, True)]) - sum([queen_table[i] for i in position.pieces(5, False).mirror()])
    kings =  sum([king_table[i] for i in position.pieces(6, True)]) - sum([king_table[i] for i in position.pieces(6, False).mirror()])
    total = pawns + knights + bishops + rooks + queens + kings
    return total

def piece_positioning_endgame(position):
    pawns = sum([pawn_table_endgame[i] for i in position.pieces(1, True)]) - sum([pawn_table_endgame[i] for i in position.pieces(1, False).mirror()])
    knights = sum([knight_table_endgame[i] for i in position.pieces(2, True)]) - sum([knight_table_endgame[i] for i in position.pieces(2, False).mirror()])
    bishops = sum([bishop_table_endgame[i] for i in position.pieces(3, True)]) - sum([bishop_table_endgame[i] for i in position.pieces(3, False).mirror()])
    rooks = sum([rook_table_endgame[i] for i in position.pieces(4, True)]) - sum([rook_table_endgame[i] for i in position.pieces(4, False).mirror()])
    queens =  sum([queen_table_endgame[i] for i in position.pieces(5, True)]) - sum([queen_table_endgame[i] for i in position.pieces(5, False).mirror()])
    kings =  sum([king_table_endgame[i] for i in position.pieces(6, True)]) - sum([king_table_endgame[i] for i in position.pieces(6, False).mirror()])
    total = pawns + knights + bishops + rooks + queens + kings
    return total    

