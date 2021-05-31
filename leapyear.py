
#Leap Year program 

def test(year):
    
    ##If divisible by 4
    if (year % 4) == 0:
        ##If divisible by 100
        if (year % 100) == 0:
            #If divisible by 400
            if (year % 400) == 0:
                return True
            else:
                return False     
        else:
            return True
    else:
        return False 


