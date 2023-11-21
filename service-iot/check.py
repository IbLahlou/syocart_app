import serial.tools.list_ports

# Get a list of all the available COM ports
com_ports = serial.tools.list_ports.comports()

# Print the list of COM ports
for port, desc, hwid in sorted(com_ports):
    print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")
