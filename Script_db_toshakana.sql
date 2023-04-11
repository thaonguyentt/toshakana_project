
# create table toshakana 

CREATE TABLE toshakana (
    id INT NOT NULL AUTO_INCREMENT,
    gift_detail VARCHAR(255) NOT NULL,
    gift_description VARCHAR(255) NOT NULL,
    name_recipient VARCHAR(255) NOT NULL,
    Affiliation VARCHAR(255) NOT NULL,
    sent_date DATE NOT NULL,
    Assessed_Value int NOT null,
    Retention_Cost int NOT null,
    Retained VARCHAR(10) NOT NULL,
    Remarks VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);


# create table histor weather
CREATE TABLE weather  (
    id INT NOT NULL AUTO_INCREMENT,
    format_date VARCHAR(255),
    summary VARCHAR(255),
    precip_type VARCHAR(255),
    temperature FLOAT,
    apparent_temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    wind_bearing FLOAT,
    visibility FLOAT,
    loud_cover FLOAT,
    pressure FLOAT,
    daily_summary VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

DROP TABLE weather2;


#tao bang fake
CREATE TABLE weather2  (
    format_date VARCHAR(255),
    summary VARCHAR(255),
    precip_type VARCHAR(255),
    temperature DECIMAL(2,16),
    apparent_temperature DECIMAL(16,16),
    humidity DECIMAL(2,2),
    wind_speed DECIMAL(16,16),
    wind_bearing DECIMAL(3,1),
    visibility DECIMAL(16,16),
    loud_cover DECIMAL(1,1),
    pressure DECIMAL(4,2),
    daily_summary VARCHAR(255) NOT NULL
);

LOAD DATA INFILE '/usr/local/weatherHistory.csv' 
INTO TABLE weather2 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
