# from log import get_logger
from times import times_number
import logging
import sys



logger = logging.getLogger()
[logger.removeHandler(h) for h in logger.handlers]
log_format = '%(asctime)-15s [%(funcName)s] %(message)s'
stdout_handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel(logging.INFO)

def main():
    logger.info("Start")

    for i in range(10):
        string = times_number(i)
        logger.info(string)


if __name__ == "__main__":
    main()
