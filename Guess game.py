secret_num = 5
i=0
while i<3:
    active=True
    guess=int(input("Guess:"))    
    i+=1
    if guess==secret_num:
        print('You Won!')
        break
else:
   active=False
   print('You Failed')
    
    