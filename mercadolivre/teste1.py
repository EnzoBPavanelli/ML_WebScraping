import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}


url = f'https://lista.mercadolivre.com.br/cameras-acessorios/cameras/cameras-digitais/usado/camera-sony_Desde_'
start = 1

while True:
    url_final = url +str(start) + '_NoIndex_True'
    r=requests.get(url_final, headers=headers)
    site = BeautifulSoup(r.content, 'html.parser')
    descricoes= site.find_all('a', class_='poly-component__title')
    precos_brutos = site.find_all('div', class_='poly-price__current')
    link=site.find_all('h3',class_='poly-component__title-wrapper')

    if not descricoes:
        print('Sem itens')
        break
    for descricao, preco_div, link in zip(descricoes, precos_brutos, link):
        palavras_chave = ['zv-e10', '6100', '6300', '6400', '6500', '6600']
        texto = descricao.get_text().lower()

        if any(palavra in texto for palavra in palavras_chave):
            preco_inteiro = preco_div.find('span', class_='andes-money-amount__fraction')
            preco_centavos = preco_div.find('span', class_='andes-money-amount__cents')
            preco_str = preco_inteiro.get_text() if preco_inteiro else 'N/A'
            preco_str += ',' + preco_centavos.get_text() if preco_centavos else ',00'
            print('\033[mPRODUTO : ',descricao.get_text())
            print('\033[32mPREÇO : R$', preco_str)
            print(f'\033[34mLINK : {descricao.get('href')}\n')

    start +=50