from IPython.display import clear_output
import random
all_locations = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
chosen_location = []
board = {'a1':" ",'a2':" ",'a3':" ",'b1':" ",'b2':" ",'b3':" ",'c1':" ",'c2':" ",'c3':" "}
choices = ['X','O']

random.choice(choices)

def board_layout():
    print("Dear player below is your board layout")
    print("choose your location accordingly")
    for char in 'abc':
        print("[",end="")
        for num in [1,2,3]:
            print(f' {char}{num}',end=" ")
        print("]")

        
def diplay_board():
    clear_output()
    board_layout()
    print('\n\n')

    # board.add(input_location,symbol)
    for char in 'abc':
        print("[",end="")
        for num in [1,2,3]:
            key = char+str(num)
            if key in board:
                print(f' {board[key]}',end=" ")
            else:
                print(f'  ',end=" ")
            
        print("]")
        
def declare_win():
    #for key, value in board.items():
        if board['a1'] == board['a2'] == board['a3'] == 'X' or \
           board['b1'] == board['b2'] == board['b3'] == 'X' or \
           board['c1'] == board['c2'] == board['c3'] == 'X' or \
           board['a1'] == board['b1'] == board['c1'] == 'X' or \
           board['a2'] == board['b2'] == board['c2'] == 'X' or \
           board['a3'] == board['b3'] == board['c3'] == 'X' or \
           board['a1'] == board['b2'] == board['c3'] == 'X' or \
           board['a3'] == board['b2'] == board['c1'] == 'X' :
            return True
        elif board['a1'] == board['a2'] == board['a3'] == 'O' or \
           board['b1'] == board['b2'] == board['b3'] == 'O' or \
           board['c1'] == board['c2'] == board['c3'] == 'O' or \
           board['a1'] == board['b1'] == board['c1'] == 'O' or \
           board['a2'] == board['b2'] == board['c2'] == 'O' or \
           board['a3'] == board['b3'] == board['c3'] == 'O' or \
           board['a1'] == board['b2'] == board['c3'] == 'O' or \
           board['a3'] == board['b2'] == board['c1'] == 'O' :
            return True
        else:
            return False
    
    
def choose_location(player):
    # allow player to choose location as per board layout
 
    location = input(f'{player} Enter empty location as per board layout : ')
    
    while True:
        if location not in all_locations:
            location = input(f'Dear {player}, your chosen location is not correct\nChoose location again : ')
        elif location in chosen_location:
            location = input(f'Dear {player}, your chosen location is not empty\nChoose location again : ')
        else:
            chosen_location.append(location)
            break
    return location

   
def start_game():
    # Provide detailed info on the Board Layout
    board_layout()
    
    #Get the names of both players
    player1 = input("Player 1 Enter your Name : ")
    player2 = input("Player 2 Enter your Name : ")

    
    
    # Provide basic instruction to both players
    #print(f"\nThanks {player1} and {player2}. Your turn will be called out after every move")
    print(f"{player1} plays 'X' and {player2} plays 'O'")
    
    for count in range(1,10):
        if count%2 != 0:
            location = choose_location(player1)
            board.update({location:'X'})
            diplay_board()
            win = declare_win()
            if(win):
                print(f"{player1} is winner")
                break
        else:
            location = choose_location(player2)
            board.update({location:'O'})
            diplay_board()
            win = declare_win()
            if(win):
                print(f"{player2} is winner")
                break
    else:
        print("Game is Draw")
        
start_game()
