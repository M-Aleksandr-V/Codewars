def validate_pin(pin):
    return len(pin) in (4, 6) and all(p in '0123456789' for p in pin)


pin = "-12345"

print(validate_pin(pin))