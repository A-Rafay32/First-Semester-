from itertools import permutations    
def prime(num):
    condition = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                condition = True
                break    

    s=str(num)
   
    if len(s)>=2:
        perm=permutations(s)
        for i in perm:
          num=int(''.join(i))
   
    if condition is True:
        print(num,num,"\nIt is not a circular prime number")
    else:
         print(num,num, "\nIt is a circular prime number") 
num=int(input('number:'))         
prime(num)
        

        
    
    
      
