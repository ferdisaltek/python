def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0:
        if year%100==0:
            if year%4==0:
                return True
    else:
        return  False
        
    

year = int(input())
is_leap (year)

