/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : ticket_management_system

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-12-13 21:43:48
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
  `date` date NOT NULL,
  `departure_time` time NOT NULL,
  `rank` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` int NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`booking_id`),
  KEY `booking-information_ibfk_1` (`train_id`),
  KEY `seat_id` (`seat_id`) USING BTREE,
  KEY `departure_time` (`departure_time`) USING BTREE,
  KEY `booking-information_ibfk_3` (`date`),
  KEY `booking-information_ibfk_5` (`rank`),
  KEY `booking-information_ibfk_6` (`price`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `booking-information_ibfk_1` FOREIGN KEY (`train_id`) REFERENCES `seat_information` (`train_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking-information_ibfk_3` FOREIGN KEY (`date`) REFERENCES `train_information` (`date`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking-information_ibfk_4` FOREIGN KEY (`departure_time`) REFERENCES `train_information` (`departure_time`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking-information_ibfk_5` FOREIGN KEY (`rank`) REFERENCES `seat_information` (`rank`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking-information_ibfk_6` FOREIGN KEY (`price`) REFERENCES `seat_information` (`price`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking_information_ibfk_1` FOREIGN KEY (`seat_id`) REFERENCES `seat_information` (`seat_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking_information_ibfk_2` FOREIGN KEY (`user_name`) REFERENCES `user_information` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of booking_information
-- ----------------------------
