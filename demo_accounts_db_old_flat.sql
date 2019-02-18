-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2018 at 11:56 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `demo_accounts_db_old_flat`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `login` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `first_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel1` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel2` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ul` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `linia_2` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `kodpocz` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `miejscowosc` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `kraj` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `company_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nip` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `login`, `email`, `first_name`, `last_name`, `tel1`, `tel2`, `ul`, `linia_2`, `kodpocz`, `miejscowosc`, `kraj`, `company_name`, `nip`) VALUES
('1914F640CB31E28C10C1', 'gracja.rutkowska2', 'grutkowska23@hotmail.com', 'Gracja', 'Rutkowska', '785841931', '', 'Al. Niepodległości 69', '', '81853', 'Sopot', 'Polska', NULL, NULL),
('208BCA2E17EF9BE955A8', 'marzena.kaczmarek2', 'mkaczmarek@nowystyl.com', 'Marzena', 'Kaczmarek', '512032549', '', 'ul. Głowackiego Bartosza 141', '', '41910', 'Bytom', 'Polska', 'NOWY STYL', '9566036567'),
('27FEE9ADCCC2F655DA79', 'uwalczak@allegro.pl', 'uwalczak@allegro.pl', 'Urszula', 'Walczak', '882364867', '', 'Międzyblokowa 57', '', '40302', 'Katowice', 'Polska', 'Allegro', '9561691143'),
('30821058C7CFAE48F49F', 'g.wieczorek', 'gwieczorek@allegro.pl', 'Gabrysz', 'Wieczorek', '692207081', '', 'Dębowa 38', '', '35113', 'Rzeszów', 'Polska', NULL, '9561691143'),
('5900FC28432EB619BA86', 'ryszkow', 'rkowalczyk@orlen.pl', 'Ryszard', 'Kowalczyk', '', '', 'Dworcowa 10', '', '10414', 'Olsztyn', 'Polska', 'PKN Orlen', '9558220974'),
('623F0D7672DAD9F4EEB4', 'marian.wozniak', 'marian.wozniak@nowystyl.com', 'Marian', 'Woźniak', '672767202', '', 'Bartnicza 55', '', '51513', 'Wrocław', 'Polska', NULL, '9566036567'),
('74F541B0A50BB5BBD3F0', 'krystyna.olszewska', 'krystynaolszewska@tooploox.com', 'Krystyna', 'Olszewska', '', '', 'Siejówka 42', '', '31998', 'Kraków', 'Polska', 'Tooploox', '9554109207'),
('796ADB91F0CC6B3A069A', 'nadzieja.walczak', 'nwalczak@nowystyl.com', 'Nadzieja', 'Walczak', '', '', ' Myśliborska 29', '', '00981', 'Warszawa', 'Polska', 'NOWY STYL', '9566036567'),
('8736AEB553A2C2A2529D', 'jozefa.gorska2', 'jgorska1@nowystyl.com', 'Józefa', 'Gorska', '667410467', '', 'ul. Rdestowa 145', '', '54530', 'Wrocław', 'Polska', 'NOWY STYL', '9566036567'),
('88C76EC5F7DBD106C8A6', 'lgrabowski', 'longin.grabowski@live.com', 'Longin', 'Grabowski', '668228971', '', 'Szeherezady 139', '', '92626', 'Łódź', 'Polska', NULL, NULL),
('988012B41A3D84517B99', 'j.rutkowska', 'jrutkowska@orlen.pl', 'Julita', 'Rutkowska', '532463461', '', 'Leśników 65', '', '40749', 'Katowice', 'Polska', 'PKN Orlen', '9558220974'),
('9AA7DCF80EE0E9593A86', 'resawicki', 'rsawicki260@live.com', 'Renard', 'Sawicki', '539135780', '', 'ul. Radomszczańska 77', '', '04764', 'Warszawa', 'Polska', NULL, NULL),
('9F20C553EDB66907AA46', 'joasia.jaworska', 'jjworska@biedronka.pl', 'Joasia', 'Jaworska', '603490751', '', 'Nehru Jawaharlala 77', '', '00719', 'Warszawa', 'Polska', 'Biedronka', '9598687530'),
('A8E82D737B8222C9D077', 'rackwiat11', 'rkwiat11@gmail.com', 'Racław', 'Kwiatkowski', '', '', 'Budryka Witolda 39', '', '30072', 'Kraków', 'Polska', NULL, NULL),
('BC2BA4790A7F9F52E438', 'franciszek.jasinski', 'fjasinski@nowystyl.com', 'Franciszek', 'Jasiński', '', '', 'Północna 101', '', '15452', 'Białystok', 'Polska', 'NOWY STYL', '9566036567'),
('BD92EA9C97A1640C40EB', 'bratumil.nowakowski', 'bnowakowski@gmail.com', 'Bratumił', 'Nowakowski', '722163628', '', 'ul. Daleka 144', '', '35231', 'Rzeszów', 'Polska', NULL, NULL),
('DA5A09DBF6B232194DCC', 'krystyna.olszewska2', 'krstna888@hotmail.com', 'Krystyna', 'Olszewska', '536092232', '', 'Łąkowa 91', '', '75669', 'Koszalin', 'Polska', NULL, NULL),
('E05AF29A19EDD025D956', 'waleria.tomaszewska', 'walto@tooploox.com', 'Waleria', 'Tomaszewska', '782740367', '', 'ul. Salezjańska 57', '', '53650', 'Wrocław', 'Polska', 'Tooploox', '9554109207'),
('FEFDF9E667001FAEAD15', 'iwo.sobczak', 'isobczak@orlen.pl', 'Iwo', 'Sobczak', '794354601', '', 'ul. Krynicka 29', '', '91219', ' Łódź', 'Polska', 'PKN Orlen', '9558220974');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `login` (`login`),
  ADD UNIQUE KEY `email` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
