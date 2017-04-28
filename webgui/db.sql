CREATE TABLE `requests` (
  `id` int(3) NOT NULL,
  `email` varchar(30) NOT NULL,
  `hostname` varchar(30) NOT NULL,
  `adv` int(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
