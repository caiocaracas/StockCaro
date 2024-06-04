CREATE DATABASE  IF NOT EXISTS `gerenciador_mercado` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gerenciador_mercado`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: gerenciador_mercado
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `id_compra` int NOT NULL AUTO_INCREMENT,
  `data_compra` datetime DEFAULT NULL,
  `supermercado` varchar(30) DEFAULT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id_compra`),
  KEY `fk_compras_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_compras_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (11,'2024-06-04 16:14:53','Bretas',15),(14,'2024-06-04 16:15:52','Bretas',6),(15,'2024-06-04 16:30:08','EPA',16),(16,'2024-06-04 16:44:54','EPA',16);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dividas`
--

DROP TABLE IF EXISTS `dividas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dividas` (
  `id_divida` int NOT NULL AUTO_INCREMENT,
  `valor` float NOT NULL,
  `data_divida` datetime NOT NULL,
  `data_debito` datetime DEFAULT NULL,
  `beneficiado` int NOT NULL,
  `pagador` int NOT NULL,
  `compra_id` int NOT NULL,
  PRIMARY KEY (`id_divida`),
  KEY `fk_dividas_usuarios1_idx` (`beneficiado`),
  KEY `fk_dividas_usuarios2_idx` (`pagador`),
  KEY `fk_dividas_compras1_idx` (`compra_id`),
  CONSTRAINT `fk_dividas_compras1` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`id_compra`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_dividas_usuarios1` FOREIGN KEY (`beneficiado`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_dividas_usuarios2` FOREIGN KEY (`pagador`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dividas`
--

LOCK TABLES `dividas` WRITE;
/*!40000 ALTER TABLE `dividas` DISABLE KEYS */;
INSERT INTO `dividas` VALUES (9,10,'2024-06-04 17:14:26','2024-06-04 17:15:45',15,16,11);
/*!40000 ALTER TABLE `dividas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_comprados`
--

DROP TABLE IF EXISTS `produtos_comprados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_comprados` (
  `id_produto_comprado` int NOT NULL AUTO_INCREMENT,
  `preco` float DEFAULT NULL,
  `quantidade_comprada` int NOT NULL,
  `produto_residencia_id` int NOT NULL,
  `compra_id` int NOT NULL,
  PRIMARY KEY (`id_produto_comprado`),
  KEY `fk_produtos_comprados_produtos_residencia1_idx` (`produto_residencia_id`),
  KEY `fk_produtos_comprados_compras1_idx` (`compra_id`),
  CONSTRAINT `fk_produtos_comprados_compras1` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`id_compra`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_produtos_comprados_produtos_residencia1` FOREIGN KEY (`produto_residencia_id`) REFERENCES `produtos_residencia` (`id_produto_residencia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_comprados`
--

LOCK TABLES `produtos_comprados` WRITE;
/*!40000 ALTER TABLE `produtos_comprados` DISABLE KEYS */;
INSERT INTO `produtos_comprados` VALUES (6,10,2,27,11);
/*!40000 ALTER TABLE `produtos_comprados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_dispensas`
--

DROP TABLE IF EXISTS `produtos_dispensas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_dispensas` (
  `id_produto_dispensa` int NOT NULL AUTO_INCREMENT,
  `quantidade_existente` int DEFAULT NULL,
  `produto_comprado_id` int NOT NULL,
  PRIMARY KEY (`id_produto_dispensa`),
  KEY `fk_produtos_dispensas_produtos_comprados1_idx` (`produto_comprado_id`),
  CONSTRAINT `fk_produtos_dispensas_produtos_comprados1` FOREIGN KEY (`produto_comprado_id`) REFERENCES `produtos_comprados` (`id_produto_comprado`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_dispensas`
--

LOCK TABLES `produtos_dispensas` WRITE;
/*!40000 ALTER TABLE `produtos_dispensas` DISABLE KEYS */;
INSERT INTO `produtos_dispensas` VALUES (5,2,6),(6,2,6),(7,2,6),(8,2,6);
/*!40000 ALTER TABLE `produtos_dispensas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_listados_gerais`
--

DROP TABLE IF EXISTS `produtos_listados_gerais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_listados_gerais` (
  `id_produto_listado_geral` int NOT NULL AUTO_INCREMENT,
  `quantidade_listada` int NOT NULL,
  `produto_residencia_id` int NOT NULL,
  `residencia_id` int NOT NULL,
  PRIMARY KEY (`id_produto_listado_geral`),
  KEY `fk_produtos_listados_gerais_produtos_residencia1_idx` (`produto_residencia_id`),
  KEY `fk_produtos_listados_gerais_residencias1_idx` (`residencia_id`),
  CONSTRAINT `fk_produtos_listados_gerais_produtos_residencia1` FOREIGN KEY (`produto_residencia_id`) REFERENCES `produtos_residencia` (`id_produto_residencia`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_produtos_listados_gerais_residencias1` FOREIGN KEY (`residencia_id`) REFERENCES `residencias` (`id_residencia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_listados_gerais`
--

LOCK TABLES `produtos_listados_gerais` WRITE;
/*!40000 ALTER TABLE `produtos_listados_gerais` DISABLE KEYS */;
/*!40000 ALTER TABLE `produtos_listados_gerais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_listados_pessoais`
--

DROP TABLE IF EXISTS `produtos_listados_pessoais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_listados_pessoais` (
  `id_produto_listado_pessoal` int NOT NULL AUTO_INCREMENT,
  `quantidade_listada` int NOT NULL,
  `produto_residencia_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id_produto_listado_pessoal`),
  KEY `fk_produtos_listados_pessoais_produtos_residencia1_idx` (`produto_residencia_id`),
  KEY `fk_produtos_listados_pessoais_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_produtos_listados_pessoais_produtos_residencia1` FOREIGN KEY (`produto_residencia_id`) REFERENCES `produtos_residencia` (`id_produto_residencia`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_produtos_listados_pessoais_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_listados_pessoais`
--

LOCK TABLES `produtos_listados_pessoais` WRITE;
/*!40000 ALTER TABLE `produtos_listados_pessoais` DISABLE KEYS */;
INSERT INTO `produtos_listados_pessoais` VALUES (11,10,31,16),(12,10,31,16);
/*!40000 ALTER TABLE `produtos_listados_pessoais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_residencia`
--

DROP TABLE IF EXISTS `produtos_residencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_residencia` (
  `id_produto_residencia` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) NOT NULL,
  `quantidade_unid` int DEFAULT NULL,
  `unidade_de_medida` enum('kg','g','l','ml') DEFAULT NULL,
  `categoria` varchar(20) DEFAULT NULL,
  `preco_medio` float DEFAULT NULL,
  `residencia_id` int NOT NULL,
  PRIMARY KEY (`id_produto_residencia`),
  KEY `fk_produtos_residencia_residencias1_idx` (`residencia_id`),
  CONSTRAINT `fk_produtos_residencia_residencias1` FOREIGN KEY (`residencia_id`) REFERENCES `residencias` (`id_residencia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_residencia`
--

LOCK TABLES `produtos_residencia` WRITE;
/*!40000 ALTER TABLE `produtos_residencia` DISABLE KEYS */;
INSERT INTO `produtos_residencia` VALUES (27,'Leite',1,'l','bebida',NULL,5),(28,'Leite',1,'l','bebida',NULL,5),(29,'Leite',1,'l','bebida',NULL,5),(30,'Leite',1,'l','bebida',NULL,5),(31,'Leite',1,'l','bebida',NULL,5);
/*!40000 ALTER TABLE `produtos_residencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_residencia__usuarios`
--

DROP TABLE IF EXISTS `produtos_residencia__usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_residencia__usuarios` (
  `produto_residencia_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`produto_residencia_id`,`usuario_id`),
  KEY `fk_produtos_residencia__usuarios_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_produtos_residencia__usuarios_produtos_residencia1` FOREIGN KEY (`produto_residencia_id`) REFERENCES `produtos_residencia` (`id_produto_residencia`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_produtos_residencia__usuarios_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_residencia__usuarios`
--

LOCK TABLES `produtos_residencia__usuarios` WRITE;
/*!40000 ALTER TABLE `produtos_residencia__usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `produtos_residencia__usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residencias`
--

DROP TABLE IF EXISTS `residencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residencias` (
  `id_residencia` int NOT NULL AUTO_INCREMENT,
  `usuario_adm_id` int DEFAULT NULL,
  PRIMARY KEY (`id_residencia`),
  KEY `fk_residencias_usuarios1_idx` (`usuario_adm_id`),
  CONSTRAINT `fk_residencias_usuarios1` FOREIGN KEY (`usuario_adm_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residencias`
--

LOCK TABLES `residencias` WRITE;
/*!40000 ALTER TABLE `residencias` DISABLE KEYS */;
INSERT INTO `residencias` VALUES (5,15);
/*!40000 ALTER TABLE `residencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `senha` varchar(20) NOT NULL,
  `residencia_id` int DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_usuarios_residencias_idx` (`residencia_id`),
  CONSTRAINT `fk_usuarios_residencias` FOREIGN KEY (`residencia_id`) REFERENCES `residencias` (`id_residencia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (6,'User1','novo@','111',NULL),(15,'User2','6@','000',5),(16,'User2','7@','000',5);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-04 17:19:32
