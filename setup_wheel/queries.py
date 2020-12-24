"""Queries which are used in glue_job_data_agg.py."""

SELECT_JOB_SUCCEEDED_CLIENT_QUERY_FMT = """
  SELECT
    client_id
  FROM
    job_execution
  WHERE
    DATE(last_executed_time) = '{executed_date}';
"""

AGG_LAGCV_USERS_QUERY_FMT = """
we need to pass following values
{client_id},
{one_day_period_start_time},
{one_week_period_start_time},
{four_weeks_period_start_time},
{four_weeks_period_end_time},
{invalid_cv_gram_year_month_cond},
{gram_year_month_day_cond},
{GRAM_TABLE_PREFIX},
{GLOBAL_CONVERSION_IDS},
"""

UPDATE_LAGCV_USER_QUERY_FMT = """
  INSERT INTO lag_cv_result
    (client_id, period, conversion_id, user_ids, start_date, end_date)
  VALUES
    {values}
  ON DUPLICATE KEY UPDATE
    user_ids = VALUES(user_ids),
    start_date = VALUES(start_date),
"""

UPDATE_JOB_EXECUTION_QUERY_FMT = """
  INSERT INTO
    job_execution (client_id, last_executed_time)
  VALUES
    ({client_id}, '{last_executed_time}')
  ON DUPLICATE KEY UPDATE
    last_executed_time = VALUES(last_executed_time);
"""
