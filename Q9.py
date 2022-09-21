secret_num = 5
i=0
print('*****Guess the number between 1-10*****')

while i<3:
    #active=True
    guess=int(input("Guess:"))    
    i+=1
    while i<=2:
        if secret_num<guess:
            print(f'hint:It is less than {guess}')
        elif secret_num>guess:
            print(f'hint:It is greater than {guess}')
        break    
    if guess==secret_num:
        print('You Won!')
        break
    
else:
   #active=False
   print('You Failed')

