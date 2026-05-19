def calculator(a,b):
    op=input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n")
    match op:
        case "1":
            return "Addition",a+b
        case "2":
            return "Subtraction",a-b
        case "3":
            return "Multiplication",a*b
        case "4":
            if b==0:
                return "Cannot be divided by zero"
            else:
                return "Division",a/b
        case "5":
            return "Modulus",a%b
        case _:
            return "invalid choice"
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print(calculator(a,b))
