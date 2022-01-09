import AIalgo 
import os


# checking the rule i.e 4 in row
class Game: 
  RowSize = 7
  ColSize = 6 # size of the Board

  def __init__(self, RowSize = 7, ColSize = 6):
    self.RowSize = RowSize
    self.ColSize = ColSize


  def play(self, playerPiece = 'x', enemyPiece = 'o'):

    ai = AIalgo.AI(self.RowSize, self.ColSize)


    board = [[' ' for i in range(self.RowSize)] for j in range(self.ColSize)] 
    Turn = 1
    PieceType = ''
    while (True):
      position = -1

      #-----------------input postion of the piece ---------------------
      if (Turn == 1):
        while (position < 0 or position >= self.RowSize):
          position = int(input('Enter postion from 0-6:'))
        PieceType = playerPiece
      else:
        while (position < 0 or position >= self.RowSize):
          position = int(input('Enter postion from 0-6:'))

          #===============================================AI======================================================================
          #position = AIalgo.AI.Search(ai, board, depth = 0, depthLimit = 6, minOrMax = 'Max', playerPiece= playerPiece, enemyPiece=enemyPiece)
          #================================================================================================================
       
        PieceType = enemyPiece
        #-----------------------------------------------------------------------
      
      #--------------------------filing the board----------------------------------
      for i in range(self.ColSize+1):
        if (i == self.ColSize or board[i][position] == playerPiece or board[i][position] == enemyPiece ):
          if (i != 0):
            board[i-1][position] = PieceType                 
          break
      #---------------------------------------------------------------------------


      #------------------checking the rules of the game------------------
      tem = Game.CheckForFour(self, i-1, position, board, PieceType )
      #-------------------------------------------------------------------


      #----------------------printing board-----------------------------
      if (not tem ):
        if (Turn == 1):
          Turn = 2
        elif (Turn == 2):
          Turn = 1
        os.system('cls')
        print('\n\n')
        for x in board:
          print(x)
          
      
      else:
        print('--------------------')
        print('player', Turn, 'wins')
        print('--------------------')
        for x in tem:
          board[x[0]][x[1]] = PieceType.capitalize()
        for x in board:
          print(x)
        return 
      #----------------------------------------------------------------------




  # (i,j checking from postion Board[i][j]), (Board = playing board for 4 in row)
  # (PieceType = Piece which we will be checking (e.g x = player, 0 for enemy))
  def CheckForFour(self,i,j, Board, PieceType):

    #-------------------------checking for 4 in a row------------------------------
    counter = 0
    Highlight = []
    counter = Game.Check(self, Board, i, j, 0, 'row', 1, PieceType, Highlight)

    if (counter < 4):
      counter = Game.Check(self, Board, i, j-1, counter, 'row', -1, PieceType, Highlight)
    if (counter >= 4):
      return Highlight # returing True if found 4 in row
    del Highlight
    #------------------------------------------------------------------------------

    #-------------------------checking for 4 in a column---------------------------
    counter = 0
    Highlight = []
    counter = Game.Check(self, Board, i, j, 0, 'col', 1, PieceType, Highlight)

    if (counter < 4):
      counter = Game.Check(self, Board, i-1, j, counter, 'col', -1, PieceType, Highlight)
    if (counter >= 4):
      return Highlight
    del Highlight
    #------------------------------------------------------------------------------


    #-----------checking for 4 in a (upper-left to bottom-right) diagonal-----------
    counter = 0
    Highlight = []
    counter = Game.Check(self, Board, i, j, 0, 'diag1', 1, PieceType, Highlight)

    if (counter < 4):
      counter = Game.Check(self, Board, i-1, j-1, counter, 'diag1', -1, PieceType, Highlight)
    if (counter >= 4):
      return Highlight
    del Highlight
    #------------------------------------------------------------------------------


    #-----------checking for 4 in a (upper-right to bottom-left) diagonal-----------
    counter = 0
    Highlight = []
    counter = Game.Check(self, Board, i, j, 0, 'diag2', 1, PieceType, Highlight)

    if (counter < 4):
      counter = Game.Check(self, Board, i+1, j-1, counter, 'diag2', -1, PieceType, Highlight)

    if (counter >= 4):
      return Highlight
    del Highlight
    #------------------------------------------------------------------------------


    return [] # if not found 

  #----------------------------- checking recursively------------------------------
  # (Board = Board of 4 in a row), (i,j the postion which is being checked), (counter = how many in row or col etc)
  # (DirectionType = (row,col,dig1, dig2)), (direction = in a certain dircigon type e.g for row it's left or right)
  # (Piece Type = piece we are checking for) 
  def Check(self, Board, i, j, counter, DirectionType, direction, PieceType, Highlight):

    if ((i < 0 or i >= self.ColSize) or (j < 0 or j>= self.RowSize)):#check if out of bounds
      return counter

    # (1) checking the piece type(player piece or enemy piece)
    # (2) checking if four in a row
    if (Board[i][j] != PieceType or counter >= 4):
      return counter
    Highlight.append([i,j])

    if (DirectionType == 'row'):
      return Game.Check(self,Board, i, j + (1 * direction) , counter+1, DirectionType, direction, PieceType, Highlight) 

    elif (DirectionType == 'col'):
      return Game.Check(self,Board, i + (1 * direction), j, counter+1, DirectionType, direction, PieceType,Highlight)

    elif (DirectionType == 'diag1'):
      return Game.Check(self,Board, i + (1 * direction), j + (1 * direction), counter+1, DirectionType, direction, PieceType, Highlight)
    
    elif (DirectionType == 'diag2'):
      return Game.Check(self,Board, i + (-1 * direction), j + (1 * direction), counter+1, DirectionType, direction, PieceType, Highlight)
    #----------------------------------------------------------------------------------------------------------------------------



if (__name__ == "__main__"):
  game = Game()
  Game.play(game)


#CheckRule.CheckForFour(CheckRul,2,2, Board, 'x')



