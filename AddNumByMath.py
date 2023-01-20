def check_user_input(input):
    try:
        n=int(input)
        print(n/2 * (n+1))
    except ValueError:
        print("Idiot,enter a number!!!!")

n=input("Enter the Last Number ")
check_user_input(n)







