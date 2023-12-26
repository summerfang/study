from futu import *

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # Create quote object
print(quote_ctx.get_market_snapshot('HK.00700'))  # Get market snapshot for HK.00700
quote_ctx.close() # Close object to prevent the number of connextions from running out


trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)  # Create trade object
print(trd_ctx.place_order(price=500.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE))  # Placing an order through paper trading account (It is nessary to unlock trade by trading password for placing orders in the real environment.)

trd_ctx.close()  # Close object to prevent the number of connextions from running out