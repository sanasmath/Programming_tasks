print("if you want to close it, please press 'f' ")
def k(input):

         try:

          n=int(input)

          print(n/2 * (n+1))
          
         except ValueError:
          print("Idiot Enter a number!!!!")

while True:
    n=input("Enter the Last Number ")
    if n=="f":
        print("stoped!!!!!")
        break
    else:
        k(n)







