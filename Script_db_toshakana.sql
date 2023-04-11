
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
    temperature VARCHAR(255),
    apparent_temperature VARCHAR(255),
    humidity VARCHAR(255),
    wind_speed VARCHAR(255),
    wind_bearing VARCHAR(255),
    visibility VARCHAR(255),
    loud_cover VARCHAR(255),
    pressure VARCHAR(255),
    daily_summary VARCHAR(255),
    PRIMARY KEY (id)
);

DROP TABLE weather2;
DROP TABLE weather;


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
INSERT INTO weather (format_date, summary, precip_type, temperature, apparent_temperature, humidity, wind_speed,wind_bearing, visibility, loud_cover, pressure, daily_summary)
SELECT format_date, summary, precip_type, temperature, apparent_temperature, humidity, wind_speed,wind_bearing, visibility, loud_cover, pressure, daily_summary
 FROM weather2;

select count(*) from weather2;
