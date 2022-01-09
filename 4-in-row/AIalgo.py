import math

class AI:
  RowSize = 7
  ColSize = 6
  FullPieceScore = 10
  FourScore = 5000

  count = 0
  def __init__(self, rowSize, columnSize, fps = 2):
    self.RowSize = rowSize
    self.ColSize = columnSize
    self.FullPieceScore = fps



  def Search(self, board, depth = 0, depthLimit = 6, minOrMax = 'Max', playerPiece = 'x', enemyPiece = 'o', alpha = -math.inf, beta = math.inf):
    if (depth >= depthLimit):
      tem = AI.scorer(self, board, playerPiece, enemyPiece)
      self.count += 1
      if (minOrMax == 'Max'):
        return [tem, beta]
      elif (minOrMax == 'Min'):
        return [tem, alpha]

     
    #---------------------------------------Max---------------------------------------------- 
    if (minOrMax == 'Max'):
      position = 0
      for j in range(self.RowSize):
        for i in range(self.ColSize+1):
          if (i == self.ColSize or board[i][j] == playerPiece or board[i][j] == enemyPiece ):
      
            if (i != 0):

              board[i-1][j] = playerPiece
              tem = AI.Search(self, board, depth+1, depthLimit, 'Min', playerPiece, enemyPiece)
              board[i-1][j] = ' ' 
              
              temAlpha = max(tem)
              if (temAlpha > alpha and depth != 0 ):
                alpha = temAlpha
              elif (temAlpha > alpha and depth == 0):
                position = j
                alpha = temAlpha

              #-----------pruning---------
              if (alpha >= beta):
                if (depth == 0):
                  return j
                else:
                  return [alpha, beta]
              #------------------------
              
            break

      if (depth == 0):
        return position 
      else:
        return [alpha, beta]

    #---------------------------------------------------------------------------------------------
    #---------------------------------------Min---------------------------------------------- 
    elif (minOrMax == 'Min'):
      position = 0
      for j in range(self.RowSize):
        for i in range(self.ColSize+1):
          if (i == self.ColSize or board[i][j] == playerPiece or board[i][j] == enemyPiece ):
      
            if (i != 0):

              board[i-1][j] = enemyPiece
              tem = AI.Search(self, board, depth+1, depthLimit, 'Max', playerPiece, enemyPiece, alpha, beta)
              board[i-1][j] = ' ' 
              temBeta = min(tem)
              if (temBeta < beta and depth != 0 ):
                beta = temBeta
              elif (temBeta < beta and depth == 0):
                position = j
                beta = temBeta

              #-----------pruning---------
              if (alpha >= beta):
                if (depth == 0):
                  return j
                else:
                  return [alpha, beta]
              #------------------------
              
            break

      if (depth == 0):
        return position 
      else:
        return [alpha, beta]

      #---------------------------------------------------------------------------------------------








  def scorer(self, board, playerPiece, enemyPiece):
    score = 0
    yy1 = 0
    yy2 = 0
    for y in range(self.ColSize):
      for x in range(self.RowSize):

        if (board[y][x] == playerPiece):
          tem = AI.scoreCounter(self, board, y, x, playerPiece)
          score += tem
          if (tem >= self.FourScore):
            yy1 = y

        elif (board[y][x] == enemyPiece):
          tem = AI.scoreCounter(self, board, y, x, enemyPiece)
          score += tem
          if (tem >= self.FourScore):
            yy2 = y
    if (yy1 > yy2):
      return self.FourScore
    elif (yy2 > yy1):
      return -self.FourScore
    return score


  def scoreCounter(self, board, y, x, piece):
    #--------------------scoring row---------------------------
    count1 = 0
    count2 = 0
    isFour1 = 0
    isFour2 = 0
    score = 0
    while (count1 < 3 and count2 < 3):

      if (count1 != -1):
        count1 +=1
        if (x + count1 < self.RowSize):
          if (board[y][x+count1] == piece):
            if (isFour1 != -1):
              isFour1 += 1
            score += self.FullPieceScore
            
          elif (board[y][x+count1] == ' '):
            score += 1
            isFour1 = -1
          else:
            count1 = -1

      if (count2 != -1):
        count2 +=1
        if (x-count2 >= 0):
          if (board[y][x-count2] == piece ):
            if (isFour2 != -1):
              isFour2 += 1
            score += self.FullPieceScore
          elif (board[y][x-count2] == ' '):
            score += 1
            isFour2 = -1
          else:
            count2 = -1

      if (isFour1+isFour2 == 3 or isFour1 == 3 or isFour2 == 3):
        score += self.FourScore
      if (count1 == -1 and count2 == -1):
        break
    #-----------------------------------------------------------
    
    #--------------------scoring column---------------------------
    count1 = 0
    count2 = 0
    isFour1 = 0
    isFour2 = 0
    #score = 0
    while (count1 < 3 and count2 < 3):

      if (count1 != -1):
        count1 +=1
        if (y + count1 < self.ColSize):
          if (board[y+count1][x] == piece):
            if (isFour1 != -1):
              isFour1 += 1
            score += self.FullPieceScore
            
          elif (board[y+count1][x] == ' '):
            score += 1
            isFour1 = -1
          else:
            count1 = -1

      if (count2 != -1):
        count2 +=1
        if (y-count2 >= 0):
          if (board[y-count2][x] == piece ):
            if (isFour2 != -1):
              isFour2 += 1
            score += self.FullPieceScore
          elif (board[y-count2][x] == ' '):
            score += 1
            isFour2 = -1
          else:
            count2 = -1

      if (isFour1+isFour2 == 3 or isFour1 == 3 or isFour2 == 3):
        score += self.FourScore
      if (count1 == -1 and count2 == -1):
        break
    #-----------------------------------------------------------

    
    #--------------------scoring diagonal (\)---------------------------
    count1 = 0
    count2 = 0
    isFour1 = 0
    isFour2 = 0
    while (count1 < 3 and count2 < 3):

      if (count1 != -1):
        count1 +=1
        if (x + count1 < self.RowSize and y + count1 < self.ColSize):
          if (board[y+count1][x+count1] == piece):
            if (isFour1 != -1):
              isFour1 += 1
            score += self.FullPieceScore
            
          elif (board[y+count1][x+count1] == ' '):
            score += 1
            isFour1 = -1
          else:
            count1 = -1

      if (count2 != -1):
        count2 +=1
        if (x - count2 >= 0 and y - count2 >= 0):
          if (board[y-count2][x-count2] == piece ):
            if (isFour2 != -1):
              isFour2 += 1
            score += self.FullPieceScore
          elif (board[y-count2][x-count2] == ' '):
            score += 1
            isFour2 = -1
          else:
            count2 = -1

      if (isFour1+isFour2 == 3 or isFour1 == 3 or isFour2 == 3):
        score += self.FourScore
      if (count1 == -1 and count2 == -1):
        break
    #-----------------------------------------------------------
    
    #--------------------scoring diagonal (\)---------------------------
    count1 = 0
    count2 = 0
    isFour1 = 0
    isFour2 = 0
    while (count1 < 3 and count2 < 3):

      if (count1 != -1):
        count1 +=1
        if (x - count1 >= 0 and y + count1 < self.ColSize):
          if (board[y+count1][x-count1] == piece):
            if (isFour1 != -1):
              isFour1 += 1
            score += self.FullPieceScore
            
          elif (board[y+count1][x-count1] == ' '):
            score += 1
            isFour1 = -1
          else:
            count1 = -1

      if (count2 != -1):
        count2 +=1
        if (x + count2 < self.RowSize and y - count2 >= 0):
          if (board[y-count2][x+count2] == piece ):
            if (isFour2 != -1):
              isFour2 += 1
            score += self.FullPieceScore
          elif (board[y-count2][x+count2] == ' '):
            score += 1
            isFour2 = -1
          else:
            count2 = -1

      if (isFour1+isFour2 == 3 or isFour1 == 3 or isFour2 == 3):
        score += self.FourScore
      if (count1 == -1 and count2 == -1):
        break
    #-----------------------------------------------------------
    return score








          
          

#ai = AI(7,6)





#print(AI.Search(ai, Board, depth = 0, depthLimit = 6, minOrMax = 'Max', playerPiece='o', enemyPiece='x'))
#print(AI.scorer(ai, Board, 'o', 'x'))     
#print(ai.count)

