while True:
        def k(input):
         try:
          n=int(input)
          for x in range(n):
           n = n+x
           num=[n]
          print(sum(num))
         except ValueError:
          print("Idiot,enter a number!!!!")

        n=input("Enter the Last Number ")
        k(n)













