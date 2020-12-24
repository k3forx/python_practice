# from log import get_logger
import logging
import sys


logger = logging.getLogger()
[logger.removeHandler(h) for h in logger.handlers]
log_format = '%(asctime)-15s [%(funcName)s] %(message)s'
stdout_handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel(logging.INFO)


def times_number(num):
    logger.info("Times")
    times_num = num ** 2

    logger.info(times_num)
    logger.info("end")
    return "succeed"
