#!python3

"""
Create a function that will determine if one person is the winner (has 3 in a row)
inputs:
list board : the list that contains the board data

return:
str 'X' if X is the winner
str 'O' if O is the winner
None if there is no winner
"""

def whoWins(board):
  print(f"{board[0]} {board[1]} {board[2]}\n{board[3]} {board[4]} {board[5]}\n{board[6]} {board[7]} {board[8]}\n")
  

  #vertical
  for i in range(0,3):
    if board[i] == board[i+3] and board[i+3] == board[i+6]:
      return board[i]

  #horizontal
  
  if board[0] == board[1] and board[1] == board[3]:
    return board[0]

  elif board[4] == board[5] and board[5] == board[6]:
    return board[4]

  elif board[7] == board[8] and board[8] == board[9]:
    return board[7]

  #diagonals
  elif board[0] == board[4] and board[4] == board[8]:
    return board[0]
    
  elif board[2] == board[4] and board[4] == board[6]:
    return board[2]




def main():
  board = [ 'O','X',0,'X','O',0,'X',0,'O']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','O','X','O','O','X']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','X','O','O','X','O']
  assert whoWins(board) == None
  board = [ 'X','O',0,'X','X','X','O','O','X']
  assert whoWins(board) == 'X'

if __name__ == "__main__":
  main()
