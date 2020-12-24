"""Test purpose."""
from joblib import Parallel, delayed
import pymysql
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

kwargs = {
    "host": "usergram-test.cn2hwra1jxld.ap-northeast-1.rds.amazonaws.com",
    "user": "miyahana",
    "db": "lag_cv",
    "passwd": "xxxxx",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

COUNT_GRAM_FOR_EACH_USER_QUERY_FMT = """
SELECT
  JSON_ARRAYAGG(sum_gram_count)
FROM (
  SELECT
    SUM(gram_count) AS sum_gram_count
  FROM
    gram_count_per_user
  WHERE
    client_id = {client_id}
    AND
      user_id IN ({user_ids})
  GROUP BY
    user_id
  ORDER BY
    sum_gram_count DESC
  )
AS SUM_TABLE;
"""

SELECT_LAG_CV_USERS_QUERY_FMT = """
SELECT
  user_ids
FROM
  lag_cv_result
WHERE
  client_id = {client_id}
  AND
    conversion_id = {conversion_id}
  AND
    end_date = DATE('2020-10-31')
  AND
    period = 'four-weeks';
"""


class Db:
    """Class to deal with database"""

    def __init__(self):
        pass

    def make_connection(self):
        self.conn = pymysql.connect(**kwargs)
        logger.info("Connecting to DB...")
        logger.info(
            f"Host: {self.conn.host}, Database: {self.conn.db}, User: {self.conn.user}"
        )

    def close_connection(self):
        self.conn.close()
        logger.info("Connection is closed.")

    def execute_select_query(self, query):
        self.make_connection()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except pymysql.Error as e:
            logger.error(f"Error while executing query. {e}")
        finally:
            self.close_connection()

    def get_gram_count_for_each_user(self, client_id, query):
        user_ids = self.execute_select_query(query)
        print(user_ids[0]{'user_ids'}))
        count_gram_query = COUNT_GRAM_FOR_EACH_USER_QUERY_FMT.format(client_id=client_id, user_ids=','.join(user_ids[0]{'user_ids'}))
        print(count_gram_query)



def main():
    """Main func."""
    LagCvDb = Db()
    client_id2conversion_id = {3: [0, 28, 64, 65, 66, 116, 740, 2091]}
    select_lagcv_users_query = SELECT_LAG_CV_USERS_QUERY_FMT.format(
        client_id=3, conversion_id=64
    )
    LagCvDb.get_gram_count_for_each_user(3, select_lagcv_users_query)


    """
    db_conn = pymysql.connect(**db_config)
    logger.info(
        f"Connecting to database... Host: {db_conn.host}, Database: {db_conn.db}, User: {db_conn.user}"
    )
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return func(results, kwargs) if func else results
    except pymysql.Error as e:
        logger.error(f"Error while executing query. {e}")
    finally:
        db_conn.close()
        logger.info("Connection is closed.")


def generate_abnormal_users_select_query(
    client_id, gram_count_threshold, gram_count_days
):
    """Generate a query to select abnormal users.

    Args:
        client_id (`int`): client ID
        gram_count_threshold (`int`): minimum value of gram count for abnormal users
        gram_count_days (`int`): number of days for which we aggregate abnormal users

    Returns:
        query (`str`): MySQL query to extract abnormal users

    """
    end_date = datetime.now(JST).date()
    start_date = end_date - timedelta(days=gram_count_days)
    gram_count_year_month_cond = f"""
        (year, month) >= ({start_date.year}, {start_date.month})
        AND
          (year, month) <= ({end_date.year}, {end_date.month})"""
    return SELECT_ABNORMAL_USERS_QUERY_FMT.format(
        client_id=client_id,
        gram_count_year_month_cond=gram_count_year_month_cond,
        gram_count_threshold=gram_count_threshold,
    )


if __name__ == "__main__":
    main()
