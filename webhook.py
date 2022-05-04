import websocket


class Webhook:
    ws = websocket.WebSocket()
    iterator = 1

    send_state_int = {"on": "turn_on", "open": "turn_on", "close": "turn_off", "off": "turn_off"}

    def __init__(self, socket_address, token):
        self.ws.connect(socket_address)
        print(self.ws.recv())
        self.ws.send('{"type": "auth", "access_token": "' + token + '"}')
        print(self.ws.recv())

    def get_states(self):
        self.ws.send('{"id":' + str(self.iterator) + ', "type": "get_states"}')
        self.iterator += 1
        return self.ws.recv()

    def send_state(self, entity_id, state):
        print(self.send_state_int.get(state))
        message = '{"id":' + str(
            self.iterator) + ', "domain": "switch", "type": "call_service", "service":"' + self.send_state_int.get(
            state) + '", "target": {"entity_id": "' + entity_id + '"}}'
        self.ws.send(message)
        self.iterator += 1

    def subscribe_states(self):
        self.ws.send('{"id":' + str(self.iterator) + ', "type":"subscribe_events", "event_type": "state_changed"}')
        self.ws.recv()
        self.iterator += 1

    def __del__(self):
        print("Connection closed.")
        self.ws.close()
