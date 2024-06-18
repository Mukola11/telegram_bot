import requests

# Замість 'YOUR_API_TOKEN' введіть свій API токен, який ви отримали від BotFather
TOKEN = '7335859829:AAH4q3XvBiIKuO6NIke77aaNAJXKpYcXWyo'

# Замість 'CHAT_ID' введіть ідентифікатор чату, куди ви хочете відправити повідомлення
CHAT_ID = '453014825'

# URL для відправки повідомлення через Telegram Bot API
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# Текст повідомлення, яке ви хочете відправити
text = 'Це тестове повідомлення від мого Telegram бота.'

# Параметри запиту
params = {
    'chat_id': CHAT_ID,
    'text': text
}

# Відправляємо POST запит з використанням бібліотеки requests
response = requests.post(url, params=params)

# Перевіряємо результат запиту
if response.status_code == 200:
    print('Повідомлення успішно відправлено.')
else:
    print(f'Помилка відправки повідомлення: {response.status_code} - {response.reason}')
    print(response.text)


#TOKEN = '7335859829:AAH4q3XvBiIKuO6NIke77aaNAJXKpYcXWyo'




