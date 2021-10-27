board=["-","-","-",
       "-","-","-",
       "-","-","-",]


game_still_going = True
winner=None
current_player="x"


def display_board():
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])


def play_game():
  #display board
  display_board()
  print("x's turn")

  while game_still_going:

    handle_turn(current_player)
    check_if_game_over()
    flip_player()


  if winner=='x' or winner=='o':
    print(winner+' won.')
  elif winner==None:
    print('tie.')



def handle_turn(player):
  position = input("select an integer from 1-9 : ")

  valid=False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("invalid input..select an integer from 1-9 : ")
      
    
    position=int(position)-1
    if board[position]=="-":
      valid=True
    else:
      print( "you can go there,go again!!")
  board[position]=player
  display_board()
   



def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  global winner
  row_winner=check_row()
  column_winner=check_column()
  diagonal_winner=check_diagonal()

  if row_winner:
    winner=row_winner
    

  elif column_winner:
    winner=column_winner
    
  

  elif diagonal_winner:
    winner=diagonal_winner
    

  else:
    winner=None
    return


  

  

def check_row():
  global game_still_going
  row_1=board[0]==board[2]==board[1] !="-"
  row_2=board[3]==board[4]==board[5] !="-"
  row_3=board[6]==board[7]==board[8] !="-"
  if row_1 or row_2 or row_3:
    game_still_going=False
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]
  



def check_column():
  global game_still_going
  column_1=board[0]==board[3]==board[6] !="-"
  column_2=board[1]==board[4]==board[7] !="-"
  column_3=board[2]==board[5]==board[8] !="-"
  if column_1 or column_2 or column_3:
    game_still_going=False
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]



def check_diagonal():

  global game_still_going
  diagonal_1=board[0]==board[4]==board[8] !="-"
  diagonal_2=board[2]==board[4]==board[6] !="-"
  if diagonal_1 or diagonal_2:
    game_still_going=False
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[2]


  


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False

  return

def flip_player():
  global current_player
  if current_player=="x":
    print ("o's turn")
    current_player="o"
  elif current_player=="o":
    print ("x's turn")
    current_player="x"
  return


play_game()  
