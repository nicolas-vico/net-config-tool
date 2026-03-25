import yaml


def load_commands(filepath):
    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
    return data["show_commands"]


def run_commands(connection, commands):
    results = {}
    for command in commands:
        output = connection.send_command(command)
        results[command] = output
    return results
