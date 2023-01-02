class AnalogInputChannel():
    def __init__(self, name, serial_number, output_l, output_h, use_scale, min, max, scale_units, comments, type):
        self.name = name
        self.serial_number = serial_number
        self.output_l = output_l
        self.output_h = output_h
        self.use_scale = use_scale
        self.min = min
        self.max = max
        self.scale_units = scale_units
        self.comments = comments
        self.type = type

class AnalogOutputChannel():
    def __init__(self, name, output_l, output_h, use_scale, min, max, scale_units, comments, type):
        self.name = name
        self.output_l = output_l
        self.output_h = output_h
        self.use_scale = use_scale
        self.min = min
        self.max = max
        self.scale_units = scale_units
        self.comments = comments
        self.type = type

class DigitalInputChannel():
    def __init__(self, name, comments, type):
        self.name = name
        self.comments = comments
        self.type = type

class DigitalOutputChannel():
    def __init__(self, name, comments, type):
        self.name = name
        self.comments = comments
        self.type = type