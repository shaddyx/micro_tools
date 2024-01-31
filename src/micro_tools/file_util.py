def get_full_filename(name: str, ext: str):
    if name.endswith(ext) or "." in name:
        return name
    else:
        return "{}.{}".format(name, ext)

