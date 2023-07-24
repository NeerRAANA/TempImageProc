import serial

class UartClient:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.uart_port = None

    def connect(self):
        try:
            self.uart_port = serial.Serial(self.port, baudrate=self.baudrate, timeout=1)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except Exception as e:
            print("connect Error:", e)

    def send_uart_message(self, message):
        try:
            if self.uart_port:
                self.uart_port.write(message.encode('utf-8'))
                print("Message sent successfully!")
            else:
                print("UART port not initialized. Connect first using the 'connect' method.")
        except Exception as e:
            print("send_uart_message Error:", e)

    def close(self):
        if self.uart_port:
            self.uart_port.close()
            print("Connection closed.")
        else:
            print("UART port not initialized.")

##    def openNsendUartMessage(self, message_to_send, port_name='/dev/ttyS0', baud_rate=9600)
##        client = UartClient(port_name, baud_rate)
##        client.connect()
##
##        client.send_uart_message(message_to_send)
##        client.close()



if __name__ == "__main__":
    port_name = "/dev/ttyS0"  # Replace with your specific port name
    baud_rate = 9600

    client = UartClient(port_name, baud_rate)
    client.connect()

    message_to_send = "Hello, UART!"
    client.send_uart_message(message_to_send)

    client.close()

