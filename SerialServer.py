import serial

def setup_uart_port(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        return ser
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    port_name = "USB1"  # Replace with your specific port name
    baud_rate = 9600

    uart_port = setup_uart_port(port_name, baud_rate)
    if uart_port is None:
        exit()

    while True:
        received_data = uart_port.readline().decode('utf-8')
        if received_data:
            print("Received:", received_data.strip())

