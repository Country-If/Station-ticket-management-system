/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : ticket_management_system

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2022-01-04 01:55:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for train_information
-- ----------------------------
DROP TABLE IF EXISTS `train_information`;
CREATE TABLE `train_information` (
  `train_id` varchar(255) NOT NULL,
  `departure` varchar(255) NOT NULL,
  `destination` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `departure_time` time NOT NULL,
  `arrival_time` time NOT NULL,
  PRIMARY KEY (`train_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
