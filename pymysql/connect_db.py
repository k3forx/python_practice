"""Test script."""
import pymysql
import logging
import sys


logger = logging.getLogger()
[logger.removeHandler(h) for h in logger.handlers]
log_format = "%(asctime)-15s [%(funcName)s] %(message)s"
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(stdout_handler)
logger.setLevel(logging.INFO)

SELECT_JOB_COMPLETED_QUERY_FMT = """SELECT client_id FROM job_execution;"""


class LocalDatabase:
    def __init__(self, db_config):
        self.db_config = db_config

    def make_connection(self):
        logger.info("Make connection...")
        self.conn = pymysql.connect(**self.db_config)
        logger.info("Connecting to DB...")
        logger.info(
            f"Host: {self.conn.host}, Database: {self.conn.db},"
            f"User: {self.conn.user}"
        )

    def close_connection(self):
        self.conn.close()
        logger.info("Connection is closed.")

    def deco_execute_query(func):
        def wrapper(self, query, *args, **kwargs):
            self.make_connection()
            try:
                with self.conn.cursor() as cursor:
                    self.cursor = cursor
                    self.cursor.execute(query)
                    return func(self)
            except Exception as e:
                logger.error(f"Error while executing query. {e}")
            finally:
                self.close_connection()

        return wrapper

    @deco_execute_query
    def execute_fetch_query(self):
        return self.cursor.fetchall()

    @deco_execute_query
    def execute_insert_query(self):
        return self.conn.commit()


def main():
    """Execute main func."""
    db_config = {
        "host": "127.0.0.1",
        "user": "lag_cv_write_user",
        "db": "lag_cv",
        "passwd": "xxxxxxx",
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
    }
    lagcv_db = LocalDatabase(db_config)
    result = lagcv_db.execute_fetch_query(SELECT_JOB_COMPLETED_QUERY_FMT)
    print(result)
    lagcv_db.execute_insert_query(
        """INSERT INTO job_execution (client_id, last_executed_time) VALUES (100, '2020-08-01 15:11:38') ON DUPLICATE KEY UPDATE last_executed_time = '2020-08-01 15:11:38';"""
    )


if __name__ == "__main__":
    main()
