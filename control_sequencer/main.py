import time
from simulate.sensor import Sensor
from simulate.average_sensors import average_2oo3

READ_RATE = 10  # Hz
READ_PERIOD = 1 / READ_RATE  # seconds

def main():
    pt_sensors = []

    PT_A = Sensor(sensor_name="Tank_PT_A", mode="random", amplitude=1.0, offset=14.7, noise=0.1, units="psi")
    PT_B = Sensor(sensor_name="Tank_PT_B", mode="random", amplitude=2.0, offset=14.5, noise=0.2, units="psi")
    PT_C = Sensor(sensor_name="Tank_PT_C", mode="random", amplitude=3.0, offset=15.3, noise=0.5, units="psi")

    pt_sensors.extend([PT_A, PT_B, PT_C])

    print("Starting sensor read loop. Press Ctrl+C to stop.")
    print(f"Read Rate: {READ_RATE} Hz ({READ_PERIOD:.3f} sec)")

    try:
        while True:
            values = [sensor.read() for sensor in pt_sensors]
            
            for sensor, value in zip(pt_sensors, values):
                print(f"[{time.strftime('%H:%M:%S')}] {sensor.sensor_name}: {value:.3f} {sensor.units}", flush=True)

            voted_average = average_2oo3(sensor_values=values)
            print(f"2oo3 Voted Average: {voted_average:.3f} psi\n")

            time.sleep(READ_PERIOD)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
