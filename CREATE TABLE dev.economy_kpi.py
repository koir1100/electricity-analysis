CREATE TABLE dev.raw_data.economy_kpi(
    year1 int primary key,
    percentage_of_ratio DOUBLE PRECISION
);

-- AWS 자격 증명은 코드에서 직접 입력하지 않습니다.
COPY INTO dev.raw_data.economy_kpi
FROM 's3://semlabbucket123/test_data/경제지표.csv'
credentials=(AWS_KEY_ID=$AWS_KEY_ID AWS_SECRET_KEY=$AWS_SECRET_KEY)
FILE_FORMAT=(type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

SELECT * FROM dev.raw_data.economy_kpi;
