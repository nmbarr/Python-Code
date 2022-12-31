import json

raw_json = 'raw.json'
output_json = 'output.json'

class SensorData():
    def __init__(self, name, min, max, scaledmin, scaledmax, units, scaledunits):
        self.name = name
        self.min = min
        self.max = max
        self.scaledmin = scaledmin
        self.scaledmax = scaledmax
        self.units = units
        self.scaledunits = scaledunits
        self.fso = 0
        self.scale_slope = 0
        self.scale_offset = 0

def read_json():
    with open(raw_json, 'r') as json_file:
        data = json.load(json_file)
        return data

def unit_conversion(sensor_list):
    for sensor in sensor_list:
        sensor.fso = sensor.max - sensor.min
        sensor.scale_slope = (sensor.scaledmax - sensor.scaledmin) / sensor.fso
        sensor.scale_offset = sensor.scaledmax - (sensor.scale_slope * sensor.min)

def write_json(data):

    all_sensor_data = []

    for sensor in data:

        formatted_data = vars(sensor)
        all_sensor_data.append(formatted_data)

    with open(output_json, 'w') as json_file:
        json.dump(all_sensor_data, json_file, indent = 4)

def main():
    json_data = read_json()

    sensors = []

    for iotype in json_data:
        io_data = json_data[iotype]
        for sensorname in io_data:
            sensordata = io_data[sensorname]
            sensor = SensorData(sensorname, 
                                sensordata['Unscaled Min'], 
                                sensordata['Unscaled Max'], 
                                sensordata['Scaled Min'],
                                sensordata['Scaled Max'],
                                sensordata['Pre-scaled Units'],
                                sensordata['Scaled Units'])
            sensors.append(sensor)

    unit_conversion(sensors)
    write_json(sensors)

if __name__ == "__main__":
    main()