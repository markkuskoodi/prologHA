from webhook import Webhook
import json
import asyncio

hook = Webhook()

hook.subscribe_states()

'''
while True:
    result = hook.ws.recv()
    result = json.loads(result)
    print(result)
'''