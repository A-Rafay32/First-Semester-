print('TicTacToe'.center(40,'*'))
def instructions():
    print("""  ******Instrutions******* 
          
          1 | 2 | 3
          --+--+--
          4 | 5 | 6
          --+--+--
          7 | 8 | 9
          """)
    print('>>input numbers to insert your mark corresponding to the positions in grid ')
    print('>>press \'q\' to quit' )
    print('>>press \'r\' to restart')
    print('>>press \'i\' to get intructions')  
board={
    '1':'','2':'','3':'',
    '4':'','5':'','6':'',
    '7':'','8':'','9':''
}

def displayboard(board):
    print(board['1'] +'|'.rjust(3) + board['2'] + '|'.rjust(3) +board['3'])
    print('--+--+--')
    print(board['4'] + '|'.rjust(3) + board['5'] + '|'.rjust(3) + board['6'])
    print('--+--+--')
    print(board['7'] + '|'.rjust(3) + board['8'] + '|'.rjust(3) + board['9'])


def game_engine(board):
  
    turn='X'
    try :
        for i in range(9):
           displayboard(board)
           print(f'move {turn} to which place?')
           #global move ; 
           move=input()
           if move=='i':
              instructions()
           if move=='q':
               break
           
           if board[move]=='':
               board[move]=turn
                
           else:
               print('this place is already filled!')
        
           
           
           if i>=4:
               if board['1']==board['2']==board['3']!='':
                   displayboard(board)
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['4']==board['5']==board['6']!='':
                   displayboard(board)
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['7']==board['8']==board['9']!='':
                  displayboard(board)     
                  print(f'player {turn} has won'.center(40,'*'))
                  break
               elif board['1']==board['4']==board['7']!='':
                   displayboard(board)
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['2']==board['5']==board['8']!='':                   
                   displayboard(board) 
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['3']==board['6']==board['9']!='':  
                   displayboard(board)
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['2']==board['5']==board['8']!='':
                   displayboard(board)
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['1']==board['5']==board['9']!='':
                   displayboard(board)
                   print(f'player {turn} has won'.center(40,'*'))
                   break
               elif board['3']==board['5']==board['7']!='':
                   displayboard(board) 
                   print(f'player {turn} has won'.center(40,'*'))
                   break
           if i>=8:
               print('Tie'.center(30,'*'))
               break
                          
           if turn=='X':
               turn='O'
           else:
               turn='X'
    except KeyError:
           print('please input numbers from 1-9')
game_engine(board)


restart=''
while restart!='q' :
    restart=input(' Do you want to play again?').upper() 
    if restart=='Y':
         board2={str(num):''for num in range(1,10)}
         game_engine(board2)
    else:
         break
 
                            

       
       