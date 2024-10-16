def check_number(value: int):
    try:
        output = 0
        if value % 2 == 0:
            output += 1

        if value % 100 == 0:
            output += 2

        return output
    except Exception as exc:
        print(exc)
        raise exc