# GAME 1
def TicTacToe():
    print('TicTacToe'.center(40,'*'))
    def instructions():
        print("""  ******Instrutions******* 
              
              1 | 2 | 3
              --+---+--
              4 | 5 | 6
              --+---+--
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

 
                            

        
                
# GAME 2
def hangman():
    import random
    print('\n---------------- HANGMAN ----------------')
    words = [
        "Algorithm", "Argument", "Array", "Autonomous", "Coding", "Function",
        "Linux", "Python", "Script", "Statement", "Module", "Expression",
        "Datatype", "Program", "software", "Windows", "Google"
    ]
    word = random.choice(words)
    guesses = ""
    allowed_errors = 7
    done = False

    while not done:
        print("\n")
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")       
            else:
                print("_", end=" ")
        print("\n")
    
        guess = input(f"Allowed errors left {allowed_errors}, Next guess: ")
        guesses += guess
        if guess.lower() not in word.lower():
            allowed_errors -= 1
        if allowed_errors == 0:
                break
    
        done = True

        for letter in word:
            if letter.lower() not in guesses:      
                done = False
                
    if done:
        print(f"\nYou found the word, it was {word} \n")
    else:
        print(f"Game Over! The word was {word} \n")

    restart = input("Do you want to play again?(Y/N): ").lower()
    if restart == "y":
        hangman()

# GAME 3
def QuizGame():
    print('\n-----------------------------GENERAL KNOWLEDGE QUIZ-----------------------------')
    
    score=0
    answer1=input('What do you mean by word “Android” ------ ? \na) tough animal\nb)fast eagle\nc)human like\nd)Tasty food\n')
    if answer1=='c' or answer1=='human like':
        print('Correct')
        score+=1
        print('Score= ',score)
    else:
        print('Incorrect')
    
    answer2=input('2023 cricket world cup will be hosted by ------- ?\na)England\nb)India\nc)Newzealand\nd)Pakistan\n')
    if answer2=='b' or answer2=='India':
        print('Correct')
        score+=1
        print('Your current score is=',score)
    else:
        print('Incorrect')
    
    answer3=input('The mean radius of the earth is approximately\na)3200km\nb)6400km\nc)9600km\n12800km\n')
    if answer3=='b' or answer3=='6400':
        print('Correct')
        score+=1
        print('Your current score is=',score)
    else:
        print('Incorrect')
    
    answer4=input('Which Muslim scientist wrote first book on Algebra ?\na)Al-khwarizmi\nb)Ibn Sina\nc)Archimides\nd)Euclid\n')
    if answer4=='a' or answer4=='Al-khwarizmi':
        print('Correct')
        score+=1
        print('Your current score is=',score)
    else:
        print('Incorrect')
    
    answer5=input('The author of the Book ” The World As I See It” ?\na)Adam Smith\nb)Balban\nc)Albert Einstein\nd)Homer\n')
    if answer5=='c' or answer5=='Albert Einstein':
        print('Correct')
        score+=1
        print('Your current score is=',score)
    else:
        print('Incorrect')
    
    print('----------------------------------------------\nEND OF QUIZ')
    print('YOUR FINAL SCORE IS', score)
    print('----------------------------------------------')

# GAME 4 
def RockPaperScissor():
    import random
    print('----------------ROCK PAPER SCISSOR----------------')
    print('Winning rules of Rock paper scissor game\n'
    +'Rock vs paper -> Paper Wins\n '
    +'Rock vs scissor->Rock Wins\n'
    +'Paper vs scissor->Scissor wins\n')
    
    while True:
        print('Enter choice\n 1 for Rock,\n 2 for paper, and\n 3 for scissor\n')
    
        choice=int(input("'Users Turn'Enter the no: "))
        while choice>3 or choice<1:
            choice=int(input('Enter Valid choice to execute: '))
    
        if choice==1:
            choice_name='rock'
        elif choice==2:
            choice_name='paper'
        else:
            choice_name='scissor'
        print('Users choice is: ', choice_name)
        print('Now its BOTs Turn: ')
    
        comp_choice=random.randint(1,3)
        while comp_choice==choice:
            comp_choice=random.randint(1,3)
        
        if comp_choice==1:
            comp_choice_name="Rock"
        elif comp_choice==2:
            comp_choice_name='Paper'
        else:
            comp_choice_name="Scissor"
    
        print('Bots choice is ', comp_choice_name)
        print(choice_name + 'V/S' + comp_choice_name)
    
        if (choice==1 and comp_choice==2) or (choice==1 or comp_choice==2):
            print('Paper Wins-> ')
            result='paper'
    
        elif (choice==1 and comp_choice==3) or (choice==3 or comp_choice==1):
            print('Rock wins -> ')
            result='Rock'
    
        else:
            print('Scissor wins->')
            result='scissor'
    
        if result==choice_name:
            print('<<<<<<You win>>>>>>> ')
    
        else:
            print('<<<<<<<<<<Computer Wins:>>>>>>>>>')
    
        answer=input('Want to play again Y/N')
        if answer=='n' or answer=='N':
            break
    print('GoodBye')

available_games = ["TicTacToe", "Hangman", "QuizGame", "RockPaperScissor"]
game_to_play=''
while game_to_play !='q':   
    game_to_play=input(f"Available games are:\n1. {available_games[0]}\n2. {available_games[1]}\n3. {available_games[2]}\n4. {available_games[3]}\nWhich game do you want to play?: ")
    if game_to_play.lower() == "tictactoe" or game_to_play == "1":
        TicTacToe()
    elif game_to_play.lower() == "hangman" or game_to_play == "2":
        hangman()
    elif game_to_play.lower() == "quizgame" or game_to_play.lower() == "quiz game" or game_to_play == "3":
        QuizGame()
    elif game_to_play.lower() == "rockpaperscissor" or game_to_play.lower() == "rock paper scissor" or game_to_play == "4":
        RockPaperScissor()
    elif game_to_play.lower()=='q':
         break    
    else:
        print(f"\n{game_to_play} is not available to play")
        
    
               
    


       
       
    

        

    

