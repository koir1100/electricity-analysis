CREATE OR REPLACE TABLE dev.raw_data.electric_power_demand (
  ts TIMESTAMP primary key,
  support_capacity NUMBER(9,3),
  current_demand NUMBER(9,3),
  maximum_predict_demand NUMBER(6),
  support_reserved_power NUMBER(9,3),
  support_reserved_ratio NUMBER(9,6),
  operation_reserved_power NUMBER(8,3),
  operation_reserved_ratio NUMBER(9,6)
);

COPY INTO dev.raw_data.electric_power_demand
FROM 's3://yonggu-practice-bucket/project_2nd/power_demand.csv'
credentials=(AWS_KEY_ID='{}' AWS_SECRET_KEY='{}')
FILE_FORMAT=(type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

commit;
