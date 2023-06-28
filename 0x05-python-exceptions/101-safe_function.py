#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as error:
        result = None
        print("Exception: {}".format(error), file=sys.stderr)
    return result
