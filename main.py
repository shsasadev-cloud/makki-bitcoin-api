from fastapi import FastAPI
import requests
import json
from datetime import datetime

app = FastAPI()

@app.get('/')
def read_root():
    try:
        # Get Bitcoin price from CoinGecko
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        data = response.json()
        price = data['bitcoin']['usd']
        
        # Log to file
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'price': price
        }
        with open('btc_log.json', 'a') as f:
            f.write(json.dumps(log_entry) + '
')
            
        return {'bitcoin_price_usd': price, 'status': 'success'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}
