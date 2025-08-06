import requests

# Substitua pelo seu token do bot e seu ID de chat
TOKEN = "COLE SEU TOKEN AQUI"
CHAT_ID = "COLE SEU CHAT ID AQUI"

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    try:
        r = requests.post(url, data=data)
        if r.status_code != 200:
            print(f"❌ Erro Telegram: {r.text}")
    except Exception as e:

        print(f"❌ Falha no envio: {e}")
