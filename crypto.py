import requests

COINMARKETCAP_API_KEY = 'COINMARKETCAP_API_KEY'

def get_crypto_price(crypto_ticker: str) -> str:
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': crypto_ticker,
        'convert': 'EUR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        if 'data' in data and crypto_ticker.upper() in data['data']:
            price = data['data'][crypto_ticker.upper()]['quote']['EUR']['price']
            return f"{crypto_ticker.upper()} price is ${price:.2f}"
        else:
            return "Invalid cryptocurrency ticker or no data available."
    except Exception as e:
        return f"Error fetching data: {e}"
