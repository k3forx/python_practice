import logging


def get_logger(scope):
    logger = logging.getLogger(scope)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger
