-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para bd_album
CREATE DATABASE IF NOT EXISTS `bd_album` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bd_album`;

-- Volcando estructura para tabla bd_album.album
CREATE TABLE IF NOT EXISTS `album` (
  `id_album` int NOT NULL AUTO_INCREMENT,
  `album_foto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_album`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bd_album.album: ~5 rows (aproximadamente)
INSERT IGNORE INTO `album` (`id_album`, `album_foto`, `fecha`) VALUES
	(1, 'primer Album', '2023-07-29 01:38:48'),
	(2, 'sasaa', '2023-07-29 01:42:11'),
	(3, '432423', '2023-07-29 02:11:31'),
	(4, '43423', '2023-07-29 02:16:31'),
	(5, '444', '2023-07-29 02:41:55'),
	(6, '23232', '2023-07-29 03:26:22');

-- Volcando estructura para tabla bd_album.fotos
CREATE TABLE IF NOT EXISTS `fotos` (
  `id_foto` int NOT NULL AUTO_INCREMENT,
  `id_album` int DEFAULT NULL,
  `name_foto` mediumtext,
  `url_foto` longtext,
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_foto`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bd_album.fotos: ~9 rows (aproximadamente)
INSERT IGNORE INTO `fotos` (`id_foto`, `id_album`, `name_foto`, `url_foto`, `created`) VALUES
	(1, 1, 'c36e5e3c40ef4ee28048495c58d9e4bf315fabf948694653a9ffedacbf3e15df.jpg', 'upload_fotos/album_1/c36e5e3c40ef4ee28048495c58d9e4bf315fabf948694653a9ffedacbf3e15df.jpg', '2023-07-29 01:38:48'),
	(2, 1, 'abad4efce78744bbaf2a3d7bc0fde7bb68307c9a7d69454ea1a75741c89a805d.jpg', 'upload_fotos/album_1/abad4efce78744bbaf2a3d7bc0fde7bb68307c9a7d69454ea1a75741c89a805d.jpg', '2023-07-29 01:38:48'),
	(3, 1, 'a4bc7151bd484a3285ebe4033064fc1d3cb81c5394b643f59e4259ce1b97ea7d.jpg', 'upload_fotos/album_1/a4bc7151bd484a3285ebe4033064fc1d3cb81c5394b643f59e4259ce1b97ea7d.jpg', '2023-07-29 01:38:48'),
	(4, 2, '8c14463c80d8472abf727b330cb414a61e5d49bd4019497397d295616ec4f6ba.jpg', 'upload_fotos/album_2/8c14463c80d8472abf727b330cb414a61e5d49bd4019497397d295616ec4f6ba.jpg', '2023-07-29 01:42:11'),
	(5, 3, '021d8b93304a4fa3a807c2c61ec1a1d3b121cda295e84fd0b640603cf437dda3.png', 'upload_fotos/album_3/021d8b93304a4fa3a807c2c61ec1a1d3b121cda295e84fd0b640603cf437dda3.png', '2023-07-29 02:11:31'),
	(6, 3, 'fe90a17096f9427abc2bdf18748073c17492911f1bb2497a869ecd9be253fc2f.png', 'upload_fotos/album_3/fe90a17096f9427abc2bdf18748073c17492911f1bb2497a869ecd9be253fc2f.png', '2023-07-29 02:11:31'),
	(7, 4, '9cc1bd153e0b4e719de6f22aa7df7186ece1f66efa7f4fa49033f3fed5bf4bcc.png', 'upload_fotos/album_4/9cc1bd153e0b4e719de6f22aa7df7186ece1f66efa7f4fa49033f3fed5bf4bcc.png', '2023-07-29 02:16:31'),
	(8, 5, 'bd0113cfca0e46d197b4a013871cc849d50e506fdb614b3a9f41ab84fe65f8a5.jpg', 'upload_fotos/album_5/bd0113cfca0e46d197b4a013871cc849d50e506fdb614b3a9f41ab84fe65f8a5.jpg', '2023-07-29 02:41:55'),
	(9, 5, 'fbc0a649db7c4e5bb1d9c4616988ac9fe37bbd40bfa44a3f86522246b6e6513d.jpeg', 'upload_fotos/album_5/fbc0a649db7c4e5bb1d9c4616988ac9fe37bbd40bfa44a3f86522246b6e6513d.jpeg', '2023-07-29 02:41:55'),
	(10, 6, 'ea275183534d44068246a65799adde6a67b38d7858c14ce686d0c5a9a0ad25f0.jpg', 'upload_fotos/album_6/ea275183534d44068246a65799adde6a67b38d7858c14ce686d0c5a9a0ad25f0.jpg', '2023-07-29 03:26:22'),
	(11, 6, 'f81bb8f5699e4785a3e1ff731edf38a265f8d8c93384432ea73825525dee1d41.jpg', 'upload_fotos/album_6/f81bb8f5699e4785a3e1ff731edf38a265f8d8c93384432ea73825525dee1d41.jpg', '2023-07-29 03:26:22'),
	(12, 6, '44e201e2160d4f4382ff0b7aa063d557732ad8a850d1422985d79961058e52a8.jpg', 'upload_fotos/album_6/44e201e2160d4f4382ff0b7aa063d557732ad8a850d1422985d79961058e52a8.jpg', '2023-07-29 03:26:22'),
	(13, 6, '7c04505f274d4b49bad16f16f5f53e4945b09061e32d4fd18626386fdbd28e14.jpg', 'upload_fotos/album_6/7c04505f274d4b49bad16f16f5f53e4945b09061e32d4fd18626386fdbd28e14.jpg', '2023-07-29 03:26:22'),
	(14, 6, 'a7a94cb0521049aab004bbde93e123251a18330947584ba389a022bf5914e8bd.jpg', 'upload_fotos/album_6/a7a94cb0521049aab004bbde93e123251a18330947584ba389a022bf5914e8bd.jpg', '2023-07-29 03:26:22'),
	(15, 6, '1da9661025fc4d968a771cde22a568854a6fa0b94d2f4a27909fd66e77fbac8e.jpg', 'upload_fotos/album_6/1da9661025fc4d968a771cde22a568854a6fa0b94d2f4a27909fd66e77fbac8e.jpg', '2023-07-29 03:26:22');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
