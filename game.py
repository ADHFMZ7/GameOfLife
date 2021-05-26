from main import *
import time

board = genBoard()

while True:
  board = compute(board)
  print(board)
  #input("press enter to proceed...")
  time.sleep(0.3)
