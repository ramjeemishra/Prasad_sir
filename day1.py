# printing hello world
print("hello world")


# printing using "sep"
print("A", "B", "C", sep="-")


#printing using "end"
print("Loading", end="...")
print("Done!")



#creating an file and writing content in it
print("hello world", file=open("file.txt", "w"))


#getting name and age and printing them 
name = input("enter ur name:-")
age = int(input("enter ur age:-"))
print("your name is:-",name, "ur age is:-",age)

