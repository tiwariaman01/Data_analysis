#  function is block of code in programming language which work when it's called
# function is very importent in programming it's play vital rols to stop and aovid redundentcy.
# redendent is process of happining in various times and redendentcy is very bad in programming.
# therefore , we use function 


# in python , the syntex of function code is like 

# def function_name(Parameter_1,parameter_2):
     
#      some work
     
#      return value



# sytex of call funtion in programme .

#    function_name(argument_1,argument_2)  



# for instence, in our progamme , 
# we need to multiply our variable 
# countinuosly then we can use or make function for maltipication



# def multification(a,b):
#     multi = a * b 
#     print(multi)
#     return multi



# multification(4,8)

# multification(8,9)

# multification(2,4)


# here you will see that we make function with parameter and afterthat , 
# we just called fuction and put argument in function and we don't need to multiply each aragument individualy



# lets make avarge function 

def avarage(a,b,c,d):
    sum = a+b+c+d
    
    avg = sum/4
    print(avg)
    return avg


# avarage(3,6,8,8)

# let's find avg of mark
 
# avarage(98,89,99,87)



# function in python : there two type function 

# 1 Built_in function like : prin(),len(),type(),input() and so on  , logic automatically defined by python

# 2 user defined function : this fuction user mean we create as per our need, we nee to defined logic





movies = ['welcome beck', 'Rockstar','jawan','shershah','Delhi wally','pantom','aman','pan singh tomar','Dhobi ghat','guns of goon']


sports = ('Cricket', 'Football','Hockey','Teniess','aman','badmentel')


def interst(list):
    print(len(list))
    
    


def subject(topic):
    for item in topic:
        
     print(topic,end="/n" )
        
        
        
       
       
# subject(movies)


# subject(sports)      


interst(sports)


def factorial(n ):
    fact = 1
    
    for i in range(1,n+1):
        fact *= i
    print(fact)    


n = int(input("write the number:"))
factorial(n)


def inr_change(usd):
    inr = 83 * usd
    return inr


USD = int(input("inter the $ for change in INR:"))
inr = inr_change(USD)

print("RS:",inr)