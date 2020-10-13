import uuid


def uuid_string(upper=False):
    r = uuid.uuid1()
    if upper:
        return str(r).upper()
    return str(r)
