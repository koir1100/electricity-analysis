
CREATE TABLE DEV.RAW_DATA.HUMIDITY
(
  local_number TINYINT,
  local_name VARCHAR(10),
  ts DATE,
  avg_humidity TINYINT,
  lowest_humidity TINYINT,
  lowest_humidity_spot VARCHAR(50)
);


CREATE TABLE DEV.RAW_DATA.RAINFALL
(
  ts DATE,
  local_name VARCHAR(10), 
  rainfall_amount DECIMAL(5,1)
);


CREATE TABLE DEV.RAW_DATA.TEMPERATURE
(
  ts DATE,
  local_name VARCHAR(10),
  avg_temperature DECIMAL(3,1),
  lowest_temperature DECIMAL(3,1),
  highest_temperature DECIMAL(3,1)
);


COPY INTO dev.raw_data.HUMIDITY
FROM 's3://yonggu-practice-bucket/project_2nd/yonggu_part/merge_total_humidity.csv'
credentials=(AWS_KEY_ID='{}' AWS_SECRET_KEY='{}')
FILE_FORMAT=(type='CSV' skip_header=1 RECORD_DELIMITER = '\\n' FIELD_OPTIONALLY_ENCLOSED_BY='"' ENCODING='EUCKR' REPLACE_INVALID_CHARACTERS = TRUE);

COPY INTO dev.raw_data.RAINFALL
FROM 's3://yonggu-practice-bucket/project_2nd/yonggu_part/merge_total_rainfall.csv'
credentials=(AWS_KEY_ID='{}' AWS_SECRET_KEY='{}')
FILE_FORMAT=(type='CSV' skip_header=1 RECORD_DELIMITER = '\\n' FIELD_OPTIONALLY_ENCLOSED_BY='"' ENCODING='EUCKR' REPLACE_INVALID_CHARACTERS = TRUE);

COPY INTO dev.raw_data.TEMPERATURE
FROM 's3://yonggu-practice-bucket/project_2nd/yonggu_part/merge_total_temperature.csv'
credentials=(AWS_KEY_ID='{}' AWS_SECRET_KEY='{}'')
FILE_FORMAT=(type='CSV' skip_header=1 RECORD_DELIMITER = '\\n' FIELD_OPTIONALLY_ENCLOSED_BY='"' ENCODING='EUCKR' REPLACE_INVALID_CHARACTERS = TRUE);

COMMIT;

SELECT * FROM dev.raw_data.HUMIDITY LIMIT 10;
SELECT * FROM dev.raw_data.RAINFALL LIMIT 10;
SELECT * FROM dev.raw_data.TEMPERATURE LIMIT 10;

CREATE TABLE dev.raw_data.LOCAL_ORDER_TABLE AS
(
  SELECT DISTINCT LOCAL_NUMBER, LOCAL_NAME
  FROM dev.raw_data.HUMIDITY
  ORDER BY LOCAL_NUMBER
);

commit;

SELECT
  local_name,
  TO_CHAR(ts, 'YYYY-MM-01')::DATE as "month",
  avg(avg_humidity) as "humidity"
  FROM dev.raw_data.HUMIDITY
  GROUP BY local_name, "month"
  ORDER BY local_name, "month"
  LIMIT 10;

SELECT
  local_name,
  TO_CHAR(ts, 'YYYY-MM-01')::DATE as "month",
  avg(rainfall_amount) as "rainfall"
  FROM dev.raw_data.RAINFALL
  GROUP BY local_name, "month"
  ORDER BY local_name, "month"
  LIMIT 10;
  
SELECT
  local_name,
  TO_CHAR(ts, 'YYYY-MM-01')::DATE as "month",
  avg(AVG_TEMPERATURE) as "TEMPERATURE",
  avg(LOWEST_TEMPERATURE) as "LOWEST_TEMPERATURE",
  avg(HIGHEST_TEMPERATURE) as "HIGHEST_TEMPERATURE"
  FROM dev.raw_data.RAINFALL
  GROUP BY local_name, "month"
  ORDER BY local_name, "month"
  LIMIT 10;

ROLLBACK;
  
