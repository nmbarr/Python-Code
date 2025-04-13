import time
import random
import math

class Sensor:
    def __init__(self, sensor_name="Sensor", mode="sine", frequency=1.0, amplitude=1.0, offset=0.0, noise=0.0, round_digits=3, units="psi"):
        self.sensor_name = sensor_name
        self.mode = mode
        self.frequency = frequency
        self.amplitude = amplitude
        self.offset = offset
        self.noise = noise
        self.round_digits = round_digits
        self.units = units
        self.start_time = time.time()

    def read(self):
        elapsed = time.time() - self.start_time
        signal = self._generate_signal(elapsed)
        noisy_signal = signal + random.uniform(-self.noise, self.noise)
        return round(noisy_signal + self.offset, self.round_digits)

    def _generate_signal(self, t):
        if self.mode == "sine":
            return self.amplitude * math.sin(2 * math.pi * self.frequency * t)
        elif self.mode == "step":
            return self.amplitude if t > 2 else 0
        elif self.mode == "random":
            return random.uniform(-self.amplitude, self.amplitude)
        else:
            raise ValueError(f"Unknown signal mode: {self.mode}")