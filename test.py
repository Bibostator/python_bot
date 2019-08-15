import os
import slack
"""
client = slack.WebClient(')

response = client.chat_postMessage(
    channel='#test',
    text="Всем привет!")
assert response["ok"]
"""
reg_user=''
@slack.RTMClient.run_on(event='message')
def body(**payload):
    global reg_user
    data = payload['data']
    print(data)
    print(type(data))
    if data.get("subtype", None) == 'bot_message':
        return
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",

            )
    if '1' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = reg_user = data['user']
        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Уважаемый <@{user}>! Пожалуйста введите своё имя",
        )

        return

    if reg_user == data['user']:
        channel_id = data['channel']
        text = data['text']
        reg_user = ''
        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Спасибо, {text}",
            attachments= [
                {
                    "fallback": "Would you recommend it to customers?",
                    "title": "Would you recommend it to customers?",
                    "callback_id": "comic_1234_xyz",
                    "color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "register",
                            "text": "Зарегистрироваться",
                            "type": "button",
                            "value": "reg"
                        },
                        {
                            "name": "no",
                            "text": "Отменить",
                            "type": "button",
                            "value": "cancel"
                        }
                    ]
                }
            ]
        )



slack_token = ''
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()