import telebot
import time
import ccxt
import pandas as pd
from ta.momentum import RSIIndicator

# Substitua 'TOKEN_AQUI' pelo seu token real
TOKEN = 'TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# Substitua 'SEU_CHAT_ID' pelo ID do seu chat
chat_id = 'SEU_CHAT_ID'

# Lista de pares de criptomoedas que você deseja monitorar
crypto_pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'DOGE/USDT', 'ADA/USDT', 'BNB/USDT', 'XRP/USDT', 'LTC/USDT']

def calculate_rsi(data, period=12):
    indicator = RSIIndicator(close=data['close'], window=period)
    rsi_values = indicator.rsi()
    return rsi_values

def check_rsi():
    while True:
        for crypto_pair in crypto_pairs:
            exchange = ccxt.binance()  # Use your desired exchange
            ohlcv = exchange.fetch_ohlcv(crypto_pair, timeframe='1h', limit=100)

            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)

            rsi_values = calculate_rsi(df)
            current_rsi = round(rsi_values.iloc[-1], 1)

            print(f"{crypto_pair} RSI: {current_rsi}")

            if current_rsi < 30:
                bot.send_message(chat_id, f"Alerta: {crypto_pair} RSI é {current_rsi}! SOBREVENDA.")
            elif current_rsi > 70:
                bot.send_message(chat_id, f"Alerta: {crypto_pair} RSI é {current_rsi}! SOBRECOMPRA.")

        time.sleep(600)  # Verifica a cada 10 minutos (ajuste conforme necessário)

# Inicia a verificação do RSI em uma thread separada
import threading
thread_rsi = threading.Thread(target=check_rsi)
thread_rsi.start()

# Restante do código (handlers, etc.)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Quando o RSI estiver abaixo de 30 (sobrevenda) ou acima de 70 (sobrecompra), enviarei um alerta, Oss.")

@bot.message_handler(commands=['get_chat_id'])
def get_chat_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"O ID deste chat é {chat_id}")

@bot.message_handler(commands=['criador'])
def criador(message):
    bot.reply_to(message, f"O criador deste chat é o Caetano, the Legend")

# Inicia o bot
bot.polling()
