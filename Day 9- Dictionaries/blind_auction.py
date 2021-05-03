 
 
gameOver  = False

bidders = {}
while not gameOver:

     
    name=input("enter your name ")
    bid_money = int(input("enter your bid amount "))
    bidders[name] = bid_money
    choice =  input("is there any person.Enter Yes or No ").lower()

    if choice=="no":
       
      gameOver = True
      # the key whose value is the largest
      key2 = max(bidders, key = lambda k: bidders[k])

      print("The key with the largest value: ", key2)     

       
      print("The largest value: ", bidders[key2])     



print(bidders)