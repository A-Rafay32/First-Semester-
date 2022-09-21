def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%100==0 and year%400!=0:
      return leap
    if year%100!=0 and year%400!=0:
      return leap  
    else :
      return True     
year = int(input())
print(is_leap(year))