import sys
from .advent import log

# red
RED = '\033[91m'
GREEN = '\033[92m'
BOLD = '\033[1m'
BRED = '\033[1;91m'
BGREEN = '\033[1;92m'
YELLOW = '\033[93m'
BYELLOW = '\033[1;93m'
END = '\033[0m'


def log_debug(s, *a):
    log(f'{BYELLOW}[DEBUG]{END} ' + s.format(*a))


def assert_debug(debug_input, sol, func, **kwargs):
    out = func(debug_input, **kwargs)
    func_name = func.__name__ if hasattr(func, '__name__') else func.func.__name__
    if out != sol:
        log_debug(f'{RED}WRONG ANSWER ❌{END}: {func_name} returned {out}, expected {sol}\n')
        sys.exit(1)
    else:
        log_debug(f'{BGREEN}CORRECT ANSWER 👍{END}: {func_name} = {out}\n')


def print_debug(debug_input, sol, func, **kwargs):
    out = func(debug_input, **kwargs)
    func_name = func.__name__ if hasattr(func, '__name__') else func.func.__name__
    if out != sol:
        log_debug(f'{RED}WRONG ANSWER ❌{END}: {func_name} returned {out}, expected {sol}\n')
    else:
        log_debug(f'{BGREEN}CORRECT ANSWER 👍{END}: {func_name} = {out}\n')
