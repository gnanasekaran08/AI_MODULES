-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: department_prediction
-- ------------------------------------------------------
-- Server version	8.4.10-0ubuntu0.26.04.1

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
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL,
  `normalized_question` varchar(500) DEFAULT NULL,
  `department` varchar(100) NOT NULL,
  `division` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `normalized_question` (`normalized_question`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'How would you rate the doctor\'s punctuality?',NULL,'OPD','General Medicine'),(2,'Was the doctor available at your scheduled appointment time?',NULL,'OPD','General Medicine'),(3,'Did the doctor explain your medical condition clearly?',NULL,'OPD','General Medicine'),(4,'Were your concerns listened to carefully by the doctor?',NULL,'OPD','General Medicine'),(5,'Did you receive enough time during your consultation?',NULL,'OPD','General Medicine'),(6,'Were the treatment options explained properly?',NULL,'OPD','General Medicine'),(7,'Did the doctor answer all your questions satisfactorily?',NULL,'OPD','General Medicine'),(8,'Was the consultation process smooth and organized?',NULL,'OPD','General Medicine'),(9,'Did you feel comfortable discussing your health issues?',NULL,'OPD','General Medicine'),(10,'Would you recommend this doctor to others?',NULL,'OPD','General Medicine'),(11,'Was the orthopedic doctor available on time?',NULL,'OPD','Orthopedics'),(12,'Did the orthopedic doctor explain your injury properly?',NULL,'OPD','Orthopedics'),(13,'Were your X-ray reports reviewed carefully?',NULL,'OPD','Orthopedics'),(14,'Was the treatment plan explained clearly?',NULL,'OPD','Orthopedics'),(15,'Did you receive proper advice regarding your recovery?',NULL,'OPD','Orthopedics'),(16,'Were your mobility concerns addressed?',NULL,'OPD','Orthopedics'),(17,'Did the doctor recommend appropriate exercises?',NULL,'OPD','Orthopedics'),(18,'Was the consultation satisfactory?',NULL,'OPD','Orthopedics'),(19,'Were your follow-up instructions clear?',NULL,'OPD','Orthopedics'),(20,'Would you revisit this orthopedic department?',NULL,'OPD','Orthopedics'),(21,'Was the pediatric doctor friendly towards your child?',NULL,'OPD','Pediatrics'),(22,'Did the doctor explain your child\'s condition clearly?',NULL,'OPD','Pediatrics'),(23,'Was your child treated with care?',NULL,'OPD','Pediatrics'),(24,'Did the doctor answer all your questions?',NULL,'OPD','Pediatrics'),(25,'Was the consultation comfortable for your child?',NULL,'OPD','Pediatrics'),(26,'Were vaccination details explained properly?',NULL,'OPD','Pediatrics'),(27,'Did you receive proper dietary advice for your child?',NULL,'OPD','Pediatrics'),(28,'Was enough consultation time provided?',NULL,'OPD','Pediatrics'),(29,'Would you recommend this pediatric department?',NULL,'OPD','Pediatrics'),(30,'Overall, were you satisfied with the pediatric consultation?',NULL,'OPD','Pediatrics'),(31,'Were the nurses attentive to your needs?',NULL,'IPD','Nursing'),(32,'Did nurses respond quickly when assistance was needed?',NULL,'IPD','Nursing'),(33,'Were medications administered on time?',NULL,'IPD','Nursing'),(34,'Did the nurses communicate politely?',NULL,'IPD','Nursing'),(35,'Were your questions answered by the nursing staff?',NULL,'IPD','Nursing'),(36,'Did nurses monitor your condition regularly?',NULL,'IPD','Nursing'),(37,'Were emergency requests handled promptly?',NULL,'IPD','Nursing'),(38,'Did the nurses explain procedures before performing them?',NULL,'IPD','Nursing'),(39,'Were you treated respectfully by the nursing staff?',NULL,'IPD','Nursing'),(40,'Were shift changes handled smoothly?',NULL,'IPD','Nursing'),(41,'Was the food served at the correct temperature?',NULL,'Dietary','Kitchen'),(42,'Did the food meet your dietary requirements?',NULL,'Dietary','Kitchen'),(43,'Was the food served on time?',NULL,'Dietary','Kitchen'),(44,'Were meals hygienically prepared?',NULL,'Dietary','Kitchen'),(45,'Was the taste of the food satisfactory?',NULL,'Dietary','Kitchen'),(46,'Did you receive the correct meal?',NULL,'Dietary','Kitchen'),(47,'Was the portion size adequate?',NULL,'Dietary','Kitchen'),(48,'Was the food fresh?',NULL,'Dietary','Kitchen'),(49,'Did the kitchen staff respond to special requests?',NULL,'Dietary','Kitchen'),(50,'Overall, were you satisfied with the food service?',NULL,'Dietary','Kitchen'),(51,'Were prescribed medicines available?',NULL,'Pharmacy','Pharmacy'),(52,'Was the medicine issued without delay?',NULL,'Pharmacy','Pharmacy'),(53,'Did the pharmacist explain dosage instructions?',NULL,'Pharmacy','Pharmacy'),(54,'Were medicine labels clear?',NULL,'Pharmacy','Pharmacy'),(55,'Did you receive all prescribed medicines?',NULL,'Pharmacy','Pharmacy'),(56,'Were alternative medicines explained when necessary?',NULL,'Pharmacy','Pharmacy'),(57,'Was the pharmacy staff courteous?',NULL,'Pharmacy','Pharmacy'),(58,'Was your waiting time at the pharmacy reasonable?',NULL,'Pharmacy','Pharmacy'),(59,'Was the billing for medicines accurate?',NULL,'Pharmacy','Pharmacy'),(60,'Overall, were you satisfied with the pharmacy service?',NULL,'Pharmacy','Pharmacy'),(61,'Was your bill generated accurately?',NULL,'Billing','Accounts'),(62,'Were billing charges explained clearly?',NULL,'Billing','Accounts'),(63,'Was the billing process completed quickly?',NULL,'Billing','Accounts'),(64,'Did the billing staff answer your questions?',NULL,'Billing','Accounts'),(65,'Were payment options explained properly?',NULL,'Billing','Accounts'),(66,'Did you receive the correct receipt?',NULL,'Billing','Accounts'),(67,'Was insurance processing handled efficiently?',NULL,'Billing','Accounts'),(68,'Were there any unexpected charges?',NULL,'Billing','Accounts'),(69,'Was the billing counter organized?',NULL,'Billing','Accounts'),(70,'Overall, were you satisfied with the billing service?',NULL,'Billing','Accounts'),(71,'Was your room cleaned regularly?',NULL,'Housekeeping','Housekeeping'),(72,'Were the washrooms kept clean?',NULL,'Housekeeping','Housekeeping'),(73,'Was the hospital environment hygienic?',NULL,'Housekeeping','Housekeeping'),(74,'Did housekeeping staff respond promptly?',NULL,'Housekeeping','Housekeeping'),(75,'Were bedsheets changed regularly?',NULL,'Housekeeping','Housekeeping'),(76,'Were dustbins emptied on time?',NULL,'Housekeeping','Housekeeping'),(77,'Was the room free from unpleasant odors?',NULL,'Housekeeping','Housekeeping'),(78,'Were cleaning staff polite?',NULL,'Housekeeping','Housekeeping'),(79,'Was your room maintained throughout your stay?',NULL,'Housekeeping','Housekeeping'),(80,'Overall, were you satisfied with housekeeping?',NULL,'Housekeeping','Housekeeping'),(81,'Were your laboratory reports delivered on time?',NULL,'Laboratory','Lab'),(82,'Was the sample collection process smooth?',NULL,'Laboratory','Lab'),(83,'Were lab technicians professional?',NULL,'Laboratory','Lab'),(84,'Were your reports accurate and easy to understand?',NULL,'Laboratory','Lab'),(85,'Overall, were you satisfied with the laboratory services?',NULL,'Laboratory','Lab'),(86,'How was the experience with the hospital','how was the experience with the hospital','General','Common');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-30 22:11:06
