import bluetooth


def get_devices():
    devices = bluetooth.discover_devices(lookup_names=True)
    for i, device in enumerate(devices):
        print(f"{i + 1}. {device[1]}")

    return devices


def send_data(devices, receiver_num):
    receiver_address = devices[receiver_num - 1][0]
    receiver_port = 5
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((receiver_address, receiver_port))
    path_to_file = input("Input name of file to send: ")
    file_name = path_to_file.split('\\')[-1]
    sock.send(file_name)
    with open(path_to_file, "rb") as file:
        read_data = file.read(1024)
        while len(read_data) != 0:
            sock.send(read_data)
            read_data = file.read(1024)

    sock.close()


def main():
    devices = get_devices()
    receiver_num = int(input("Select a device to send data to: "))
    send_data(devices, receiver_num)


if __name__ == "__main__":
    main()
