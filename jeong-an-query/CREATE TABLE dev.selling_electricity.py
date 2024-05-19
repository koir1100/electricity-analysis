CREATE TABLE dev.raw_data.selling_electricity (
    year1 int primary key,
    house_selling DOUBLE PRECISION,
    general_selling DOUBLE PRECISION,
    education_selling DOUBLE PRECISION,
    industrial_selling DOUBLE PRECISION,
    farming_selling DOUBLE PRECISION,
    streetlight_selling DOUBLE PRECISION,
    latenight_selling DOUBLE PRECISION,
    total_selling DOUBLE PRECISION
);

-- AWS 자격 증명은 코드에서 직접 입력하지 않습니다.
COPY INTO dev.raw_data.selling_electricity
FROM 's3://semlabbucket123/test_data/electricity_selling.csv'
credentials=(AWS_KEY_ID=$AWS_KEY_ID AWS_SECRET_KEY=$AWS_SECRET_KEY)
FILE_FORMAT=(type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

SELECT * FROM dev.raw_data.selling_electricity;
