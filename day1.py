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

# question given on lisa
# Exercise 1: Mailing Address
name = "prasad sir"
street_address = "123 Main Street, taj hotel 4B"
city_state_zip = "uk, CA 90210"
country = "mars"

print(name)
print(street_address)
print(city_state_zip)
print(country)

# OR, using a single print statement:
print(f"{name}\n{street_address}\n{city_state_zip}\n{country}")