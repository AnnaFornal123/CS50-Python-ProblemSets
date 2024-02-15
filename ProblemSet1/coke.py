"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and 
only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, 
implement a program that prompts the user to insert a coin,
 one at a time, 
 each time informing the user of the amount due. 
 Once the user has inputted at least 50 cents, 
 output how many cents in change the user is owed.
 Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

Amount due: 50
  Insert Coin: 25                                                                 

"""

def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin_inserted = input("Insert coins... ")
        if is_coin(coin_inserted):
            coin = int(coin_inserted)
            if is_valid_coin(coin):
                amount_due -= coin
                print(str(amount_due))
            
    else:
        print(f"Change owed: " + str(0 - amount_due))


def is_coin(coin):
        try:
            int(coin)
        except:
            print("It's not a coin, try again")        
            return False
        else:
            return True 
  
def is_valid_coin(coin):
    match coin:
        case 5 | 10 | 25:
            return True
        case _:
            print("This is not a correct coin, try again")
            return False


main()
