-- Creates the table hbtn_0d_usa with table states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;  -- Switch to the created database

CREATE TABLE IF NOT EXISTS `states` (
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)
);.
