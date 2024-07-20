from read_config import all_config_data, config_headers, config_values, configs_list

class ConfigData_A:
    def __init__(self, header_a, header_b):
        self.header_a = header_a
        self.header_b = header_b

    def nested_dict(self, nested_dictionary):
        if isinstance(nested_dictionary, dict):
            self.nested_keys = list(nested_dictionary)
            self.nested_values = list(nested_dictionary.values())
        else:
            print('WTF')

class ConfigData_B:
    def __init__(self, header_c, header_d):
        self.header_c = header_c
        self.header_d = header_d

conf_a = ConfigData_A(config_values[0], config_values[1])
conf_b = ConfigData_B(config_values[2], config_values[3])

# print(conf_a.header_a)
# print(conf_a.header_b)

# print(conf_b.header_c)
# print(conf_b.header_d)

conf_dict = conf_a.nested_dict(config_values[0])

print(conf_dict)
print(conf_dict.nested_keys)
