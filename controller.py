import copy
import json

class ACController:
    def __init__(self):
        with open("commands.json", "r") as command_file:
            self.commands = json.load(command_file)
        self.ac_action = {
            "domain": "mqtt",
            "service": "publish", 
            "service_data": {
                "topic": "zigbee2mqtt/0x4c5bb3fffe0c88e0/set",
                "payload": {
                    "ir_code_to_send": ""
                },
                "qos": 0,
                "retain": False
            }   
        }

    def turn_on(self):
        # make a deep copy of the action dictionary
        ac_action = copy.deepcopy(self.ac_action)
        ac_action["service_data"]["payload"]["ir_code_to_send"] = self.commands["turn_on"]
        ac_action["service_data"]["payload"] = json.dumps(ac_action["service_data"]["payload"])
        return ac_action
    
    def turn_off(self):
        ac_action = copy.deepcopy(self.ac_action)
        ac_action["service_data"]["payload"]["ir_code_to_send"] = self.commands["turn_off"]
        ac_action["service_data"]["payload"] = json.dumps(ac_action["service_data"]["payload"])
        return ac_action