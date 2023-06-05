import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr)


eprint("este es un mensaje de error")
