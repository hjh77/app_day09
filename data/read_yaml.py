import yaml

with open("./data2.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("data:{}".format(data.get("value1")))
    print("type:{}".format(type(data)))
