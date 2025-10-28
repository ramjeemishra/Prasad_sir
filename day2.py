#this looks like variable but its an object
name_of_var = 13
print(name_of_var,id(name_of_var))
name_of_var = 69
print(name_of_var,id(name_of_var))




x = 7
print(x,id(x))
y =x
print(y+1,id(y))





#object referance
new_name = "ram"
print(new_name,id(new_name))
old_name = new_name
print(new_name,id(new_name), old_name, id(old_name))




#if statement
age = 18

if age >= 18:
    print("u can vote")




#authenticate useer
saved_name = input("enter a username: ")
saved_pass = input("enter a password: ")
print("\naccount created")
user_name = input("enter ur username: ")
user_pass = input("enter ur password: ")
if user_name == saved_name and user_pass == saved_pass:
    print(" u have logged in successfully!")
else:
    print(" invalid username or password.")



