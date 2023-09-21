''' *if name is less than 3 then print name must be atleast 3 characters  
    *if it's more than 50 chatracters then print name can be maximum of 50 characters
    *else print name looks good'''
# Name - Aditya Kumar
# ID - 22BTCSE067
# Programme - Btech CSE

name = input("Enter Your name: ")
if (len(name) < 3):
    print("! Name must be atleast 3 characters")
elif (len(name) > 50):
    print("! Name can be maximum of 50 characters")
else:
    print("Name looks good!!")  