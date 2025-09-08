import logging
from binance.client import Client
from binance.enums import *

# Configure logging (fixed for local system)
logging.basicConfig(filename='trading_bot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = 'https://testnet.binancefuture.com/fapi/v1'

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_STOP_MARKET,
                    stopPrice=stop_price,
                    quantity=quantity
                )
            else:
                logging.error(f"Unsupported order type: {order_type}")
                print("Unsupported order type.")
                return

            logging.info(f"Order placed: {order}")
            print("Order Successful:", order)
        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")
            print(f"Error: {str(e)}")

def main():
    api_key = input("Enter your API key: ").strip()
    api_secret = input("Enter your API secret: ").strip()

    bot = BasicBot(api_key, api_secret)

    print("\n=== Binance Futures Testnet Trading Bot ===")
    symbol = input("Enter trading pair symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Order Side (BUY/SELL): ").strip().upper()
    order_type = input("Order Type (MARKET/LIMIT/STOP_MARKET): ").strip().upper()
    quantity = float(input("Quantity: ").strip())

    price = None
    stop_price = None

    if order_type == 'LIMIT':
        price = input("Enter Limit Price: ").strip()
    if order_type == 'STOP_MARKET':
        stop_price = input("Enter Stop Price: ").strip()

    bot.place_order(symbol, side, order_type, quantity, price, stop_price)

if __name__ == "__main__":
    main()
