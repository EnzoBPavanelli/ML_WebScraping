# ML_WebScraping – Monitorador de Produtos do Mercado Livre com Alerta via Telegram

Este repositório contém um sistema de web scraping voltado para o site do Mercado Livre. Seu objetivo é monitorar anúncios de produtos com base em critérios definidos e enviar notificações via Telegram sempre que novas oportunidades forem encontradas.

## Objetivo

Criar um sistema automatizado para:

- Buscar automaticamente produtos no Mercado Livre
- Detectar novas ofertas com base em palavras-chave
- Enviar alertas via Telegram
- Evitar repetições de envio com uso de logs locais

## Tecnologias e Ferramentas

- Python 3
- requests e BeautifulSoup
- API do Telegram
- Scripts simples e personalizáveis

## Estrutura do Projeto

mercadolivre/
├── raspagem.py   # Script principal de raspagem
├── telegram_bot.py   # Envio de mensagens via Telegram
├── teste1.py   # Script auxiliar de testes
├── ids_enviados.txt  
├── links_enviados.txt 
└── pycache   

## Como Funciona

O script realiza buscas periódicas no Mercado Livre com base em uma consulta definida no código. Cada novo anúncio encontrado é comparado com os registros anteriores. Caso não tenha sido enviado ainda, uma notificação é disparada para o Telegram.

## Como Usar

1. Clone o repositório
2. Instale as dependências (caso aplicável)
3. Configure o token e chat ID no `telegram_bot.py`
4. Execute:
     python raspagem.py

## Licença

Uso pessoal. Todos os direitos reservados ao autor.

## Contato

Enzo Pavanelli  
LinkedIn: https://www.linkedin.com/in/enzo-brito-pavanelli-269290256/
