from os import system, name


cnt=1
move_player=1
p1=''
p2=''
win_flag=0
l_row1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def clear():
    if name == 'nt': 
        _ = system('cls')



def print_board():
    global win_flag
    clear()
    b1='     {} | {} | {} '.format(l_row1[0],l_row1[1],l_row1[2])
    b3='     {} | {} | {} '.format(l_row1[3],l_row1[4],l_row1[5])
    b5='     {} | {} | {} '.format(l_row1[6],l_row1[7],l_row1[8])
    print(b1)
    print('    ---+---+----')
    print(b3)
    print('    ---+---+----')
    print(b5)

def take_player_names():
    print()
    print()
    p1=input('Enter Player1 Name:  ')
    print()
    p2=input('Enter Player2 Name:  ')
    print()
    print()
    start_msg='Lets start the game {} Vs. {}'.format(p1,p2)
    print(start_msg)
    return p1,p2

def end_win(player,symbol):
    global win_flag
    win_msg="Player {} with symbol {} has WON the Match!!".format(player,symbol)
    print()
    print(win_msg)
    win_flag=1

def check_if_win(player,l_row1,symbol):
    if l_row1[:3]== [symbol,symbol,symbol] or l_row1[3:6]== [symbol,symbol,symbol] or l_row1[6:] == [symbol,symbol,symbol] or l_row1[0]+l_row1[3]+l_row1[6]== symbol+symbol+symbol or l_row1[1]+l_row1[4]+l_row1[7]== symbol+symbol+symbol or l_row1[2]+l_row1[5]+l_row1[8]== symbol+symbol+symbol or l_row1[0]+l_row1[4]+l_row1[8]== symbol+symbol+symbol or l_row1[2]+l_row1[4]+l_row1[6]== symbol+symbol+symbol:
        end_win(player,symbol)
    

def perform_move(player,move,symbol):
    if l_row1[int(move)-1] == 'X' or l_row1[int(move)-1] == 'O':
        print('This field is already used ! Please choose another one')
        take_move_from_player(player,symbol)
    l_row1[int(move)-1]=symbol
    print_board()
    check_if_win(player,l_row1,symbol)
    

def take_move_from_player(player,symbol):
        print()
        move_msg='{}, Enter block number:  '.format(player)
        move= input(move_msg)
        perform_move(player,move,symbol)
    

def take_ip_from_p2():
    pass

def start_game(cnt,p1,p2,move_player):
    global win_flag
    while cnt<=10:
        if move_player%2 != 0:
            player=p1
            symbol='X'
        else:
            player=p2
            symbol='O'
            
        move_player=move_player+1
        
        if win_flag==1:
            break
        take_move_from_player(player,symbol)
        cnt=cnt+1
        




if __name__== '__main__':
    
    print_board()
    p1,p2=take_player_names()
    start_game(cnt,p1,p2,move_player)