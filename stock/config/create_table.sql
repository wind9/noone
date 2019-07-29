
Create Table

CREATE TABLE `stock_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coop_code` varchar(100) DEFAULT NULL,
  `coop_name` varchar(100) DEFAULT NULL,
  `stock_code` varchar(100) DEFAULT NULL,
  `stock_name` varchar(100) DEFAULT NULL,
  `reg_date` date DEFAULT NULL,
  `total_share` bigint(11) DEFAULT NULL,
  `circulating_share` bigint(11) DEFAULT NULL,
  `industry` varchar(100) DEFAULT NULL,
  `security_type` varchar(100) DEFAULT NULL,
  `market` varchar(100) DEFAULT NULL,
  `other1` varchar(100) DEFAULT NULL,
  `other2` varchar(100) DEFAULT NULL,
  `other3` varchar(100) DEFAULT NULL,
  `other4` varchar(100) DEFAULT NULL,
  `other5` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3762 DEFAULT CHARSET=utf8