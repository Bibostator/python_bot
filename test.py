import os
import slack

client = slack.WebClient('')

response = client.chat_postMessage(
    channel='#test',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"