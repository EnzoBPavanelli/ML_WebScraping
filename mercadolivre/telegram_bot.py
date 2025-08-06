import requests

# Substitua pelo seu token do bot e seu ID de chat
TOKEN = "7753035599:AAFPRQ-fI-7uRxwy8P_P_zdNDQFFkP_s5Fc"
CHAT_ID = "8140693630"

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