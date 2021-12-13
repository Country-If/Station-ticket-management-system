/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : ticket_management_system

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-12-13 21:44:03
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
  PRIMARY KEY (`train_id`),
  KEY `date` (`date`),
  KEY `departure_time` (`departure_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of train_information
-- ----------------------------
INSERT INTO `train_information` VALUES ('D2336', '北京', '厦门', '2022-01-16', '06:38:00', '09:12:00');
INSERT INTO `train_information` VALUES ('D2920', '杭州', '北京', '2022-01-21', '00:04:00', '01:43:00');
INSERT INTO `train_information` VALUES ('D3971', '上海', '天津', '2022-01-27', '10:28:00', '13:46:00');
INSERT INTO `train_information` VALUES ('D3998', '南京', '广州', '2022-02-03', '10:12:00', '13:59:00');
INSERT INTO `train_information` VALUES ('D7957', '珠海', '厦门', '2022-01-17', '18:47:00', '20:46:00');
INSERT INTO `train_information` VALUES ('D8003', '天津', '珠海', '2022-01-29', '20:44:00', '00:41:00');
INSERT INTO `train_information` VALUES ('D9528', '桂林', '佛山', '2022-02-02', '06:36:00', '08:36:00');
INSERT INTO `train_information` VALUES ('G5299', '西安', '上海', '2022-01-28', '07:11:00', '10:07:00');
INSERT INTO `train_information` VALUES ('G6394', '上海', '厦门', '2022-01-24', '01:54:00', '03:05:00');
INSERT INTO `train_information` VALUES ('G6777', '佛山', '南京', '2022-01-19', '02:43:00', '06:34:00');
INSERT INTO `train_information` VALUES ('G8783', '北京', '西安', '2022-01-27', '23:08:00', '02:14:00');
INSERT INTO `train_information` VALUES ('K3686', '南京', '厦门', '2022-01-29', '08:27:00', '12:32:00');
INSERT INTO `train_information` VALUES ('K4106', '桂林', '北京', '2022-01-25', '09:06:00', '12:48:00');
INSERT INTO `train_information` VALUES ('K8037', '上海', '珠海', '2022-01-15', '04:31:00', '07:48:00');
INSERT INTO `train_information` VALUES ('L2397', '杭州', '佛山', '2022-01-23', '13:08:00', '16:49:00');
INSERT INTO `train_information` VALUES ('L2970', '厦门', '上海', '2022-01-21', '16:46:00', '19:43:00');
INSERT INTO `train_information` VALUES ('L3546', '上海', '杭州', '2022-01-30', '06:26:00', '08:23:00');
INSERT INTO `train_information` VALUES ('L6163', '桂林', '成都', '2022-01-26', '08:17:00', '10:36:00');
INSERT INTO `train_information` VALUES ('L8229', '深圳', '成都', '2022-02-05', '02:02:00', '03:12:00');
INSERT INTO `train_information` VALUES ('L9005', '厦门', '北京', '2022-02-01', '08:46:00', '12:24:00');
