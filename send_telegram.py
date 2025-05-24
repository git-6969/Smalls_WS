import requests

BOT_TOKEN = '5994386382:AAGM0b3mKFwIjXfSGHhscJCg8FCX7oIu8yM'

CHAT_ID = 1017525086  # 이전에 받은 chat.id 값

def send_telegram_message(chat_id, message):
    """주어진 chat_id로 텔레그램 메시지 보내는 함수"""
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(url)
    return response.json()  # 응답 결과 반환

# 예시 사용
response = send_telegram_message(CHAT_ID, "안녕하세요! 이것은 자동으로 보내는 메시지입니다.")
print(response)