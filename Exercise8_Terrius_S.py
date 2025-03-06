# Login data
userName = "admin"
passWord = "pass1234"

# Price
apple = 5
orange = 6
banana = 3.5
mango = 10
strawberry = 7
pineApple = 14
grapes = 2.25
watermelon = 20

checkUserName = input("Please input your username: ")
checkPassWord = input("Please input your password: ")

if (checkUserName == userName):
    if (checkPassWord == passWord):
        print("Access Grant!")
    else:
        print("Wrong Password!")
        quit()
else:
    print("Wrong Username!")
    quit()
    
print("         Welcome to our shop!")
print("--------------------------------------")
print("1. Apple        X1  :   5 THB")
print("2. Orange       X1  :   6 THB")
print("3. Banana       X1  :   3.5 THB")
print("4. Mango        X1  :   10 THB")
print("5. Strawberry   X1  :   7 THB")
print("6. PineApple    X1  :   14 THB")
print("7. Grapes       X1  :   2.25 THB")
print("8. Watermelon   X1  :   20 THB")
print("--------------------------------------")

customerReq = input("What do you want to buy?: ")
amount = int(input("How many do you want to buy?: "))

if (customerReq.lower() == 'apple' or customerReq == '1'):
    price = 5
elif (customerReq.lower() == 'orange' or customerReq == '2'):
    price = 6
elif (customerReq.lower() == 'banana' or customerReq == '3'):
    price = 3.5
elif (customerReq.lower() == 'mango' or customerReq == '4'):
    price = 10
elif (customerReq.lower() == 'strawberry' or customerReq == '5'):
    price = 7
elif (customerReq.lower() == 'pineApple' or customerReq == '6'):
    price = 14
elif (customerReq.lower() == 'grapes' or customerReq == '7'):
    price = 2.25
elif (customerReq.lower() == 'watermelon' or customerReq == '8'):
    price = 20

print(customerReq.upper(), "Amount:", amount, "Total:", price * amount, "THB")