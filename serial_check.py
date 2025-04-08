import serial.tools.list_ports as stlp
import platform


def check_ports():
    system_platform = platform.system()
    if system_platform == "Windows":
        return list(stlp.comports())
    elif system_platform == "Linux" or system_platform == "Darwin":
        ports = []
        for port in stlp.comports():
            if port.device.startswith('/dev/ttyUSB') or port.device.startswith('/dev/ttyACM'):
                ports.append(port.device)
        return ports


def print_available_ports():
    try:
        ports = check_ports()
        if ports:
            print("Available COM Ports:")
            for port in ports:
                print(f" - {port}")
        else:
            print("No available COM ports found.")
    except Exception as e:
        print(f"Error: {e}")
