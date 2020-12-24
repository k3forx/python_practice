from joblib import Parallel, delayed
import logging
import sys
from collections import defaultdict
import time
from datetime import datetime, timedelta, timezone


logger = logging.getLogger()
[logger.removeHandler(h) for h in logger.handlers]
log_format = "%(asctime)-15s [%(funcName)s] %(message)s"
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(stdout_handler)
logger.setLevel(logging.INFO)

def main():
    res = Parallel(n_jobs=5, verbose=100)([delayed(test(x_square))(i) for i in range(10000)])



def x_square(i):
    return i * 2

def test(num):
    return f"number is {num}"


if __name__ == "__main__":
    main()
