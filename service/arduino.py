import serial
import time
import serial_check as sc

def send_fold_name(fold):
    PORT = sc.check_ports()[0]
    BAUD = 9600
    if 1 <= fold <= 99:
        with serial.Serial(PORT, BAUD, timeout=2) as ser:
            time.sleep(2)
            ser.write(f"{fold}\n".encode())
            print(f"[INF] Sent fold name: {fold}")
    else:
        print(f"Error {fold}")
