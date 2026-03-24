from netmiko import ConnectHandler


def connect(device):
    connection = ConnectHandler(
        host=device["host"],
        username=device["username"],
        password=device["password"],
        device_type=device["device_type"],
        port=device["port"]
    )
    return connection


def disconnect(connection):
    connection.disconnect()
