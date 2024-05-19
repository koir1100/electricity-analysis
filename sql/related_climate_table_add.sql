
ALTER TABLE dev.analytics.temperature_summary RENAME COLUMN "TEMPERATURE" to "temperature";
ALTER TABLE dev.analytics.temperature_summary RENAME COLUMN "LOWEST_TEMPERATURE" to "lowest_temperature";
ALTER TABLE dev.analytics.temperature_summary RENAME COLUMN "HIGHEST_TEMPERATURE" to "highest_temperature";

SELECT * FROM dev.analytics.climate_summary LIMIT 10;

CREATE OR REPLACE TABLE dev.raw_data.wind_speed
(
  local_number SMALLINT,
  local_name VARCHAR(10),
  ts DATE,
  avg_wind_speed DECIMAL(3,1),
  max_wind_speed DECIMAL(3,1),
  max_wind_speed_spot VARCHAR(20),
  max_instant_speed DECIMAL(3,1),
  max_instant_speed_spot VARCHAR(20)
);

COPY INTO dev.raw_data.wind_speed
FROM 's3://yonggu-practice-bucket/project_2nd/yonggu_part/merge_total_wind_speed.csv'
credentials=(AWS_KEY_ID='{}' AWS_SECRET_KEY='{}')
FILE_FORMAT=(type='CSV' skip_header=1 RECORD_DELIMITER = '\\n' FIELD_OPTIONALLY_ENCLOSED_BY='"' ENCODING='EUCKR' REPLACE_INVALID_CHARACTERS = TRUE);

COMMIT;

CREATE TABLE dev.analytics.windspeed_summary AS
(
  SELECT
    local_name,
    TO_CHAR(ts, 'YYYY-MM-01')::DATE as "month",
    avg(AVG_WIND_SPEED) as "windspeed",
    avg(MAX_WIND_SPEED) as "maxwindspeed",
    avg(MAX_INSTANT_SPEED) as "maxinstantspeed"
    FROM dev.raw_data.WIND_SPEED
    GROUP BY local_name, "month"
    ORDER BY local_name, "month"
);

CREATE OR REPLACE TABLE dev.analytics.climate_summary AS
(
  SELECT
    A.local_name,
    A."month"::DATE AS ts,
    AVG(A."temperature") AS temperature,
    AVG(B."humidity") AS humidity,
    AVG(C."rainfall") AS rainfall,
    AVG(D."windspeed") AS windspeed
  FROM
    dev.analytics.temperature_summary AS A
    LEFT JOIN dev.raw_data.local_order_table AS E
      ON A.local_name = E.local_name
    INNER JOIN dev.analytics.humidity_summary AS B
      ON A.local_name = B.local_name AND A."month" = B."month"
    INNER JOIN dev.analytics.rainfall_summary C
      ON B.local_name = C.local_name AND B."month" = C."month"
    INNER JOIN dev.analytics.windspeed_summary D
      ON B.local_name = D.local_name AND B."month" = D."month"
    GROUP BY A.local_name, E.local_number, A."month"
    ORDER BY E.local_number, A."month"
);
