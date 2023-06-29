#!/usr/bin/python3
def safe_function(fct, *args):
    result = 0
    for i in range(1, 6):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result += a + b
            break
    return result
