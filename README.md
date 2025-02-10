Bot de RSI para Criptomoedas no Telegram 📈

Desenvolvi um bot em Python para o Telegram que monitora o RSI (Índice de Força Relativa) de diversas criptomoedas em tempo real! Ele envia alertas quando um ativo está sobrevendido (< 30) ou sobrecomprado (> 70), ajudando a identificar possíveis oportunidades no mercado.

🔥 Oportunidade na Sobrevenda?
Quando um ativo está em tendência de alta e o RSI cai abaixo de 30, pode significar pânico momentâneo e abrir uma ótima oportunidade de compra. Já em tendência de baixa, um RSI abaixo de 30 pode indicar que a pressão vendedora ainda não acabou.

💡 Como funciona?

    O bot monitora pares como BTC, ETH, SOL, DOGE, ADA e mais.
    A cada 10 minutos, ele analisa o RSI e envia alertas no Telegram.
    Se o RSI for baixo demais ➝ possível ponto de compra.
    Se for alto demais ➝ pode indicar sobrecompra e risco de correção.

🔧 Tecnologias usadas:
✅ Python + Telebot 🤖
✅ ccxt para dados de mercado 📊
✅ Pandas e TA-Lib para análise técnica 📉
