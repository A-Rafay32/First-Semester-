def list_rotation():
    
    rotated_list=list1[x:]+list1[0:x]
    print(rotated_list)
    
x=int(input('By how many elements you want the list to be rotated?'))
list1=[1,2,3,4,5,6]
print(f'list rotated by {x} elements is:')

list_rotation()    
        
        
        

        

    

