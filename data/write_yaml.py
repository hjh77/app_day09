import yaml

data = {
    "name_data": {
        "name1": "hhhh"
    }
}
with open("./data3.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
