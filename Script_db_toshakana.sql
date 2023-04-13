
-- CREATE TABLE df (
--     summary VARCHAR(255),
--     precip_type VARCHAR(255),
--     temperature VARCHAR(255),
--     apparent_temperature VARCHAR(255),
--     humidity VARCHAR(255),
--     wind_speed VARCHAR(255),
--     wind_bearing VARCHAR(255),
--     visibility VARCHAR(255),
--     loud_cover VARCHAR(255),
--     pressure VARCHAR(255),
--     date_ VARCHAR(255),
--     formatted_year VARCHAR(255),
--     formatted_month VARCHAR(255),
--     formatted_week VARCHAR(255),
--     formatted_day VARCHAR(255),
--     formatted_dayofweek VARCHAR(255),
--     formatted_dayofyear VARCHAR(255),
--     formatted_is_month_end VARCHAR(255),
--     formatted_is_month_start VARCHAR(255),
--     formatted_is_quarter_end VARCHAR(255),
--     formatted_is_quarter_start VARCHAR(255),
--     formatted_is_year_end VARCHAR(255),
--     formatted_is_year_start VARCHAR(255),
--     formatted_elapsed VARCHAR(255),
--     season VARCHAR(255),
--     hour_ VARCHAR(255),
--     timing VARCHAR(255)
-- );


drop table df;


CREATE TABLE df (
    summary VARCHAR(255),
    precip_type VARCHAR(255),
    temperature float,
    apparent_temperature float,
    humidity float,
    wind_speed float,
    wind_bearing float,
    visibility float,
    loud_cover float,
    pressure float,
    date_ VARCHAR(255),
    formatted_year int,
    formatted_month int,
    formatted_week int,
    formatted_day int,
    formatted_dayofweek int,
    formatted_dayofyear int,
    formatted_is_month_end VARCHAR(255),
    formatted_is_month_start VARCHAR(255),
    formatted_is_quarter_end VARCHAR(255),
    formatted_is_quarter_start VARCHAR(255),
    formatted_is_year_end VARCHAR(255),
    formatted_is_year_start VARCHAR(255),
    formatted_elapsed float,
    season VARCHAR(255),
    hour_ int,
    timing VARCHAR(255)
);


#load data vao bang fake
LOAD DATA INFILE '/usr/local/df.csv' #su dung cho dung duong link nha, khong phai 
# file nao mariadb cung thay duoc
INTO TABLE df 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


CREATE TABLE resampled_df (
    temperature VARCHAR(255),
    apparent_temperature VARCHAR(255),
    humidity VARCHAR(255),
    wind_speed VARCHAR(255),
    wind_bearing VARCHAR(255),
    visibility VARCHAR(255),
    loud_cover VARCHAR(255),
    pressure VARCHAR(255)
);

drop table resampled_df;
CREATE TABLE resampled_df (
    temperature float,
    apparent_temperature float,
    humidity float,
    wind_speed float,
    wind_bearing float,
    visibility float,
    loud_cover float,
    pressure float
);

LOAD DATA INFILE '/usr/local/resampled_df.csv' #su dung cho dung duong link nha, khong phai 
# file nao mariadb cung thay duoc
INTO TABLE resampled_df
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


drop table resampled_days;

CREATE TABLE resampled_days (
    temperature float,
    apparent_temperature float,
    humidity float,
    wind_speed float,
    wind_bearing float,
    visibility float,
    loud_cover float,
    pressure float
);

LOAD DATA INFILE '/usr/local/resampled_df.csv' #su dung cho dung duong link nha, khong phai 
# file nao mariadb cung thay duoc
INTO TABLE resampled_days
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;




# create table histor weather
CREATE TABLE weather(
    id INT NOT NULL AUTO_INCREMENT,
    format_date VARCHAR(255),
    summary VARCHAR(255),
    precip_type VARCHAR(255),
    temperature VARCHAR(255),
    apparent_temperature VARCHAR(255),
    humidity VARCHAR(255),
    wind_speed VARCHAR(255),
    wind_bearing VARCHAR(255),
    visibility VARCHAR(255),
    loud_cover VARCHAR(255),
    pressure VARCHAR(255),
    PRIMARY KEY (id)
);

DROP TABLE resampled_days;
DROP TABLE weather1;


#tao bang fake
CREATE TABLE weather2  (
    format_date VARCHAR(255),
    summary VARCHAR(255),
    precip_type VARCHAR(255),
    temperature VARCHAR(255),
    apparent_temperature VARCHAR(255),
    humidity VARCHAR(255),
    wind_speed VARCHAR(255),
    wind_bearing VARCHAR(255),
    visibility VARCHAR(255),
    loud_cover VARCHAR(255),
    pressure VARCHAR(255),
    daily_summary VARCHAR(255)
);

#load data vao bang fake
LOAD DATA INFILE '/usr/local/weatherHistory.csv' #su dung cho dung duong link nha, khong phai 
# file nao mariadb cung thay duoc
INTO TABLE weather2 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#insert vao bang chinh
INSERT INTO weather (format_date, summary, precip_type, temperature, apparent_temperature, humidity, wind_speed,wind_bearing, visibility, loud_cover, pressure)
SELECT format_date, summary, precip_type, temperature, apparent_temperature, humidity, wind_speed,wind_bearing, visibility, loud_cover, pressure
 FROM weather2;

select count(*) from weather2;
