import requests
from bs4 import BeautifulSoup
import time
from telegram_bot import enviar_telegram  # mesma função que você já usa

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

filtros = {
    'zv-e10': (1800, 3500),
    '6100': (1800, 4200),
    'a6100': (1800, 4200),
    'A6100': (1800, 4200),
    '6300': (1500, 3000),
    'a6300': (1500, 3000),
    'A6300': (1500, 3000),
    '6400': (1500, 4000),
    'a6400': (1500, 4000),
    'A6400': (1500, 4000),
    '6500': (1500, 3800),
    'a6500': (1500, 3800),
    'A6500': (1500, 3800),
    '6600': (1800, 5500),
    'a6600': (1800, 5500),
    'A6600': (1800, 5500),
    '6700': (2800, 7900),
    'a6700': (2800, 7900),
    'A6700': (2800, 7900),
    '7rii':(2000,5900),
    'a7rii':(2000,5900),
    'rii':(2000,5900),
    'Rii':(2000,5900),
    '7Rii':(2000,5900),
    '7RII':(2000,5900),
    '7ii':(1500,4000),
    'a7ii':(1500,4000),
    'ii':(1500,4000),
    'Ii':(1500,4000),
    '7Ii':(1500,4000),
    '7II':(1500,4000),
    '7sii':(1500,3500),
    'a7sii':(1500,3500),
    'sii':(1500,3500),
    'Sii':(1500,3500),
    '7Sii':(1500,3500),
    '7SII':(1500,3500),
    'a7iii':(3000,6000),
    'iii':(3000,6000),
    'Iii':(3000,6000),
    'III':(3000,6000),
    '7Iii':(3000,6000),
    '7III':(3000,6000),
    '6000':(1200,1900),
    'a6000':(1200,1900),
    'a7c':(5000,7000),
    '7c':(5000,7000),
}

listIds_enviados = set()
INTERVALO_MINUTOS = 60

def monitorar_ml():
    start = 0
    url_base = 'https://lista.mercadolivre.com.br/cameras-acessorios/cameras/cameras-digitais/usado/sony_Desde_'
    encontrou = False

    while True:
        url_final = url_base + str(start) + '_NoIndex_True'
        r = requests.get(url_final, headers=headers)
        site = BeautifulSoup(r.content, 'html.parser')

        descricoes = site.find_all('a', class_='poly-component__title')
        precos_brutos = site.find_all('div', class_='poly-price__current')

        if not descricoes:
            break

        for descricao, preco_div in zip(descricoes, precos_brutos):
            texto = descricao.get_text().lower()
            texto=texto.lower()
            preco_inteiro = preco_div.find('span', class_='andes-money-amount__fraction')
            preco_centavos = preco_div.find('span', class_='andes-money-amount__cents')
            preco_str = preco_inteiro.get_text() if preco_inteiro else 'N/A'
            preco_str += ',' + preco_centavos.get_text() if preco_centavos else ',00'

            try:
                preco = float(preco_str.replace('.', '').replace(',', '.'))
            except:
                continue

            for palavra, (minimo, maximo) in filtros.items():
                if palavra.lower() in texto.lower() and minimo <= preco <= maximo:
                    id_unico = descricao.get('href').split('/')[-1].split('?')[0]
                    if id_unico in listIds_enviados:
                        continue

                    mensagem = (
                        f"📸 {descricao.get_text()}\n"
                        f"💸 R$ {preco:.2f}\n"
                        f"🔍 Palavra-chave: {palavra}\n"
                        f"🔗 {descricao.get('href')}"
                    )

                    enviar_telegram(mensagem)
                    print(f"✔️ Enviado: {descricao.get_text()} - R$ {preco:.2f}")
                    listIds_enviados.add(id_unico)
                    encontrou = True
                    break

        start += 50
    return encontrou

# Loop
print(f" Monitoramento Mercado Livre rodando a cada {INTERVALO_MINUTOS} minutos...")
while True:
    try:
        achou = monitorar_ml()
        if not achou:
            print("🔍 Nenhum anúncio novo filtrado.")
    except Exception as e:
        print(f" Erro: {e}")
    time.sleep(INTERVALO_MINUTOS * 60)