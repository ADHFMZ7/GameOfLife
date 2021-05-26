import numpy as np
import random

np.set_printoptions(threshold=np.inf)

def genBoard(num = int(input("board size: "))):
  board = np.zeros((num, num), int)
  for i in range(num):
    for j in range(num):
      if random.randint(0,9) < 2:
        board[i][j] = 1
  return board

def getLiveNeighbors(x, y, board):
  neighbors = 0
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if i < 0 or j < 0:
        continue
      try: 
       if board[i][j] == 1:
        neighbors += 1
      except:
        continue
  return neighbors

def compute(board):
  result = board
  for i in range(0, len(board)):
    for j in range(0, len(board)):
      if board[i][j] == 1 and (getLiveNeighbors(i, j, board) ==  2 or getLiveNeighbors(i, j, board) == 3):
        result[i][j] = 1
      elif board[i][j] == 0 and getLiveNeighbors(i, j, board) == 3:
        result[i][j] = 1
      else:
        result[i][j] = 0
  return result
