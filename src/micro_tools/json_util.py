import json


def stringify(data):
    return json.dumps(list(data), indent=4)


def dump_steam_to_file(file, stream):
    with open(file, "w") as f:
        f.write("[")
        first = True
        for row in stream:
            if not first:
                f.write(",\n")
            first = False
            f.write(json.dumps(row, indent=4))
        f.write("]")
