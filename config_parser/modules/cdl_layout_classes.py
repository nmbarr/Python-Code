class AnalogInputLayout():
    def __init__(self, name, serial_number, output_l, output_h, use_scale, min, max, scale_units, comments):
        self.name = name
        self.serial_number = serial_number
        self.output_l = output_l
        self.output_h = output_h
        self.use_scale = use_scale
        self.min = min
        self.max = max
        self.scale_units = scale_units
        self.comments = comments

class AnalogOutputLayout():
    def __init__(self, name, output_l, output_h, use_scale, min, max, scale_units, comments):
        self.name = name
        self.output_l = output_l
        self.output_h = output_h
        self.use_scale = use_scale
        self.min = min
        self.max = max
        self.scale_units = scale_units
        self.comments = comments

class DigitalInputLayout():
    def __init__(self, name, comments):
        self.name = name
        self.comments = comments

class DigitalOutputLayout():
    def __init__(self, name, comments):
        self.name = name
        self.comments = comments