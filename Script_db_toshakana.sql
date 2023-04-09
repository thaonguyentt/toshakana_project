
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


