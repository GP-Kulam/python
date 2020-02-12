import math 
  
def isPerfectSquare(x):  
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0)

def threesquares(n):
    
    if(n<0):
        return False
    elif(isPerfectSquare(n)):
        return True
    elif(n<7):
        return True
    else:
        
        while(True):
            for i in range(int(n/2)):
                for j in range(int(n/7)):
                    if(n is (4**i)*(8*j+7)):
                        return False
                    
            if(i==int(n/2)-1):
                return True
                        
                            
        
        

while(True):
    n = int(input("Enter number : "))
    print(threesquares(n))
