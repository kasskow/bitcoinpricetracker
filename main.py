import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = res.json()
    price = data['bpi']['USD']['rate']
    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)