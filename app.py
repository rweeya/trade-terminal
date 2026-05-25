from flask import Flask, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/signals')
def get_signals():
    try:
        # Пробуем получить сигналы с твоего старого сервера
        response = requests.get('https://ai-trade-machine.onrender.com/api/signals', timeout=10)
        return jsonify(response.json())
    except:
        # Если сервер не отвечает — возвращаем тестовые данные
        test_signals = [
            {"symbol": "BTC/USDT", "action": "buy", "price": 68500, "rsi": 32, "timestamp": "2026-05-25T10:00:00", "reason": "RSI перепродан"},
            {"symbol": "ETH/USDT", "action": "sell", "price": 3450, "rsi": 72, "timestamp": "2026-05-25T09:30:00", "reason": "RSI перекуплен"},
            {"symbol": "SOL/USDT", "action": "buy", "price": 165, "rsi": 28, "timestamp": "2026-05-25T09:00:00", "reason": "Стохастик на дне"}
        ]
        return jsonify(test_signals)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
