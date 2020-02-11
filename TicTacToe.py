
print("TIC TAC TOE GAME\n ")

first_row = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
second_row = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
third_row = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
middle_row =["-----------"]


#Displays the board 
def display_board(*args):
    for i in args:
        print("".join(i))

#Play again

pg = "y"

def play_again():
    global pg
    choice = input("\nDo you wan to play again? (y/n) ")
    if(choice == "y"):
        global first_row
        global second_row
        global third_row
        first_row = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
        second_row = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
        third_row = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
        pg = "y"
        play_game()
    if(choice =="n"):
        pg = "n"
        print("\nThankyou for playing!")


#Game win logic
def gameState_win():
    #HORIZONTAL
    if(first_row[1] =="X" and first_row[5] =="X" and first_row[9] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(second_row[1] == "X" and second_row[5] == "X" and second_row[9] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(third_row[1] == "X" and third_row[5]== "X" and third_row[9] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(first_row[1]=="O" and first_row[5]=="O" and first_row[9] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()
    if(second_row[1]=="O" and second_row[5]=="O" and second_row[9] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()
    if(third_row[1]=="O" and third_row[5]=="O" and third_row[9] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()

    #VERTICAL
    if(first_row[1]== "X" and second_row[1]== "X" and third_row[1] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(first_row[5]== "X" and second_row[5]== "X" and third_row[5] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(first_row[9]== "X" and second_row[9]== "X" and third_row[9] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(first_row[1]=="O" and second_row[1]=="O" and third_row[1] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()
    if(first_row[5]=="O" and second_row[5]=="O" and third_row[5] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()
    if(first_row[9]=="O" and second_row[9]=="O" and third_row[9] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()

    #DIAGONAL
    if(first_row[1]== "X" and second_row[5]== "X" and third_row[9] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(third_row[1]== "X" and second_row[5]== "X" and first_row[9] == "X"):
        print("\nPlayer 1 - X wins the game!!")
        play_again()
    if(first_row[1]=="O" and second_row[5]=="O" and third_row[9] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()
    if(third_row[1]=="O" and second_row[5]=="O" and first_row[9] == "O"):
        print("\nPlayer 2 - O wins the game!!")
        play_again()
    
    #TIE

    if((first_row[1] == "X" or first_row[1]== "O") and
       (first_row[5] == "X" or first_row[5]== "O") and
       (first_row[9] == "X" or first_row[9]== "O") and
       (second_row[1] == "X" or second_row[1]== "O") and
       (second_row[5] == "X" or second_row[5]== "O") and
       (second_row[9] == "X" or second_row[9]== "O") and
       (third_row[1] == "X" or third_row[1]== "O") and
       (third_row[5] == "X" or third_row[5]== "O") and
       (third_row[9] == "X" or third_row[9]== "O")):
        print("\nIt's a tie!!")
        play_again()

 

    
      

#Player next position logic
def play_game():
    for i in range(1,10):
      
        
        if(i % 2 == 0):
            row = int(input("\nPlayer two Enter the row position(O) : "))
            column = int(input("Player two Enter the column position(O) : "))
            print("")
            if(row == 1):
                if(column == 1):
                    first_row[1] = "O"
                elif(column == 2):
                    first_row[5] = "O"
                elif(column == 3):
                    first_row[9] = "O"
                
            elif(row == 2):
                if(column == 1):
                    second_row[1] = "O"
                elif(column == 2):
                    second_row[5] = "O"
                elif(column == 3):
                    second_row[9] = "O"
                    
            elif(row == 3):
                if(column == 1):
                    third_row[1] = "O"
                elif(column == 2):
                    third_row[5] = "O"
                elif(column == 3):
                    third_row[9] = "O"
            
                
            display_board(first_row,middle_row,second_row,middle_row,third_row)
            gameState_win()

        if(i%2 != 0):
            row = int(input("\nPlayer one Enter the row position(X) : "))
            column = int(input("Player one Enter the column position(X) : "))
            print("")
            if(row == 1):
                if(column == 1):
                    first_row[1] = "X"
                elif(column == 2):
                    first_row[5] = "X"
                elif(column == 3):
                    first_row[9] = "X"
                
            elif(row == 2):
                if(column == 1):
                    second_row[1] = "X"
                elif(column == 2):
                    second_row[5] = "X"
                elif(column == 3):
                    second_row[9] = "X"
                    
            elif(row == 3):
                if(column == 1):
                    third_row[1] = "X"
                elif(column == 2):
                    third_row[5] = "X"
                elif(column == 3):
                    third_row[9] = "X"
            
            display_board(first_row,middle_row,second_row,middle_row,third_row)
            gameState_win()
        if(pg == "n"):
            break
        

#Displays the blank board            
display_board(first_row,middle_row,second_row,middle_row,third_row)

#Calls the main game logic function
play_game()






 
