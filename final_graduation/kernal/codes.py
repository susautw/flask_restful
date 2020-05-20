codes = {
    # system-related
    'UnknownError': -1,

    # database-related
    'NoDataFound': -200,
    'ItemAlreadyExists': -201,
}


def get_codes(name: str) -> int:
    return codes[name]
