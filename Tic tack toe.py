import itertools
def win(current_game):
    #horizontal
    def all_same(l):
      if l.count(l[0])==len(l) and l[0]!=0:
         return True
      else:
          return False
    for row in game:
        print(row)
        if all_same(row): 
            print(f" player {row[0]} is the horizontal winner!")
            return True


    #Diagonal
    diags=[]
    for col,row in enumerate(reversed(range(len(game)))):
       diags.append(game[row][col])
    if all_same(diags):
        print(f"player {diags[0]} is the diagonal winner(/)!")
        return True

        
       
    diags=[]
    for ix in range(len(game)):
       diags.append(game[ix][ix])

       
    if all_same(diags):
            print(f"player {diags[0]} is the diagonal winner(\)!")
            return True

#vertical
    for col in range(len(game)):
     check=[]
     for row in game:
         check.append(row[col])

         
     if all_same(check):
            print(f"player {check[0]} is the  vertically winner!")
            return True
    return False        

def game_board(game_map,player=0,row=0,column=0,just_display=False):
   try:
     if game_map[row][column]!=0:
         print("this postion is ocuppied!choose another!")
         return game_map,False
     print("   0  1  2")
     if not just_display:
        game_map[row][column]=player
     for count, row in enumerate(game_map):
        print(count,row)
     return game_map,True

   except IndexError as e:
       print("Error: make sure you input row/column as 0 1 or 2?",e)
       return  game_map,False
   except Exception as e:
       print("somthing went very wrong!",e)
       return game_map,False
play=True
players=[1,2]
while play:
    game=[[0,0,0],
          [0,0,0],
          [0,0,0],]
    game_won=False
    game , _ =game_board(game,just_display=True)
    player_choise=itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choise)
        print(f"current_player:{current_player}")
        played = False
        while not played:
           column_choise=int(input("what column do you want ot choise?(0,1,2):"))
           row_choise=int(input("what row do you want ot choise?(0,1,2):"))
           game,played=game_board(game,current_player,row_choise,column_choise)

           
        if win(game):
            game_won=True
            again =input("The game is over,would you like to play again?(y/n)")
            if again.lower()=="y":
                print("restarting")
            elif again.lower()=="n":
                print("byeeeee")
                play=False
            else:
                print("Not a valid answer,so...")
                play=False
