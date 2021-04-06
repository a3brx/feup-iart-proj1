def request_file(key):
    # TODO
    return request(key)


def request(key, possible_values=None):
    key = str(key)
    ans = input(f"{key}:\n>> ")

    while possible_values and ans not in possible_values:
        print(error_message)
        ans = input(f"{key}:\n>> ")

    return ans


def request_optional(key, possible_values=None):
    key = str(key)
    ans = input(f"{key} (enter to leave deafult):\n>> ")
    try:
        ans = input(f"{key}:\n>> ")
    except SyntaxError:
        return None

    while possible_values and ans not in possible_values:
        print(error_message(key, ans))
        try:
            ans = input(f"{key} (enter to leave deafult):\n>> ")
        except SyntaxError:
            return None

    return ans


def is_file(file):
    # TODO
    pass


def error_message(key, value):
    return f"{value} is an invalid {key}"
