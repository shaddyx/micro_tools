def find_value(msg: str, name: str, delimiter="=", terminators=[" ", ",", ";", "\n"], default=None):
    try:
        n_with_delimiter = name + delimiter
        first = msg.index(n_with_delimiter)
        value_start = first + len(n_with_delimiter)
        value_end = len(msg)
        for k in terminators:
            try:
                value_end = min(value_end, msg.index(k, value_start))
            except ValueError:
                pass
        return msg[value_start: value_end]

    except ValueError:
        return default


def find_value_between(msg: str, string1: str, string2: str):
    index1 = msg.index(string1) + len(string1)
    index2 = msg.index(string2, index1)
    return msg[index1:index2]
