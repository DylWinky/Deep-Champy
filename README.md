# Deep-Champy
A chess playing program (chess engine), that uses a minimax algorithm with alpha-beta pruning. 
## Installation 
Requires the python libraries pygame (https://www.pygame.org/docs/ref/display.html) and python-chess (https://python-chess.readthedocs.io/en/latest/). Run from the main file 'Chess_Game.py'. 
## Usage 
Make moves by clicking on a square containing one of your pieces, followed by the square you wish to move the piece to. In order to promote a pawn to a queen, press q on your keyboard, followed by moving a pawn to the 8th rank (or 1st rank if playing black).    

You can change which colour you play as by setting the Boolean variable 'engine_white' as True if you wish to play black, or False to play as white. This can be found on line 7 of the 'Chess_Engine.py' file.  

The depth that the engine plays at (how deep it searches the tree of possible moves) can be set by changing the integer value passed into the function 'engine_move' on line 87 of the 'Chess_Game.py' file. A higher depth will result in stronger play; however the engine will take longer to make a move.  
