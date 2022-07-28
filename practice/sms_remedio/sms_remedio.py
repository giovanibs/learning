# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import time

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC922bad90ac88d90de4d4a0c7c6acd0c0"
auth_token = "7ee21aba7101aef81b9a706250489258"
client = Client(account_sid, auth_token)

timer = time.time()
x = 1
while True:
    
    message = client.messages \
                    .create(
                        body=f"Mensagem #{x}",
                        from_='+17372658183',
                        to='+5595991599099', ''
                        to='+5595991599099'
                        to='+5595991599099'
                        to='+5595991599099'
                        to='+5595991599099'
                        to='+5595991599099'
                        to='+5595991599099'
                    )
    timer_end = time.time()
    if (timer_end - timer) > 350:
        break
    time.sleep(60)
    x += 1
    
print(message.sid)
