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
-- Database: `demo_accounts_db_new`
--

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

CREATE TABLE `companies` (
  `company_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `nip_fk` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `companies`
--

INSERT INTO `companies` (`company_name`, `email`, `nip_fk`) VALUES
('International Corporation, Inc.', 'contact@intlcorp.com', '2394050030'),
('Wolne Lektury', 'webmaster@wolnelektury.pl', '9551401657'),
('Allegro', 'contact@allegro.pl', '9561691143'),
('Biedronka', 'mail@biedronka.pl', '9598687530');

-- --------------------------------------------------------

--
-- Table structure for table `unique_id`
--

CREATE TABLE `unique_id` (
  `ID` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `is_corporate` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `unique_id`
--

INSERT INTO `unique_id` (`ID`, `is_corporate`) VALUES
('050C071D65AEE34EC63E', 0),
('2394050030', 1),
('406E60E2ED22D9855B46', 0),
('5CBF843B4870D5010EC9', 0),
('79A01714A8CAA8AC5B60', 0),
('9551401657', 1),
('9561691143', 1),
('9598687530', 1),
('BC9ED612261D96BECB7E', 0),
('CC53FC6C98E3DC2DC60B', 0),
('DDEC8A1E243DD6479DC7', 0),
('E156B690BF688D66081A', 0);

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
  `nip` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `login`, `email`, `first_name`, `last_name`, `tel1`, `tel2`, `ul`, `linia_2`, `kodpocz`, `miejscowosc`, `kraj`, `nip`) VALUES
('050C071D65AEE34EC63E', 'aleksander.lesiak', NULL, 'Aleksander', 'Lesiak', '605460835', '', 'Armii Krajowej 41', '', '40671', 'Katowice', 'Polska', NULL),
('9551401657', 'arnold.rajewski', 'arajewski@wolnelektury.pl', 'Arnold', 'Rajewski', '783792860', '', 'Armii Krajowej 40', '', '42202 ', 'Częstochowa', 'Polska', '9551401657'),
('9561691143', 'bazyli.biedrzycki', 'bbiedrzycki@allegro.pl', 'Bazyli', 'Biedrzycki', '', '672767202', 'Listopadowa 58', '', '92006', 'Łódź', 'Polska', '9561691143'),
('BC9ED612261D96BECB7E', 'bozena.komorowska', 'bkomorowska@gmail.com', 'Bożena', 'Komorowska', '881429669', '', 'Koło Benniego 13', '', '97204', 'Tomaszów Mazowiecki', 'Polska', NULL),
('79A01714A8CAA8AC5B60', 'daria.antczak', 'dantczak@gmail.com', 'Daria', 'Antczak', '786442645', '', 'Izerska 114', '', '85689', 'Bydgoszcz', 'Polska', NULL),
('9561691143', 'dariusz.kielb', 'dkielb@allegro.pl', 'Dariusz', 'Kielb', '', '672767202', 'Motylowa 2', '', '20826', 'Lublin', 'Polska', '9561691143'),
('CC53FC6C98E3DC2DC60B', 'edyta.iwanicka', NULL, 'Edyta', 'Iwanicka', '', '', 'Obrońców Warszawy 32', '', '91850', 'Łódź', 'Polska', NULL),
('9598687530', 'hugo.pianka', 'hpianka@biedronka.pl', 'Hugo', 'Pianka', '721329619', '791169402', 'Towarnickiego Ambrożego 124', '', '35010', 'Rzeszów', 'Polska', '9598687530'),
('9561691143', 'jerzy.dudek', 'jdudek@allegro.pl', 'Jerzy', 'Dudek', '786950555', '672767202', 'Wędkarska 29', '', '04869', 'Warszawa', 'Polska', '9561691143'),
('DDEC8A1E243DD6479DC7', 'lucyna.grech', NULL, 'Lucyna', 'Grech', '', '', 'Rozstajna 116', '', '20347', 'Lublin', 'Polska', NULL),
('2394050030', 'mateusz.gretsky', 'mgretsky@intlcorp.com', 'Mateusz', 'Gretsky', '15016555127', '13052235897', '102 Fountain Lake Rd.', 'Apt. #2', '30422', 'Heber Springs, N. Dakota', 'USA', '2394050030'),
('406E60E2ED22D9855B46', 'maurycy.sokal', 'msokal@gmail.com', 'Maurycy', 'Sokal', '', '', '', '', '', '', 'Polska', NULL),
('9561691143', 'melania.woida', 'mwoida@allegro.pl', 'Melania', 'Woida', '', '672767202', 'Chlebowa 112', '', '61003', 'Poznań', 'Polska', NULL),
('5CBF843B4870D5010EC9', 'miroslawa.kaczmarczyk', 'mkaczmarczyk@live.com', 'Mirosława', 'Kaczmarczyk', '536092232', '', '', '', '', '', 'Polska', NULL),
('9551401657', 'miroslawa.waglowa', 'mwaglowa@wolnelektury.pl', 'Mirosława', 'Waglowa', '787656298', '', 'Dziurawcowa 68', '', '61680', 'Poznań', 'Polska', '9551401657'),
('E156B690BF688D66081A', 'nadzieja.lesak', 'nlesak@gmail.com', 'Nadzieja', 'Lesak', '723832927', '722749283', 'Kaczeńcowa 117', '', '81575', 'Gdynia', 'Polska', NULL),
('9561691143', 'przemysl.hebda', 'phebda@allegro.pl', 'Przemysł', 'Hebda', '668930215', '672767202', '', '', '', '', 'Polska', '9561691143'),
('9598687530', 'sabina.nieswiastowska', 'snieswiastowska@biedronka.pl', 'Sabina', 'Nieswiastowska', '', '791169402', 'Biskupińska 125', '', '60416', 'Poznań', 'Polska', '9598687530'),
('9598687530', 'serafin.zaleski', 'szaleski@biedronka.pl', 'Serafin', 'Zaleski', '', '791169402', 'Eluarda Pawła 51', '', '54019', 'Wrocław', 'Polska', '9598687530'),
('9551401657', 'szarlota.robak', 'srobak@wolnelektury.pl', 'Szarlota', 'Robak', '603966092', '', 'Goździków 3', '', '04231', 'Warszawa', 'Polska', '9551401657');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `companies`
--
ALTER TABLE `companies`
  ADD PRIMARY KEY (`nip_fk`),
  ADD UNIQUE KEY `nip_fk` (`nip_fk`);

--
-- Indexes for table `unique_id`
--
ALTER TABLE `unique_id`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `ID` (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`login`),
  ADD UNIQUE KEY `login` (`login`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `nip` (`nip`),
  ADD KEY `ID` (`ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `companies`
--
ALTER TABLE `companies`
  ADD CONSTRAINT `companies_ibfk_1` FOREIGN KEY (`nip_fk`) REFERENCES `unique_id` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`nip`) REFERENCES `companies` (`nip_fk`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `users_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `unique_id` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
