import configparser

def LoadConfig(file):
    with open(file) as f:
        sample_config = f.read()
    config = configparser.RawConfigParser(allow_no_value=True)
    config.read(sample_config)
    return config

config_obj = LoadConfig("config.ini")
print(config_obj["password"])