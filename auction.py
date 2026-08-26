name = input("Enter your name: ")
price = int(input("Enter the starting price of the item: $ "))  

bid = {name: price}

continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': \n")

while continue_bidding == 'yes':
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $ "))
    bid[name] = price
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': \n")

highest_bidder = max(bid, key=bid.get)
highest_bid = bid[highest_bidder]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

    
