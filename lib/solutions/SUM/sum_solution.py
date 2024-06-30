# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if 0> x >100 or 0 > y> 100:
        raise Exception("Invalid input")
    return x + y
