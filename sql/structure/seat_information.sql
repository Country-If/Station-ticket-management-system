/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : ticket_management_system

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2022-01-04 01:55:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for seat_information
-- ----------------------------
DROP TABLE IF EXISTS `seat_information`;
CREATE TABLE `seat_information` (
  `train_id` varchar(255) NOT NULL,
  `seat_id` varchar(225) NOT NULL,
  `rank` varchar(50) NOT NULL,
  `price` int NOT NULL,
  `is_used` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`train_id`,`seat_id`),
  CONSTRAINT `seat_information_ibfk_1` FOREIGN KEY (`train_id`) REFERENCES `train_information` (`train_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
