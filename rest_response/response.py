import requests
from rest_response.states import devices


class Response:
    token = ""
    url = ""

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def send_state(self, automation_res):
        headers = {"Authorization": "Bearer " + self.token}

        response_fields = automation_res.strip().split(" ")
        device_id = response_fields[0]
        device = devices.get(device_id.split(".")[0])
        state = response_fields[1]
        if "switch" in device_id:
            req_data = {"entity_id": device_id}
            resp = requests.post(self.url + "switch/" + device.get(state), headers=headers, json=req_data)
            #print(resp.text)
        elif "climate" in device_id:
            selected_mode = response_fields[2]
            selected_mode_arr = device.get("data").get(selected_mode)
            req_data = {"entity_id": device_id, selected_mode_arr[1]: state}
            resp = requests.post(self.url + "climate/" + selected_mode_arr[0], headers=headers, json=req_data)
            #print(resp.text)
        elif "light" in device_id:
            req_data = {"entity_id": device_id}
            resp = requests.post(self.url + "light/" + device.get(state), headers=headers, json=req_data)
            #print(resp.text)





