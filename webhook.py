import websocket


class Webhook:

    ws = websocket.WebSocket()
    iterator = 1

    def __init__(self):
        self.ws.connect("ws://homeassistant.local:8123/api/websocket")
        print(self.ws.recv())
        self.ws.send('{"type": "auth", "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZTFjNGYxZmFjYjI0ZWQwOTNjNDIyOTQxNzg1MGQ3YiIsImlhdCI6MTY0NjgzMDI1MywiZXhwIjoxOTYyMTkwMjUzfQ.nSKyyDIzAUaPlWIExaBONLRhITl3ObYrwhCRr1tg62w"}')
        print(self.ws.recv())

    def get_states(self):
        self.ws.send('{"id":' + str(self.iterator) + ', "type": "get_states"}')
        self.iterator += 1
        return self.ws.recv()
    
    def send_state(self, entity_id, state):
        message = '{"id":' + str(self.iterator) + ', "domain": "switch", "type": "call_service", "service":"' + state + '", "target": {"entity_id": "' + entity_id + '"}}'
        self.ws.send(message)
        self.iterator += 1
    
    def subscribe_states(self):
        self.ws.send('{"id":' +str(self.iterator) + ', "type":"subscribe_events", "event_type": "state_changed"}')
        self.iterator += 1

    def __del__(self):
        print("Connection closed.")
        self.ws.close()



