import ccxt
from datetime import datetime,timedelta  
import pandas as pd
import binance_config
from binance.client import Client
binance=ccxt.binance({
    'apiKey' :binance_config.api,
    'secret' :binance_config.secret
    # 'options':{'defaultType':'future'}
    # 'apikey':'lYQMSCnTPXMa5cONBBpUjnnny9LofxphQHm38agGbi9p93hPGar4bWbTyGXONyJj'
    # 'secret' 'O7tKnXGXMinHyGusVDRnMWlEQQ6ViRPUU9mHCaMRRnf0gleeKA393YlOGdBPD'
})
client=Client(api_key=binance_config.api,api_secret=binance_config.secret)
# order=binance.create_limit_buy_order('BTCUSDT',.01,best_bid)
# od=binance.create_order('BTCUSDT','market','buy',0.001) # worked
# print(od)
# print(binance.fetch_balance)
# print(binance.fetch_bids_asks)
# btc_ticker = binance.fetch_ticker('BTC/USDT') 
# print(btc_ticker)

# orderbook=binance.fetch_order_book('BTC/USDT')
# print(orderbook)

# market=binance.load_markets()
# print(market)
def get_best_bid_ask():

    orderbook=binance.fetch_order_book('BTCUSDT')
    best_bid=orderbook['bids'][0][0]
    best_ask=orderbook['asks'][0][0] 
    bal=binance.fetch_balance
    print(f'the best bid is: {best_bid} and the best ask is {best_ask}')

    return best_bid,best_ask

print(get_best_bid_ask())
# params={'positionSide':'SHORT'}
# order=binance.create_order('BTC/USDT','market','buy',.001,params)
# print(order)
# print(binance.fetch_balance())
def order_book():
    binance_order=binance.fetch_order_book('BTCUSDT')
    binance_bids=binance_order['bids'][0][0]
    binance_asks=binance_order['asks'][0][0]

    # print(f'The best bid is {binance_bids} and the best asks is {binance_asks}')
    bal=client.futures_account_balance()
    # print(bal)

    # order=binance.create_order('BTCUSDT','market','BUY',.01)
    # print(order)
    # print(binance.fetch_balance())
   

# print(order_book())
# balance=client.get_asset_balance('USDT')
# print(balance)

# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)
# print(binance.fetch_balance())




symbol = 'BTCUSDT'
order_type = client.ORDER_TYPE_MARKET
side = client.SIDE_SELL
quantity = .002
leverage = 50
# tick=client.futures_ticker()
# print(tick)
# ticke=client.futures_symbol_ticker()
# print(ticke)
# s=client.futures_exchange_info()
# print(s)
# symbols = [symbol['symbol'] for symbol in s['symbols'] if symbol['contractType'] == 'CURRENT_QUARTER']
# print(symbols)
# position_side = 'L'
def convert_to_ist(unix_timestamp):
    utc_time = datetime.utcfromtimestamp(unix_timestamp / 1000)  # Convert to seconds and UTC datetime
    ist_time = utc_time + timedelta(hours=5, minutes=30)        # Add 5 hours and 30 minutes for IST
    return ist_time

ohlc=binance.fetch_ohlcv("BTCUSDT",'15m')
#print(ohlc)
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(ohlc, columns=columns)

df['timestamp'] = df['timestamp'].apply(convert_to_ist)
print(df)
order = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=order_type,
    quantity=quantity,
    leverage=leverage
    
)

print("order trying to place") 
print(order)

# contract_order_book=client.futures_order_book(symbol='BTCUSDT')
# # print(contract_order_book)
# bids=contract_order_book['bids'][0][1]
# asks=contract_order_book['asks'][0][1]
# print(bids,asks)
# df=pd.DataFrame(contract_order_book,columns=['bids','asks'])
# print(df)
# symbol = 'BTCUSDT'
# fees = binance.load_fees()

# maker_fee = fees['trading'][symbol]['maker']
# taker_fee = fees['trading'][symbol]['taker']

# print(f"Maker fee for {symbol}: {maker_fee}")
# print(f"Taker fee for {symbol}: {taker_fee}")
# cancel=client.futures_cancel_all_open_orders(symbol='BTCUSDT')
# print(cancel)
# order_sell = client.futures_create_order(
#     symbol='BTCUSDT',
#     side='SELL',
#     type='MARKET',
#     price=0,
#     timeInForce='IOC',
#     quantity=quantity,
    
# )
# print(order_sell)
