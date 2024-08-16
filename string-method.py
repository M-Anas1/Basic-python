# Basic string method 

Name:str ="M Anas"
#upper case
print(Name.upper(),": Upper case") 
#lower case 
print (Name.lower(),": Lower case")
#cpital case 
print (Name.capitalize(),": Capital case")
#title case
print(Name.title(),": Title case")

# string concatinatin in python 
# Method no 1
Fname :str = "Hassan"
Sname :str = " Ali "

Fullname :str = Fname + Sname
print (Fullname)

# Method no 2
name1 :str = "Ahmar"
name2 :str = " Ali "

Total_name :str = f"{name1} {name2}"
print(Total_name)


# String spacing method 
# Method no 1
print("Abdul"+"   "+"Basit")

# Method no 2 (seprate method )
print( "Muhammad", "Atif", sep=" - ")

# Method no 3 (End method )
print ("Mr",end=" - ")
print ("Anas")




