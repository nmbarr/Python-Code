import os
import json
from definitions import CONFIGS_DIR
from modules.config_classes import ChannelType

def main():
    config_data = read_configs()
    channel_types = parse_configs(config_data)
    return channel_types

def read_configs():
    for config in os.listdir(CONFIGS_DIR):
        if check_if_valid_config(config):
            config_filename = os.path.join(CONFIGS_DIR, config)

            with open(config_filename, 'r') as json_config:
                data = json.load(json_config)
    return data

def check_if_valid_config(config):
    if config.endswith('.json'):
        valid_config = True
    else:
        valid_config = False
    return valid_config

def parse_configs(config_data):

    channel_types = []

    for section in config_data:
        channel_type = ChannelType(section, config_data[section])
        channel_types.append(channel_type)
    return channel_types