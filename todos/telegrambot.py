import requests
from decouple import config

# decouple로 token 숨겨서 가져오기
token = config('TELEGRAM_TOKEN')

def send(title, due_date):
    # 보낼 메시지
    text = f'할일: {title} | 마감일: {due_date}'

    baseurl = "https://api.telegram.org"
    # chat_id 받아오기
    url_updates = f'{baseurl}/bot{token}/getUpdates'
    response_updates = requests.get(url_updates)
    dict_updates = response_updates.json()
    # chat_id = dict_updates['result'][0]['message']['from']['id']
    
    # chat_id마다 메시지 보내기
    for result in dict_updates['result']:
        chat_id = result['message']['from']['id']
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        url_sending = f'{baseurl}/bot{token}/sendMessage'
        requests.get(url_sending, params)