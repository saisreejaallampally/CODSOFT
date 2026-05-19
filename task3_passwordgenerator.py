import string
import random
print("PASSWORD GENERATOR")
def password_generator(length):
    print("Choose the password complexity:")
    print("1.Only Letters")
    print("Letters+Numbers")
    print("Letters+Numbers+Symbols")
    choice=int(input("Enter your Choice:"))
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    print("Password Generated:",end="")
    for i in range(length):
      if choice==1:
            print(random.choice(letters),end="")
      elif choice==2:
        
            print(random.choice(letters+numbers),end="")
      elif choice==3:
        
            print(random.choice(letters+numbers+symbols),end="")
      else:
        print("Wrong choice")   
length=int(input("Enter the length:"))
password_generator(length)