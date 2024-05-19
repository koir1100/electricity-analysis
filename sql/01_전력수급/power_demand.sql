CREATE OR REPLACE TABLE dev.raw_data.electric_power_demand (
  ts TIMESTAMP primary key,
  support_capacity DECIMAL(9,3),
  current_demand DECIMAL(9,3),
  maximum_predict_demand DECIMAL(6),
  support_reserved_power DECIMAL(9,3),
  support_reserved_ratio DECIMAL(9,6),
  operation_reserved_power DECIMAL(8,3),
  operation_reserved_ratio DECIMAL(9,6)
);

COPY INTO dev.raw_data.electric_power_demand
FROM 's3://yonggu-practice-bucket/project_2nd/power_demand.csv'
credentials=(AWS_KEY_ID='{}' AWS_SECRET_KEY='{}')
FILE_FORMAT=(type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

commit;

-- 전력 수급 테이블 (전력 수급 및 예비 전력 표시 활용)
CREATE TABLE dev.analytics.electronic_power_demand_summary AS
(
  SELECT DAY_AVERAGE, -- ts 용 입니다.
         SUPPORT_CAPACITY,
         CURRENT_DEMAND,
         RESERVED_CAPACITY
  FROM DEV.ANALYTICS.ELECTRONIC_POWER_DEMAND_SUMMARY;
);
