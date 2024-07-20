import json
import os

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

all_config_data = {}
configs_list = []

for config in os.listdir(WORKING_DIR):
    if config.endswith('.json'):
        config_filename = os.path.join(WORKING_DIR, config)
        configs_list.append(config)

        with open(config_filename) as json_config:
            config_data = json.load(json_config)
            all_config_data.update(config_data)
    else:
        continue

config_headers = list(all_config_data)
config_values = list(all_config_data.values())
