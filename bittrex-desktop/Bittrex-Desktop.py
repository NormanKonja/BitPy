from bittrex.bittrex import Bittrex, API_V2_0

my_bittrex = Bittrex(None, None)  # Bittrex("<my_api_key>", "<my_api_secret>")
        #print(1/my_bittrex.get_ticker("USDT-BTC")["result"]["Last"]) 1 USD

x="Options: Buy Sell Price Balances\nExample Buy: buy 100 XLM at 0.00000010 SAT\nExample Sell: sell 100 XLM at 0.20 USD\nExample Pricing: Price XLM\nYou may also buy and sell at 'last', 'ask', or 'bid' prices!\n'Buy 50 VTC at last' buys at the current price of vertcoin\nTo check balances use 'balance <coin ticker>' EX: 'balance ETH'\nInput: "
def ErrorMessage():
    print("Please enter a valid Input")
    new = input(x)
    MakeTransaction(new)

def tryme(trying):
    try:
        if trying["success"] == False:
            print("Order Failed " + trying["message"])
        else:
            if input("Your order has been created! Enter Y to make another order:").lower() =="y":
                MakeTransaction(input("Place Order Here: "))
    except:
        ErrorMessage()

def MakeTransaction(details):
    #split input to get order details
    words = details.split(" ")

    #Deleting extra spaces
    for i, v in enumerate(words):
        if v == " ":
            del words[i]
        words[i]=words[i].lower()

    #Getting options
    if words[0] == "buy":
        #checking for correct input
        try:
            words[1] = int(words[1])
            words[2] = words[2].upper()
            float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Last"])
            if words[4] == "last":
                tryme(my_bittrex.buy_limit( "BTC-"+words[2], words[1], float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Last"])))
            elif words[4] == "ask":
                tryme(my_bittrex.buy_limit( "BTC-"+words[2], words[1], float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Ask"])))
            elif words[4] == "bid":
                tryme(my_bittrex.buy_limit( "BTC-"+words[2], words[1], float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Bid"])))
            else:
                words[4] == float(words[4])
                if words[5].upper == "SAT":
                    tryme(my_bittrex.buy_limit( "BTC-"+words[2], words[1], words[4]))#placing buy#
                elif words[5].upper == "USD":
                    tryme(my_bittrex.buy_limit( "BTC-"+words[2], words[1], float(1/my_bittrex.get_ticker("USDT-BTC")["result"]["Last"])*words[4]))
                else:
                    ErrorMessage()
        except:
            print("You did not put an Integer in the amount you want to purchase!")
            ErrorMessage()
    elif words[0] == "sell":
        #checking for correct input
        try:
            words[1] = int(words[1])
            words[2] = words[2].upper()
            float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Last"])
            if words[4] == "last":
                tryme(my_bittrex.sell_limit( "BTC-"+words[2], words[1], float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Last"])))
            elif words[4] == "ask":
                tryme(my_bittrex.sell_limit( "BTC-"+words[2], words[1], float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Ask"])))
            elif words[4] == "bid":
                tryme(my_bittrex.sell_limit( "BTC-"+words[2], words[1], float(my_bittrex.get_ticker("BTC-"+words[2])["result"]["Bid"])))
            else:
                words[4] == float(words[4])
                if words[5].upper == "SAT":
                    tryme(my_bittrex.sell_limit( "BTC-"+words[2], words[1], words[4]))
                elif words[5].upper == "USD":
                    tryme(my_bittrex.sell_limit( "BTC-"+words[2], words[1], float(1/my_bittrex.get_ticker("USDT-BTC")["result"]["Last"])*words[4]))
                else:
                    ErrorMessage()
        except:
            print("You did not put an Integer in the amount you want to purchase!")
            ErrorMessage()
    elif words[0] == "price":
        words[1] = words[1].upper()
        if words[1] == "BTC":
            if my_bittrex.get_ticker("BTC-"+words[1])["success"] == True:
                f = float(my_bittrex.get_ticker("USDT-"+words[1])["result"]["Last"]/(1/my_bittrex.get_ticker("USDT-BTC")["result"]["Last"]))
                print(str(f)+" USD")
                MakeTransaction(input(x))
            else:
                print("Not a valid currency ticker")
                ErrorMessage()
        else:
            if my_bittrex.get_ticker("BTC-"+words[1])["success"] == True:
                print(str(my_bittrex.get_ticker("BTC-"+words[1])["result"]["Last"])+" SAT")
                f = float(my_bittrex.get_ticker("BTC-"+words[1])["result"]["Last"]/(1/my_bittrex.get_ticker("USDT-BTC")["result"]["Last"]))
                print(str(f)+" USD")
                MakeTransaction(input(x))
            else:
                print("Not a valid currency ticker")
                ErrorMessage()
    elif words[0] == "balance":
        if my_bittrex.get_balance(words[1])["success"] == True:
            print(my_bittrex.get_balance(words[1])+" SAT")
            print(my_bittrex.get_balance(words[1])/(1/my_bittrex.get_ticker("USDT-BTC")["result"]["Last"]) + " USD")
            MakeTransaction(input(x))
        else:
            print("Bad ticker")
            ErrorMessage()
    else:
        ErrorMessage()



MakeTransaction(input(x))
