'''
25 cents, 10 cents, and 5 cents.
Amount Due: 5                                                                   
Insert Coin: 10                                                                 
Change Owed: 5                                                                  
$               
'''
#list
coins = [25, 10, 5]
#creat function
def main():
    coin = int(input("Insert Coin: "))
    #write calculator
    amount = 50 - coin
    while True:
        #code when amount > 0
        if coin in coins and amount > 0 :
            print("Amount Due:", amount)
        # code for amount = 0
        elif coin in coins and amount == 0:
            print("Change Owed: 0")
            break
        #code for amount <0
        elif coin in coins and amount < 0:
            n_amount = amount * -1
            print("Change Owed:", n_amount)
            break
        #when coin is not 10, 25, 5
        elif coin not in coins:
            print("Amount Due: 50")
            break
        coin = int(input("Insert Coin: "))
        amount -= coin
main()
