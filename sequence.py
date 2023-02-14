first_num,second_num,third_num=4,0,0
counter=0
print(first_num) 
while counter<=20:  
    operation=first_num**2 + second_num**2 + third_num**2
    s=str(operation)
    
    if len(s)==1:
        first_num=int(s[:])
    if len(s)==2:
       third_num=0 
       first_num,second_num=int(s[0]),int(s[1])    
    elif len(s)==3:
       first_num,second_num,third_num=int(s[0]),int(s[1]),int(s[2])
       
    print(operation)    
    counter+=1    
    
