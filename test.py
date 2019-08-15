import os
import slack
import asyncio
"""
client = slack.WebClient(')

response = client.chat_postMessage(
    channel='#test',
    text="Всем привет!")
assert response["ok"]
"""

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
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
    if '/register' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Уважаемый <@{user}>! Пожалуйста введите своё имя",
        )
        web_client.

slack_token = ''
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()