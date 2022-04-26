import json
from config.devices_config import supported_devices


class Data:
    data = {}

    def __init__(self, initial_request):
        data_temp = json.loads(initial_request)
        result = data_temp.get("result")

        for i in result:
            device_type = i.get("entity_id").split(".")[0]
            if device_type in supported_devices:
                self.data[i.get("entity_id")] = (i.get("state"), i.get("attributes"))

    def get_data(self):
        return self.data

    def update_data(self, received_state):
        temp = json.loads(received_state)
        result = temp.get("event")
        if result is not None and result.get("event_type") == "state_changed":
            result = result.get("data")
            self.data[result.get("entity_id")] = (
                result.get("new_state").get("state"), result.get("new_state").get("attributes"))
