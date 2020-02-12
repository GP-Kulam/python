def printDistinct(n, arr): 
    s=[]
    
    for i in range(0, n): 
  
        
        d = 0
        for j in range(0, i): 
            if (arr[i] == arr[j]): 
                d = 1
                break
  
        
        if (d == 0): 
            s.append(arr[i])
    return s 

def sockMerchant(n, ar):
    
    s=[]
    s=printDistinct(n,ar)
    ar_count=0
    for x in s:
        count=0
        for i in range(0,n):
            if(x==ar[i]):
                count+=1
      
        ar_count+=int(count/2)
 
    return ar_count


    


if __name__ == "__main__":
    ar=[1,1,3,3,4,2,2,4,4,4]
    n=10
    print(sockMerchant(n,ar))
      
