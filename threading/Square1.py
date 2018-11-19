
# pool de threads... programacao monolitica - 
# manual explicativo sobre como implementar. 
#código extraído de: 
### https://www.geeksforgeeks.org/synchronization-pooling-processes-python/


#Pooling between processes

#Let us consider a simple program to find squares of numbers in a given list.

# Python program to find  
# squares of numbers in a given list 
def square(n): 
    return (n*n) 
  
if __name__ == "__main__": 
  
    # input list 
    mylist = [1,2,3,4,5] 
  
    # empty list to store result 
    result = [] 
  
    for num in mylist: 
        result.append(square(num)) 
  
    print(result) 