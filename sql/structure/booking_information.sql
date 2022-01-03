/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : ticket_management_system

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2022-01-04 01:55:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for booking_information
-- ----------------------------
DROP TABLE IF EXISTS `booking_information`;
CREATE TABLE `booking_information` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `train_id` varchar(255) NOT NULL,
  `seat_id` varchar(255) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`booking_id`),
  KEY `user_name` (`user_name`),
  KEY `train_id` (`train_id`,`seat_id`),
  CONSTRAINT `booking_information_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `user_information` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking_information_ibfk_2` FOREIGN KEY (`train_id`, `seat_id`) REFERENCES `seat_information` (`train_id`, `seat_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
