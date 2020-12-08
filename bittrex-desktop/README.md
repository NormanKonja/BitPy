# Bittrex-Desktop


Main File with all logic is in bittrex-desktop.py you will need to install python bittrex to run the program.
I have included python bittrex in the  main folder to install go to the directory in the command line and type

```python setup.py install```


The only configuration needed is in the Bittrex-Desktop.py file

In line 3 chnage
```
my_bittrex = Bittrex(None, None)  
```
to
```
my_bittrex = Bittrex("<my_api_key>", "<my_api_secret>")
```
and your go to go after that.

Just open the dektop-bittrex file and inputs are simple!
Options: Buy, Sell, Price, Balace
```
Your input :  '<order_type>' '<amount>' '<currecy_ticker>' 'at' '<price>' '<price_currency>'
```
order_types = buy/sell

amount = amount you want to buy or sell

currency_ticker = ticker (bitcoin's ticker is BTC) of any currecy on bittrex...

price = price to pay per coin// You may also use 'last','bid', or 'ask' for the most recent last, bid , and ask prices

*When using last, bid, or ask as the price you do not need to add in the price_currency as it will always be the same price*

price_currency = 'SAT' for satoshi or 'USD' for usdollars

To get price type

'price ETH'
'price XLM' returns Last price of xlm

Get your balance

'balance Eth'

'balance xlm' return your xlm balance

Example Buy: buy 100 XLM at 0.00000010 SAT

Example Sell: sell 100 XLM at 0.20 USD

Example Pricing: Price XLM

You may also buy and sell at 'last', 'ask', or 'bid' prices!

Example Live Prices: 'Buy 50 VTC at last' buys at the current price of vertcoin

Example Live Prices: 'Buy 50 VTC at bid' buys at the bid price of vertcoin

To check balances use 'balance <coin ticker>'
  
Example Balanace: 'balance ETH' returns your ethereum balance
