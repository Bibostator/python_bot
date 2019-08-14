import os
import slack

client = slack.WebClient('xoxb-690139347445-728256943191-pH9k5clleGyApMddhpm28iBY')

response = client.chat_postMessage(
    channel='#test',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"