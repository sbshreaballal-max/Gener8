import yaml

def load_persona(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

