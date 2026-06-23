from password_generater import generate_password 
from password_checker import rate_password 

def user():
    print('=================================================================================')
    print("hello user do you wanna creat password or check your password strenght : ")
    print("1.creat passwor")
    print("2.check your password strenght")
    print("3.Exist")
    print('=================================================================================')
while True :
    user()
    
    try :
        choice = int(input("choose number : "))
        if choice == 1 :
            try : 
                lenght = int(input("entre your password lenght : "))
                p = generate_password(lenght)
                print(f'your password is : {p}')
                choice = input("press e to exit : ")
                if choice.lower() == "e" :
                    break
            except TypeError :
                print('you must entre number!!!!!!')
        elif choice == 2 :
            p = input("please entre your password to check : ")
            rate_password(p)
            
        elif choice == 3 :
            print("goodBye")
            break
        else :
            print("please choose numbre between 1 and 3 ")
    except ValueError :
        print("please entre a number!!!!!!")

        