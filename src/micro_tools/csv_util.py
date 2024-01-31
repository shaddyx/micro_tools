import csv
import typing

from micro_tools import control


def write_list_to_file(file, data):
    with open(file, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for k in data:
            if not isinstance(k, list):
                k = [k]
            csv_writer.writerow(k)


def write_list_of_dicts_to_file(file, data, field_names, delimiter=','):
    with open(file, 'w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=delimiter)
        csv_writer.writeheader()
        for k in data:
            if not isinstance(k, dict):
                raise Exception("row is not a dict: ".format(k))
            csv_writer.writerow(k)


def write_list_of_dicts_to_file_auto(file, data, delimiter=','):
    cols = []
    for k in data:
        if not isinstance(k, dict):
            raise Exception("row is not a dict: ".format(k))
        for x in k:
            if x not in cols:
                cols.append(x)
    return write_list_of_dicts_to_file(file, data, cols, delimiter=delimiter)


def get_cols(data: typing.Union[typing.List[typing.Dict], typing.Dict]):
    res = {}
    for x in data:
        res[x] = 1
    return [k for k in res]


def write_csv(file: str, data: typing.Union[typing.List[typing.Dict], typing.Iterator[typing.Dict]], cols=None,
              write_header=True, delimiter=','):
    with open(file, 'w') as f:
        writer = csv.writer(f, delimiter=delimiter)
        first = True
        for k in data:
            if first:
                first = False
                if cols is None:
                    cols = get_cols(k)
                if write_header:
                    writer.writerow(cols)
            line = [""] * len(cols)
            for x in range(len(cols)):
                field_name = cols[x]
                line[x] = k[field_name] if field_name in k else ""
            writer.writerow(line)


def read_csv(file: str, read_headers=False, delimiter=',', quotechar=None):
    with open(file, 'r') as csvfile:
        first = control.Once()
        csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        cols = None
        for row in csv_reader:
            if read_headers and first.check():
                cols = row
                continue
            if read_headers:
                yield {cols[k]: row[k] for k in range(len(cols))}
            else:
                yield row
