/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : ticket_management_system

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2022-01-04 01:55:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user_information
-- ----------------------------
DROP TABLE IF EXISTS `user_information`;
CREATE TABLE `user_information` (
  `user_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
