#  recursion : when function called itself repeatedly

#  in another words , recursion is denger version of loops . where recursion function call themseld repeatdly.

#  loops and recursion both are interelated . so, we can do anything with help of recursion whatever we do with the help of loops.
#  most of the case , we use loop and recursion are used for specfic case.

#  recursion syntex 

def show(n):
    if(n == 0):  #this called  # this if statement write for break the recursion loop,
        return     #  otherwise show(n-1) recursion function continuosly run 0,-1,-2,-3,-4 and so on
    print(n)
    show(n-1)  #this called recusion 
    
    
show(4)    



#  for devloping understanding towards of function and recursion ,like how they work 
# need to understand Called Stack



# let's make recursion for factorial

def cul_factorial(n):
    if(n== 0 or n == 1):
        return 1
    
    else:
        return n * cul_factorial(n -1)
    
    
    
 
number = int(input("inter number :"))  

print(cul_factorial(number))  



#  Factorial make recurence relation , therefore we can write recursion function .




def cul_sum(n):
    if( n == 0):
        return 0
    else:
        return cul_sum(n-1) + n


sum = cul_sum(5)

print(sum)