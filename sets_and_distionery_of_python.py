# disctionary are unordered and mutable
# disctionary work with "key":"value"
# they dont have index like strings and lists
# disctionary ,lists both are mutable and both can be store nested value like inside list , disctionary,tuple,sets,int,string,boolinen,dobule or float







container = {"name": "Aman",
             "profession":"Data Analysts",
             "education":"graduaction",
             "age": 23,
             "Skills": {
                 "Soft skills": ["Communtication","Leadership","Teamwork","Time Management"],
                 "Technical Skills":["git hub","vs code","my sql","BI Tools"],
                 "Programming languages":["python","java","java Script","css","html","sql"],
                 "BI Tools": "Tableau",
                 "MS office":["Excel","Ms Word","Power Point"]
             }}
 
# print(container)

# print(type(container))

# print(container.keys())

# print(container.values())

# print(container.get("Skills"))

# print(list(container.items()))


more_information = {"Gender":"male",
                    "height":5.5,
                    "belong":"Utter Pradesh",
                    "live":"Delhi"}


container.update(more_information)


# print(container)


# Sets_of_python
# sets and disctionary both are unordered  
# we can add list and disctionary in sets because both are mutable whereas sets are imutable like Tuple 
# one importent point that sets are mutable but their value are imutable
# Sets always cantain or store unique vales like disctionary
# if we store duplicate value in sets will not show error but they show unique value

# sets contains hashable value and imutable


# creating sets 

collection = {2,3,5,1,5,35,"aman","Tushar",4.5,}

print(collection)
print(type(collection))


# creating empty sets 


store = set()

print(store)
print(type(store))

# set.add() they add value

store.add(3) 
store.add(4)
store.add(3)
store.add(6)
store.add(2)
store.add(8)

print(store)

# you will notice that sets authometically remove duplicate value in sets


# sets.revome() this function remove value in sets


store.remove(8)
print(store)


# set.clear() this functions  do empties of sets

# set.pop() this function removes value in sets



# sets methods
# 
# set.union(set2)  this methods work combines both value & return new
# set.intersection(set2)  this methods work combines common value & return new


#  both methods work like venn diegramme


step1 = {1,34,5,6}
step2 = {1,3,6,54,7,6}


print(step1.union(step2))


print(step1.intersection(step2))

             
             
