import yaml
from connector import connect, disconnect
from executor import load_commands, run_commands
from reporter import save_report


def load_devices(filepath):
    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
    return data["devices"]


def main():
    devices = load_devices("inventory/devices.yaml")
    commands = load_commands("commands/show_commands.yaml")

    for device in devices:
        print(f"\n[*] Conectando a {device['name']}...")

        try:
            connection = connect(device)
            print(f"[+] Conectado a {device['name']}")

            results = run_commands(connection, commands)
            save_report(device["name"], results)

            disconnect(connection)
            print(f"[-] Desconectado de {device['name']}")

        except Exception as e:
            print(f"[!] Error en {device['name']}: {e}")


if __name__ == "__main__":
    main()
