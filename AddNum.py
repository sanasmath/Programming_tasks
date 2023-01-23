def k(input):
         try:
          n=int(input)
          for x in range(n):
           n = n+x
           num=[n]
          print(sum(num))
         except ValueError:
          print("Idiot,enter a number!!!!")

while True:
    n=input("Enter the Last Number "" ")
    if n=="f":
        print("Stoped")
        break
    else:
        k(n)












