CREATE DATABASE  IF NOT EXISTS `webhw` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `webhw`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: webhw
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `idorder` int NOT NULL,
  `iduser` int DEFAULT NULL,
  `iditem` int DEFAULT NULL,
  `count` decimal(2,0) DEFAULT NULL,
  PRIMARY KEY (`idorder`),
  KEY `orderitem_idx` (`iditem`),
  KEY `itemuser_idx` (`iduser`),
  CONSTRAINT `cartitem` FOREIGN KEY (`iditem`) REFERENCES `item` (`iditem`),
  CONSTRAINT `cartuser` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (2,1,6,1),(3,1,4,1),(5,1,2,1),(6,1,3,1),(7,1,9,1),(8,1,7,1),(9,2,27,1),(10,2,12,1),(11,6,25,1),(12,5,10,1),(13,2,21,1),(14,2,7,1),(15,2,10,1),(16,2,26,1),(17,2,28,1),(18,2,19,1),(19,2,27,1),(20,2,6,1);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image` (
  `idimage` int NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `iditem` int DEFAULT NULL,
  PRIMARY KEY (`idimage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `iditem` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `price` decimal(5,0) DEFAULT NULL,
  `image` text,
  `image2` text,
  `image3` text,
  `image4` text,
  `species` int DEFAULT NULL,
  `desc` varchar(45) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`iditem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'男士卫衣',159,'1.png','1-2.png','1-3.png','1-4.png',1,'青春流行，宽松','2022-08-16 16:15:10'),(2,'青花瓷',99,'100.png','100-2.png','100-3.png','100-4.png',2,'青花缠枝莲中号赏瓶','2022-08-16 16:15:16'),(3,'绿联充电宝',429,'12.jpg','12-2.png','12-3.png','12-4.png',3,'100W笔记本电脑专用,145W大功率快充,便携移动电源','2022-08-16 16:15:26'),(4,'高等数学（同济版）',50,'13.jpg','13-2.png','13-3.png','13-4.png',4,'高等数学教材','2022-08-16 16:15:44'),(5,'2024考研真相英语一',35,'15.png','15-2.png','15-3.png','15-4.png',4,'包含2003-2023共20年真题','2022-08-16 16:16:05'),(6,'NVIDIA英伟达盒装RTX4090显卡24G',8990,'3.png','3-2.png','3-3.png','3-4.png',3,'24G显存','2023-05-16 16:16:29'),(7,'大疆入门级遥控无人机',698,'5.png','5-2.png','5-3.png','5-4.png',3,'无刷电机，高清电调摄像头','2022-08-16 16:16:50'),(8,'2022李永乐复习全书基础篇',54,'6.png','6-2.png','6-3.png','6-4.png',4,'22考研数学','2023-04-16 16:17:09'),(9,'大疆DJI专业摄像机',3600,'7.png','7-2.png','7-3.png','7-4.png',3,'5.5英寸，三轴防抖，专业级','2022-08-16 16:17:24'),(10,'casio电子手表男士',866,'9.jpg','9-2.jpg','9-3.jpg','9-4.jpg',1,'GA-110,防震防磁,全自动日历等','2022-08-16 16:17:47'),(11,'纸质笔记本',6,'bjb.jpg','bjb-2.jpg','bjb-3.jpg','bjb-4.jpg',4,'物美价廉轻松笔记本办公用品','2022-08-16 16:17:55'),(12,'Jeep山地自行车',679,'zxc.jpg','zxc-2.jpg','zxc-3.jpg','zxc-4.jpg',5,'男女式变速单车镁合金油刹27.5寸','2022-08-16 16:18:08'),(13,'帆布袋',20,'fbd.jpg','fbd-2.jpg','fbd-3.jpg','fbd-4.jpg',1,'典雅，时尚通勤购物袋，ins手提单肩托特包','2022-08-16 16:18:26'),(14,'电镀哑铃',3200,'yl.jpg','yl-2.jpg','yl-3.jpg','yl-4.jpg',5,'六角哑铃套装','2022-08-16 16:18:37'),(15,'雅戈尔短袖衬衫',68,'chenshan.jpg','chenshan-2.jpg','chenshan-3.jpg','chenshan-4.jpg',1,'男式,商务,正装','2022-08-16 16:18:56'),(16,'沙宣柔顺去屑洗发水',99,'xfs.jpg','xfs-2.jpg','xfs-3.jpg','xfs-4.jpg',6,'美妆护肤','2022-08-16 16:19:11'),(17,'良品铺子红豆三明治',39,'smz.jpg','smz-2.jpg','smz-3.jpg','smz-4.jpg',7,'红豆味400g送果粒味400g，临海市璐哥食品有限公司','2022-08-16 16:19:31'),(18,'沙宣男士哑光蓬松定型发泥',50,'fani.jpg','fani-2.jpg','fani-3.jpg','fani-4.jpg',6,'自然蓬松,清香型,持久定型','2022-08-16 16:19:46'),(19,'kdst拳击沙袋',99,'qjsd.jpg','qjsd-2.jpg','qjsd-3.jpg','qjsd-4.jpg',5,'减压，立式，沙袋','2022-08-16 16:20:05'),(20,'激光投影虚拟镭射键盘',299,'xnjp.jpg','xnjp-2.jpg','xnjp-3.jpg','xnjp-4.jpg',3,'无线蓝牙无线3d投屏触控','2022-08-16 16:20:29'),(21,'李宁握力器',26,'wlq.jpg','wlq-2.jpg','wlq-3.jpg','wlq-4.jpg',5,'电子款计数','2022-08-16 16:20:43'),(22,'露营收纳箱',23,'snx.jpg','snx-2.jpg','snx-3.jpg','snx-4.jpg',5,'车载，折叠','2022-08-16 16:20:52'),(23,'电蚊拍充电式',25,'dwp.jpg','dwp-2.jpg','dwp-3.jpg','dwp-4.jpg',8,'家用，锂电池，超强力灭蚊','2022-08-16 16:21:15'),(24,'飞利浦机械键盘',109,'jxjp.jpg','jxjp-2.jpg','jxjp-3.jpg','jxjp-4.jpg',3,'办公，有线','2022-08-16 16:21:30'),(25,'折叠水桶',13,'zdst.jpg','zdst-2.jpg','zdst-3.jpg','zdst-4.jpg',5,'户外钓鱼，车载洗车桶','2022-08-16 16:21:42'),(26,'新飞迷你小型冰箱',139,'xxbx.jpg','xxbx-2.jpg','xxbx-3.jpg','xxbx-4.jpg',8,'学生宿舍，车载家用','2022-08-16 16:21:56'),(27,'小型多功能电煮锅',100,'dzg.jpg','dzg-2.jpg','dzg-3.jpg','dzg-4.jpg',8,'智能款，5款火力，700W','2022-08-16 16:22:17'),(28,'迷你小电视',156,'monixds.jpg','monixds-2.jpg','monixds-3.jpg','monixds-4.jpg',3,'触摸屏，易操作，usb充电','2022-08-16 16:22:44');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `merchant`
--

DROP TABLE IF EXISTS `merchant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `merchant` (
  `id` int DEFAULT '5',
  `iditem` int DEFAULT NULL,
  `image` text,
  `image2` text,
  `image3` text,
  `image4` text,
  `species` int DEFAULT NULL,
  `store` int DEFAULT NULL,
  `price` decimal(5,0) DEFAULT NULL,
  `desc` varchar(45) DEFAULT NULL,
  `creatime` datetime NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`creatime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchant`
--

LOCK TABLES `merchant` WRITE;
/*!40000 ALTER TABLE `merchant` DISABLE KEYS */;
INSERT INTO `merchant` VALUES (5,1,'1.png','1-2.png','1-3.png','1-4.png',1,200,159,'青春流行，宽松','2022-08-16 16:15:10','男士卫衣'),(5,2,'100.png','100-2.png','100-3.png','100-4.png',2,200,99,'青花缠枝莲中号赏瓶','2022-08-16 16:15:16','青花瓷'),(5,3,'12.jpg','12-2.png','12-3.png','12-4.png',3,200,429,'100W笔记本电脑专用,145W大功率快充,便携移动电源','2022-08-16 16:15:26','绿联充电宝'),(5,4,'13.jpg','13-2.png','13-3.png','13-4.png',4,200,50,'高等数学教材','2022-08-16 16:15:44','高等数学（同济版）'),(5,5,'15.png','15-2.png','15-3.png','15-4.png',4,200,35,'包含2003-2023共20年真题','2022-08-16 16:16:05','2024考研真相英语一'),(5,7,'5.png','5-2.png','5-3.png','5-4.png',3,200,698,'无刷电机，高清电调摄像头','2022-08-16 16:16:50','大疆入门级遥控无人机'),(5,9,'7.png','7-2.png','7-3.png','7-4.png',3,200,3600,'5.5英寸，三轴防抖，专业级','2022-08-16 16:17:24','大疆DJI专业摄像机'),(5,10,'9.jpg','9-2.jpg','9-3.jpg','9-4.jpg',1,200,866,'GA-110,防震防磁,全自动日历等','2022-08-16 16:17:47','casio电子手表男士'),(5,11,'bjb.jpg','bjb-2.jpg','bjb-3.jpg','bjb-4.jpg',4,200,6,'物美价廉轻松笔记本办公用品','2022-08-16 16:17:55','纸质笔记本'),(5,12,'zxc.jpg','zxc-2.jpg','zxc-3.jpg','zxc-4.jpg',5,200,679,'男女式变速单车镁合金油刹27.5寸','2022-08-16 16:18:08','Jeep山地自行车'),(5,13,'fbd.jpg','fbd-2.jpg','fbd-3.jpg','fbd-4.jpg',1,200,20,'典雅，时尚通勤购物袋，ins手提单肩托特包','2022-08-16 16:18:26','帆布袋'),(5,14,'yl.jpg','yl-2.jpg','yl-3.jpg','yl-4.jpg',5,200,3200,'六角哑铃套装','2022-08-16 16:18:37','电镀哑铃'),(5,15,'chenshan.jpg','chenshan-2.jpg','chenshan-3.jpg','chenshan-4.jpg',1,200,68,'男式,商务,正装','2022-08-16 16:18:56','雅戈尔短袖衬衫'),(5,16,'xfs.jpg','xfs-2.jpg','xfs-3.jpg','xfs-4.jpg',6,200,99,'美妆护肤','2022-08-16 16:19:11','沙宣柔顺去屑洗发水'),(5,17,'smz.jpg','smz-2.jpg','smz-3.jpg','smz-4.jpg',7,200,39,'红豆味400g送果粒味400g，临海市璐哥食品有限公司','2022-08-16 16:19:31','良品铺子红豆三明治'),(5,18,'fani.jpg','fani-2.jpg','fani-3.jpg','fani-4.jpg',6,200,50,'自然蓬松,清香型,持久定型','2022-08-16 16:19:46','沙宣男士哑光蓬松定型发泥'),(5,19,'qjsd.jpg','qjsd-2.jpg','qjsd-3.jpg','qjsd-4.jpg',5,200,99,'减压，立式，沙袋','2022-08-16 16:20:05','kdst拳击沙袋'),(5,20,'xnjp.jpg','xnjp-2.jpg','xnjp-3.jpg','xnjp-4.jpg',3,200,299,'无线蓝牙无线3d投屏触控','2022-08-16 16:20:29','激光投影虚拟镭射键盘'),(5,21,'wlq.jpg','wlq-2.jpg','wlq-3.jpg','wlq-4.jpg',5,200,26,'电子款计数','2022-08-16 16:20:43','李宁握力器'),(5,22,'snx.jpg','snx-2.jpg','snx-3.jpg','snx-4.jpg',5,200,23,'车载，折叠','2022-08-16 16:20:52','露营收纳箱'),(5,23,'dwp.jpg','dwp-2.jpg','dwp-3.jpg','dwp-4.jpg',8,200,25,'家用，锂电池，超强力灭蚊','2022-08-16 16:21:15','电蚊拍充电式'),(5,24,'jxjp.jpg','jxjp-2.jpg','jxjp-3.jpg','jxjp-4.jpg',3,200,109,'办公，有线','2022-08-16 16:21:30','飞利浦机械键盘'),(5,25,'zdst.jpg','zdst-2.jpg','zdst-3.jpg','zdst-4.jpg',5,200,13,'户外钓鱼，车载洗车桶','2022-08-16 16:21:42','折叠水桶'),(5,26,'xxbx.jpg','xxbx-2.jpg','xxbx-3.jpg','xxbx-4.jpg',8,200,139,'学生宿舍，车载家用','2022-08-16 16:21:56','新飞迷你小型冰箱'),(5,27,'dzg.jpg','dzg-2.jpg','dzg-3.jpg','dzg-4.jpg',8,200,100,'智能款，5款火力，700W','2022-08-16 16:22:17','小型多功能电煮锅'),(5,28,'monixds.jpg','monixds-2.jpg','monixds-3.jpg','monixds-4.jpg',3,200,156,'触摸屏，易操作，usb充电','2022-08-16 16:22:44','迷你小电视'),(5,8,'6.png','6-2.png','6-3.png','6-4.png',4,200,54,'22考研数学','2023-04-16 16:17:09','2022李永乐复习全书基础篇'),(5,6,'3.png','3-2.png','3-3.png','3-4.png',3,200,8990,'24G显存','2023-05-16 16:16:29','NVIDIA英伟达盒装RTX4090显卡24G');
/*!40000 ALTER TABLE `merchant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `idorder` int NOT NULL,
  `iduser` text,
  `idmerchant` text,
  `iditem` text,
  `ifecho` int DEFAULT NULL,
  `price` text,
  `total` int DEFAULT NULL,
  `item_num` text,
  `time` datetime NOT NULL,
  PRIMARY KEY (`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,'2','root','27,12,21,7,10,26,28,19,27',0,'100,679,26,698,866,139,156,99,100',2863,'1,1,1,1,1,1,1,1,1','2023-06-12 19:35:19'),(2,'2','root','27,28,19',0,'100,156,198',454,'1,1,2','2023-06-12 20:31:54'),(3,'2','root','6',1,'8990',8990,'1','2023-06-12 21:15:13');
INSERT INTO `order` VALUES (4,'1','7','1,2,3,4,5',1,'159,99,429,50,35',712,'1,1,1,1,1','2023-02-12 19:35:19');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `auth` int DEFAULT NULL,
  `address` text,
  PRIMARY KEY (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'wz','1726307829@qq.com',NULL,'111','2023-05-16 14:30:50',1,'ss省ss市ss小区'),(2,'2326','wwtt232623226@gmail.com',NULL,'111','2023-06-06 17:11:55',2,'xx省xx市xx街道xx号'),(3,'王某','2179739766@qq.com',NULL,'111','2023-06-06 17:14:38',1,NULL),(4,'r23m','21@qq.com',NULL,'111','2023-06-06 19:56:45',2,NULL),(5,'root','root@123.com','13105268912','111','2023-06-06 19:56:41',2,'xx省xx市xx街道xx号'),(6,'26','23@23.com',NULL,'111','2023-06-09 15:35:59',2,NULL);
INSERT INTO `user` VALUES (7,'张三','1234@qq.com',10088,'123456','2023-06-06 14:30:50',1,'xx省xx市xx小区');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'webhw'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-12 21:24:36

CREATE TABLE IF NOT EXISTS `comments` (
  `created_at` datetime NOT NULL,
  `username` VARCHAR(255) NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `comment` TEXT NOT NULL,
  PRIMARY KEY (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `comments` VALUES ('2023-05-16 14:30:50', 'ljq', '青花瓷', '这个青花瓷太酷了！');